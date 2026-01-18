## Volatility forensics

The analysis was performed using a virtual machine with FLARE-VM installed.

### What is the Operating System of this Dump file? (OS name)
```BASH
python vol.py -f <filename>.raw windows.info
```

![alt text](image.png)

### What is the PID of SearchIndexer?

```BASH
python vol.py -f <filename>.raw windows.pslist
```
![alt text](image-1.png)

## Task 2

### There are many suspicious open ports; which one is it? (ANSWER format: protocol:port)

```BASH
python vol.py -f <filename>.raw windows.netscan
```
![alt text](image-2.png)

### Vads tag and execute protection are strong indicators of malicious processes; can you find which they are? (ANSWER format: Pid1;Pid2;Pid3) 

```BASH
python vol.py -f <filename>.raw windows.malfind > malfind.txt
```
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)

## IOC SAGA

```BASH
python vol.py -f <filename>.raw windows.memmap --pid <PID_NUMBER> --dump

strings -n 6 pid.<PID_NUMBER>*.dmp > strings_<PID_NUMBER>.txt

findstr /i "www.go" strings_<PID_NUMBER>.txt
findstr /i "www.i" strings_<PID_NUMBER>.txt
findstr /i "www.ic" strings_<PID_NUMBER>.txt

findstr /R "[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*" strings_<PID_NUMBER>.txt > file.txt

python vol.py -f <filename>.raw windows.envars --pid <PID_NUMBER>
```


