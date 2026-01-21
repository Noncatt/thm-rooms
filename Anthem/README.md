# Anthem Report 

## Summary
A misconfigured Umbraco CMS installation running on TCP 80 allowed disclosure of sensitive credentials via predictable files, administrative account compromise, and subsequent RDP access to a Windows machine. Insufficient file system permissions enabled local privilege escalation to retrieve administrative passwords and full control over the host.

<span>&nbsp;</span>

| Risk  | Impact | Severity |
| --- | --- | --- |
| Remote Desktop compromise | Full system access | Critical
| Misconfigured file permissions | Privilege escalation | High

<span>&nbsp;</span>

## Scope
The assessment was limited to a single internet-accessible Windows host at IP 10.10.x.x. Black-box testing — no credentials or prior knowledge provided.

<span>&nbsp;</span>

## Methodology
- Enumeration
- Vulnerability Analysis
- Exploitation
- Privilege Escalation
- Post-Exploitation

<span>&nbsp;</span>

## Environment Overview
The target environment consists of a single Windows-based machine running vulnerable web services. Enumeration revealed the following:

Port | Service | Version |
| --- | --- | --- | 
80 | Microsoft HTTPAPI httpd 2.0 | Windows internal web service |
3389 | Microsoft Terminal Services | RDP |
5985 | Microsoft HTTPAPI httpd 2.0 | WinRM service |

- Operating System: Microsoft Windows (version unspecified)
- CMS: Umbraco (hosted on internal HTTP server)
- Remote Management: RDP and WinRM exposed
- Backup Files: Located in `C:\backup\`

<span>&nbsp;</span>

## Identified Vulnerabilities
### Discovery of Hardcoded Password in robots.txt
- **Vector:** Accessible robots.txt file disclosed a plaintext password.  

- **Proof of Concept**:   

    ```
    http://$ip/robots.txt 
    ```
    contains password `UmbracoIsTheBest!`  

- **Impact:** Knowledge of internal password aiding in further authentication attempts.  

<span>&nbsp;</span>

### Enumeration of Administrator Identity and Email
- **Vector:** Public pages contained administrator's email pattern.

- **Proof of Concept:** The hiring post references initials for email on employees and poem matched the administrator `Solomon Grundy`.

- **Impact:** Identification of privileged account for credential guessing or phishing.

<span>&nbsp;</span>

### Retrieval of Hidden Flags through Source Inspection and Directory Enumeration
- **Vector:** Hidden flags embedded in source code and obscure directories.

- **Proof of Concept:** Page source inspection revealed flags like THM{G!T_G00D} and Gobuster enumeration of /authors revealed hidden content

- **Impact:** No direct security risk. Task-specific discovery.

<span>&nbsp;</span>

### RDP Access with Recovered Credentials
- **Vector:** Using credentials obtained through earlier enumeration, authenticated via RDP.

- **Proof of Concept:**
```BASH
rdesktop $ip
Username: SG
Password: UmbracoIsTheBest!
```

- **Impact: Full desktop access as a regular user.**

<span>&nbsp;</span>

### Privilege Escalation via File System Permission Misconfigurations
- **Vector:** Backup file restore.txt had misconfigured permissions allowing standard users to grant themselves access.

- **Proof of Concept:**
    - Navigate to C:\backup
    - Modify file permissions via GUI
    - Access restore.txt
    - Password: `ChangeMeBaby1MoreTime`

- **Impact:** Elevation to local administrator privileges.

<span>&nbsp;</span>

### Root Flag Retrieval as Administrator
- **Vector:** Login as Administrator

- **Proof of Concept:** Retrieve root.txt directly from Administrator Desktop.

- **Impact:** Complete system takeover.

<span>&nbsp;</span>

## Walktrough
Run an Nmap service scan to identify open ports and running services:
```BASH
sudo nmap -sV -p- $ip
```
![alt text](image.png)

<span>&nbsp;</span>

### What port is for the web server?
<pre>80</pre>

<span>&nbsp;</span>

### What port is for remote desktop service?
<pre>3389</pre>

<span>&nbsp;</span>

### What is a possible password in one of the pages web crawlers check for?
Web crawlers check for `robots.txt` so go there.    

![alt text](image-3.png)
<pre>UmbracoIsTheBest!</pre>

<span>&nbsp;</span>

### What CMS is the website using?
<pre>umbraco</pre>

<span>&nbsp;</span>

### What is the domain of the website?
<pre>anthem.com</pre>

<span>&nbsp;</span>

### What's the name of the Administrator
For this one you have to search poem in search engine. 
![alt text](image-5.png)
<pre>Solomon Grundy</pre>

<span>&nbsp;</span>

### Can we find find the email address of the administrator?
In "We are hiring" post mówi o zatrudnieniu kgoś nowego i autor postu podaje swój email. Są to inicjały i domena. Czyli administartolr musi mieć podobny email.
<pre>SG@anthem.com</pre>

<span>&nbsp;</span>

Use Gobuster to enumerate hidden directories:
```BASH
gobuster dir -u "http://10.10.50.147/" -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 64
```
![alt text](image-7.png)

<span>&nbsp;</span>

## Spot the flags

What is flag 1?
![alt text](image-6.png)  
THM{L0L_WH0_US3S_M3T4}

What is flag 2?
There is second flag, in page view source:    
![alt text](image-1.png)
THM{G!T_G00D}

What is flag 3?
Enumerate website using gobuster. One from many directories will be `/authors` directory, here is third flag.
![alt text](image-2.png)
THM{L0L_WH0_D15}  

What is flag 4?
The same as second flag, from view page source.
![alt text](image-4.png)
THM{AN0TH3R_M3TA}

<span>&nbsp;</span>

## Final stage

### Gain initial access to the machine, what is the contents of user.txt?
Install rdesktop to log in to Windows machine with gained credentials. 

```BASH
sudo apt install rdesktop
rdesktop $ip
```
![alt text](image-9.png)
<pre>THM{N00T_NO0T}</pre>

### Can we spot the admin password?

![alt text](image-10.png)  

Looks like C:\backup\ contains backup files. Go to backup directory:  

![alt text](image-11.png)

Access is denied to read file.  

![alt text](image-12.png)

In file explorer go to where restore.txt stayes. Click properties -> Security. Edit Group or user names. In popu window Add new user `WIN-LU09299160F\SG`. 
![alt text](image-13.png)

Click save and gave yourself all permissions:
![alt text](image-14.png)

<pre>ChangeMeBaby1MoreTime</pre>

### Escalate your privileges to root, what is the contents of root.txt?
Relog yourself as administrator. On desktop there is root file:  

![alt text](image-15.png)
<pre>THM{Y0U_4R3_1337}</pre>



