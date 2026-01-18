## Volatility forensics

The analysis was performed using a virtual machine with FLARE-VM installed.

### What is the Operating System of this Dump file? (OS name)
```BASH
python vol.py -f <filename>.raw windows.info
```

<img width="407" height="76" alt="image" src="https://github.com/user-attachments/assets/09417ac2-576a-4e8f-86d0-70730921c4d9" />

### What is the PID of SearchIndexer?

```BASH
python vol.py -f <filename>.raw windows.pslist
```

<img width="1208" height="38" alt="image-1" src="https://github.com/user-attachments/assets/a2357a68-6c87-4f37-9cd4-a4f5513a19d7" />

<span style="line-height:0.5;">&nbsp;</span>

## Task 2

### There are many suspicious open ports; which one is it? (ANSWER format: protocol:port)

```BASH
python vol.py -f <filename>.raw windows.netscan
```

<img width="1162" height="102" alt="image-2" src="https://github.com/user-attachments/assets/db6e9236-a594-46d9-9113-6819157bd4e4" />

### Vads tag and execute protection are strong indicators of malicious processes; can you find which they are? (ANSWER format: Pid1;Pid2;Pid3) 

```BASH
python vol.py -f <filename>.raw windows.malfind > malfind.txt
```

<img width="1025" height="43" alt="image-3" src="https://github.com/user-attachments/assets/e0ff02a3-3501-4d07-ac8e-0bc52b94c509" />

<img width="1103" height="37" alt="image-4" src="https://github.com/user-attachments/assets/ea2e0937-ee2d-49d4-ab9c-20c76f7640f9" />

<img width="1038" height="67" alt="image-5" src="https://github.com/user-attachments/assets/597fa25e-0c52-4cf8-9e40-51e9c23c031f" />

<span style="line-height:0.5;">&nbsp;</span>

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


