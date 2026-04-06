## What is the name of the Content Management System (CMS) installed on the server?

```TEXT
Cockpit
```

<span>&nbsp;</span>

## What is the version of the Content Management System (CMS) installed on the server?

![alt text](image.png)
```TEXT
0.11.1
```

<span>&nbsp;</span>

## What is the path that allow user enumeration?

![alt text](image-1.png)
```TEXT
/auth/check
```

<span>&nbsp;</span>

## How many users can you identify when you reproduce the user enumeration attack?

![alt text](image-2.png)

![alt text](image-3.png)

<span>&nbsp;</span>

## What is the path that allows you to change user account passwords?

```TEXT
/auth/resetpassword
```

<span>&nbsp;</span>

## Compromise the Content Management System (CMS). What is Skidy's email.

![alt text](image-6.png)

![alt text](image-5.png)

<span>&nbsp;</span>

What is the web flag?

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

<span>&nbsp;</span>

## Compromise the machine and enumerate collections in the document database installed in the server. What is the flag in the database?

![alt text](image-12.png)

![alt text](image-10.png)

![alt text](image-11.png)

Go to: `http://$machine-ip/php-reverse-shell.php` to trigger reverse shell.

```BASH
python3 -c 'import pty; pty.spawn("/bin/bash")' 
```

![alt text](image-13.png)

![alt text](image-14.png)

<span>&nbsp;</span>

## What is the user.txt flag?

![alt text](image-15.png)

```BASH
p4ssw0rdhack3d!123
```

```
su stux
```

![alt text](image-16.png)

<span>&nbsp;</span>

## What is the CVE number for the vulnerability affecting the binary assigned to the system user? Answer format: CVE-0000-0000

![alt text](image-17.png)

```TEXT
CVE-2021-22204
```

<span>&nbsp;</span>

## What is the utility used to create the PoC file?

```TEXT
djvumake
```

<span>&nbsp;</span>

## Escalate your privileges. What is the flag in root.txt?

Use gtfobins.

```BASH
sudo exiftool -filename=/home/stux/root.txt /root/root.txt
```

![alt text](image-18.png)

