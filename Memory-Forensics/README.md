## Login

> The forensic investigator on-site has performed the initial forensic analysis of John's computer and handed you the memory dump he generated on the computer. As the secondary forensic investigator, it is up to you to find all the required information in the memory dump.

The analysis was performed using a virtual machine with FLARE-VM installed. To retrieve user password hashes from memory, the following Volatility 3 command was used:

```BASH
python vol.py -f <filename>.vmem windows.hashdump
```

![alt text](image-1.png)

After obtaining John’s NTLM hash, the hash was transferred to the AttackBox environment. The hash was saved to a file named password.hash, and Hashcat was used with the rockyou wordlist:

```BASH
hashcat -m 1000 password.hash /usr/share/wordlists/rockyou.txt
```

The cracking process revealed John’s plaintext password:

![alt text](image-2.png)

<span style="line-height:0.5;">&nbsp;</span>

## Analysis

> On arrival a picture was taken of the suspect's machine, on it, you could see that John had a command prompt window open. The picture wasn't very clear, sadly, and you could not see what John was doing in the command prompt window. To complete your forensic timeline, you should also have a look at what other information you can find, when was the last time John turned off his computer?

<span style="line-height:0.5;">&nbsp;</span>

### When was the machine last shutdown?
System information was retrieved using the following command:
```BASH
python vol.py -f <filename>.vmem windows.info
```

The shutdown time was located in the Windows registry:
```BASH
python vol.py -f <filename>.vmem  windows.registry.printkey --offset 0xf8a000024010 --key "ControlSet001\Control\Windows"
```
![alt text](image-3.png)

The ShutdownTime value was decoded from FILETIME format, resulting in the following UTC timestamp:

```
2020-12-27 22:50:12
```

<span style="line-height:0.5;">&nbsp;</span>

### What did John write?

Printable strings were extracted from the memory image.

```BASH
strings <filename>.vmem > strings.txt
```

The memory dump was searched for printable strings to identify possible user input.
A search for the `THM{` pattern revealed a flag present in memory.

![alt text](image-4.png)

<span style="line-height:0.5;">&nbsp;</span>

## TrueCrypt
> A common task of forensic investigators is looking for hidden partitions and encrypted files, as suspicion arose when TrueCrypt was found on the suspect's machine and an encrypted partition was found. The interrogation did not yield any success in getting the passphrase from the suspect, however, it may be present in the memory dump obtained from the suspect's computer.

The Volatility 3 plugin windows.truecrypt.Passphrase was used. Due to a known issue with Windows 7 memory images, the plugin required a small patch before it could work correctly.

![alt text](image-6.png)

The following file was edited:

![alt text](image-8.png)

Lines 80-82 were commented out and replaced with:

```BASH
count, not_aligned = divmod(size, DWORD_SIZE_BYTES)
```
![alt text](image-9.png)

After saving the changes, the plugin was executed using the following command:

```BASH
python vol.py -f <filename>.vmem windows.truecrypt.Passphrase
```

![alt text](image-10.png)