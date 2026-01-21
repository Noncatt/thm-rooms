## User.txt

The target system was identified as running Fuel CMS version 1.4.1. This specific version is vulnerable to a Server-Side Template Injection (SSTI) flaw in the /fuel/pages/select/ endpoint, allowing for unauthenticated Remote Code Execution (RCE).

![alt text](image.png)

A local listener was initialized using:

```BASH
nc -lvnp 4444
```
The server initiated a connection from victim ip, granting access as the www-data service account.

![alt text](image-7.png)

The shell was upgraded to a full TTY using the following Python command:

![alt text](image-8.png)

![alt text](image-12.png)

<span style="line-height:0.5;">&nbsp;</span>

## Root.txt
Examination of the `fuel/application/config/database.php` file revealed hardcoded database credentials:
```BASH
cat fuel/application/config/database.php
```

![alt text](image-9.png)

```BASH
su root
```

![alt text](image-10.png)



