## User.txt

The target system was identified as running Fuel CMS version 1.4.1. This specific version is vulnerable to a Server-Side Template Injection (SSTI) flaw in the /fuel/pages/select/ endpoint, allowing for unauthenticated Remote Code Execution (RCE).

<img width="1181" height="745" alt="image" src="https://github.com/user-attachments/assets/069e888f-6d1d-4ee1-8221-c7e5eab5314b" />

A local listener was initialized using:

```BASH
nc -lvnp 4444
```
The server initiated a connection from victim ip, granting access as the www-data service account.

<img width="538" height="326" alt="image-7" src="https://github.com/user-attachments/assets/c8c42d72-95af-4694-b107-ddae598ee4af" />

The shell was upgraded to a full TTY using the following Python command:

<img width="464" height="45" alt="image-8" src="https://github.com/user-attachments/assets/f8c2272b-c6bb-49e3-aa44-fd03215aa783" />

<img width="591" height="130" alt="image-12" src="https://github.com/user-attachments/assets/f5b58917-48e2-4026-a6f8-71effb0c7a29" />

<span style="line-height:0.5;">&nbsp;</span>

## Root.txt
Examination of the `fuel/application/config/database.php` file revealed hardcoded database credentials:
```BASH
cat fuel/application/config/database.php
```

<img width="576" height="554" alt="image-9" src="https://github.com/user-attachments/assets/6e741902-cded-4635-8b3e-ce92e87ee719" />

```BASH
su root
```

<img width="440" height="60" alt="image-10" src="https://github.com/user-attachments/assets/7d46c014-f9fa-436f-96ac-034eed7f86a7" />


