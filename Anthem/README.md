Run an Nmap service scan to identify open ports and running services:
```BASH
sudo nmap -sV -p- $ip
```
<img width="640" height="180" alt="image" src="https://github.com/user-attachments/assets/6cff7d9e-daf5-41f1-9d2b-65a662bf4619" />

<span>&nbsp;</span>

### What port is for the web server?
<pre>80</pre>

<span>&nbsp;</span>

### What port is for remote desktop service?
<pre>3389</pre>

<span>&nbsp;</span>

### What is a possible password in one of the pages web crawlers check for?
Web crawlers check for `robots.txt` so go there.    

<img width="622" height="239" alt="image-3" src="https://github.com/user-attachments/assets/5e2b335c-24af-4b77-ab4b-e4479950d391" />

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

<img width="753" height="138" alt="image-5" src="https://github.com/user-attachments/assets/8cc6ec5d-6d4f-4d1b-bf12-8abf3c5dfab2" />

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
<img width="612" height="327" alt="image-7" src="https://github.com/user-attachments/assets/04766091-776a-45eb-a325-201fabac5d65" />

<span>&nbsp;</span>

## Spot the flags

What is flag 1?

<img width="624" height="208" alt="image-6" src="https://github.com/user-attachments/assets/36f6972f-8934-4d44-9086-3b3ac92c04f0" />

<span>&nbsp;</span>

What is flag 2?

There is second flag, in page view source:  

<img width="884" height="117" alt="image-1" src="https://github.com/user-attachments/assets/e97286ef-b191-4da7-84f5-4d8306e39f25" />

<span>&nbsp;</span>

What is flag 3?

Enumerate website using gobuster. One from many directories will be `/authors` directory, here is third flag.

<img width="716" height="611" alt="image-2" src="https://github.com/user-attachments/assets/b8578f41-4abb-4225-9124-7451339807d3" />

<span>&nbsp;</span>

What is flag 4?

The same as second flag, from view page source.

<img width="753" height="225" alt="image-4" src="https://github.com/user-attachments/assets/30a4fc88-4b30-4047-8424-cf3e55cb609d" />

<span>&nbsp;</span>

## Final stage

### Gain initial access to the machine, what is the contents of user.txt?
Install rdesktop to log in to Windows machine with gained credentials. 

```BASH
sudo apt install rdesktop
rdesktop $ip
```

<img width="805" height="513" alt="image-9" src="https://github.com/user-attachments/assets/55a58947-ce80-4225-8b75-dc054565ea8b" />

### Can we spot the admin password?

<img width="760" height="410" alt="image-10" src="https://github.com/user-attachments/assets/4f382dee-59ae-4eee-8fc9-2b7423be69b6" />

Looks like C:\backup\ contains backup files. Go to backup directory:  

<img width="433" height="234" alt="image-11" src="https://github.com/user-attachments/assets/7bbed321-588e-4c54-b66f-3c1391e0575c" />

Access is denied to read file.  

<img width="428" height="43" alt="image-12" src="https://github.com/user-attachments/assets/3629727e-205e-4622-8deb-61f4ba52882e" />

In file explorer go to where restore.txt stayes. Click properties -> Security. Edit Group or user names. In popu window Add new user `WIN-LU09299160F\SG`. 

<img width="445" height="244" alt="image-13" src="https://github.com/user-attachments/assets/eb716d86-6fd3-4d59-a451-f5ae9fc1fd03" />

Click save and gave yourself all permissions:

<img width="333" height="158" alt="image-14" src="https://github.com/user-attachments/assets/8639be12-5cf6-4d83-8973-16f837700a32" />

<pre>ChangeMeBaby1MoreTime</pre>

### Escalate your privileges to root, what is the contents of root.txt?
Relog yourself as administrator. On desktop there is root file with flag:  

<img width="840" height="481" alt="image-15" src="https://github.com/user-attachments/assets/b6fe4a6f-c72a-4800-8668-284eb3915ae1" />




