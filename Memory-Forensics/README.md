## Login

> The forensic investigator on-site has performed the initial forensic analysis of John's computer and handed you the memory dump he generated on the computer. As the secondary forensic investigator, it is up to you to find all the required information in the memory dump.

The analysis was performed using a virtual machine with FLARE-VM installed. To retrieve user password hashes from memory, the following Volatility 3 command was used:

```BASH
python vol.py -f <filename>.vmem windows.hashdump
```

<img width="826" height="77" alt="image-1" src="https://github.com/user-attachments/assets/9c88d5b4-86c9-4f53-85c2-e56b9da48b33" />

After obtaining John’s NTLM hash, the hash was transferred to the AttackBox environment. The hash was saved to a file named password.hash, and Hashcat was used with the rockyou wordlist:

```BASH
hashcat -m 1000 password.hash /usr/share/wordlists/rockyou.txt
```

The cracking process revealed John’s plaintext password:

<img width="544" height="128" alt="image-2" src="https://github.com/user-attachments/assets/569f1062-366e-40b8-ac2e-cc5694a3952d" />

<span style="line-height:0.5;">&nbsp;</span>

## Analysis

> On arrival a picture was taken of the suspect's machine, on it, you could see that John had a command prompt window open. The picture wasn't very clear, sadly, and you could not see what John was doing in the command prompt window. To complete your forensic timeline, you should also have a look at what other information you can find, when was the last time John turned off his computer?

### When was the machine last shutdown?
System information was retrieved using the following command:
```BASH
python vol.py -f <filename>.vmem windows.info
```

The shutdown time was located in the Windows registry:
```BASH
python vol.py -f <filename>.vmem  windows.registry.printkey --offset 0xf8a000024010 --key "ControlSet001\Control\Windows"
```

<img width="1335" height="59" alt="image-3" src="https://github.com/user-attachments/assets/c2fdb3aa-e573-4bcd-9b70-a6bc6e6c1c8e" />

The ShutdownTime value was decoded from FILETIME format, resulting in the following UTC timestamp:

```
2020-12-27 22:50:12
```

<span style="line-height:0.5;">&nbsp;</span>

### What did John write?

Printable strings were extracted from the memory image:

```BASH
strings <filename>.vmem > strings.txt
```

The memory dump was searched for printable strings to identify possible user input.
A search for the `THM{` pattern revealed a flag present in memory:

<img width="577" height="264" alt="image-4" src="https://github.com/user-attachments/assets/d0d826da-8493-47c9-8a9a-7299af7b821d" />

<span style="line-height:0.5;">&nbsp;</span>

## TrueCrypt
> A common task of forensic investigators is looking for hidden partitions and encrypted files, as suspicion arose when TrueCrypt was found on the suspect's machine and an encrypted partition was found. The interrogation did not yield any success in getting the passphrase from the suspect, however, it may be present in the memory dump obtained from the suspect's computer.

The Volatility 3 plugin windows.truecrypt.Passphrase was used. Due to a known issue with Windows 7 memory images, the plugin required a patch before it could work correctly.

<img width="513" height="92" alt="image-6" src="https://github.com/user-attachments/assets/8d5a9ecd-cdd8-4894-b337-5c255e02207a" />

The following file was edited:

<img width="673" height="57" alt="image-8" src="https://github.com/user-attachments/assets/f4df878b-64d0-442f-b20a-f47aec99bdba" />

Lines 80-82 were commented out and replaced with:

```BASH
count, not_aligned = divmod(size, DWORD_SIZE_BYTES)
```

<img width="705" height="72" alt="image-9" src="https://github.com/user-attachments/assets/29d69cab-ca15-4ae2-80c6-9cbfc6eac8d1" />

After saving the changes, the plugin was executed using the following command:

```BASH
python vol.py -f <filename>.vmem windows.truecrypt.Passphrase
```

<img width="518" height="144" alt="image-10" src="https://github.com/user-attachments/assets/33e9f192-48ff-4aeb-adb1-23b1db13b653" />
