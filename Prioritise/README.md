Visiting `/` shows a plain TODO list

![image](https://github.com/user-attachments/assets/f4acaa1f-85f9-44a4-ba54-efbf72954727)

Try to add new item and catch request in Burp to see how request looks.

![image-1](https://github.com/user-attachments/assets/1cce8111-7cb1-4900-9502-724bb947e2e1)

Manually replacing the value with `5` makes the server respond with `HTTP 500`, while returning it to a valid value such as `1` restores the usual `302 redirect`.

![image-7](https://github.com/user-attachments/assets/4d7f83fd-9b66-4731-80f5-c60fa43d1563)

With the oracle in place we can interrogate the SQLite database one byte at a time. SQLite comparisons are normally case-insensitive, so instead of comparing characters directly we compare their hexadecimal codes. For one byte the payload looks like this:
```
/?order=(CASE WHEN (hex(substr((SELECT group_concat(name) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'),1,1))='66') THEN 5 ELSE 1 END)
```

Wrapping this in `CASE WHEN` gives a yes/no for `?order=(CASE WHEN <condition> THEN 5 ELSE 1 END)`. By asking is the next byte of hex equal to X and watching for 500 or 302 HTTP, a script brute-forces table names, column names, and finally the flag. 

![image-9](https://github.com/user-attachments/assets/3d6a738f-afe7-4aac-8140-0617b43b97ad)


