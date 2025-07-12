# Project: SQL, noSQL Injection

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/J54H7V94REZLYMSB.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [SQL vs. NoSQL: What’s the difference ?](/rltoken/cgoqub0wuNsKcF9DSQ70CQ)
* [Understanding SQL Injection](/rltoken/Wb_szl6ocNgbOZr_i6lu3g)
* [SQL Injection Knowledge Base](/rltoken/8aSZmrSs5JLUkhUzU2AG5Q)
* [A Comprehensive Guide To NoSQL Injection](/rltoken/E98hdaw3KjH4M2Cw7OSfrA)
* [NoSQL Injections: Overview and Prevention](/rltoken/7Ts8_Kgy0ymMLlBFdzNHXg)
* [SQL vs NoSQL or MySQL vs MongoDB](/rltoken/mwZoK-bI6rmxUuJ-BkQFGg)
* [Preventing SQL Injection Vulnerabilities](/rltoken/dNG2qyyov1zE2rusE-fGtg)

#### References:

* [OWASP: SQL Injection Prevention Cheat Sheet](/rltoken/8RUTNQHUZGqO-a2hdy8HOQ)
* [Hacker Tricks: SQL Injection](/rltoken/lAHl0B6TtDcxxweC4N48dQ)
* [Hacker Tricks: NoSQL Injection](/rltoken/UTct8ulMj6W4K-ADyaBM9g)
* [MITRE: CWE-89: SQL Injection](/rltoken/Xscdm_Pfj_SCNcXDAT8tyA)
* [MITRE: CWE-943: Improper Neutralization of NoSQL Query Syntax](/rltoken/LaT6YMbcTHaR2sAf2TLA4g)


## Learning Objectives

* What isSQL Injection?
* How doesnoSQL Injectiondiffer?
* What are the risks ofSQL Injection?
* Describe aUNION attack.
* ExplainBlind SQL Injection.
* How to preventSQL Injections?
* What is aParameterized Query?
* What areStored Proceduresin SQL?
* Why isInput Validationimportant?
* How doesnoSQL Injectionoccur in MongoDB?
* What is the role ofORMsin preventing injections?
* CannoSQL Databaseslike MongoDB be injected?
* What isEscaping User Inputin SQL queries?
* Explain the use ofLIMITin SQL injection attacks.
* How to useRegular Expressionsfor input validation?
* What is aNoSQL Injection Attack Vector?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetcyber_websec_0x01.


## Tasks

### 0. SQLi - Basic Injection Discovery

The first step in exploiting SQL injection vulnerabilities is to identify which parameters are vulnerable.Your goal is to identify which parameters in the application’s web pages are susceptible to SQL injection attacks. For that you should:





* Access the machinecyber_websec_0x01through the VPN.
* Navigate to:http://web0x01.hbtn/a3/sql_injection/. (dont forget to edit your /etc/hosts)
* Search for the vulnerable paramters.
* $ echo "paramters_name" > 0-vuln.txt

```bash
$ echo "paramters_name" > 0-vuln.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:0-vuln.txt

### 1. SQLi - Extracting Database Information

Now that you’ve identified a vulnerable parameter, your next task is to find aflag⛳️:





* Extract information about the database itself:DatabaseVersion.Tables.
* DatabaseVersion.
* Tables.

```bash
Helpful Instructions:
1. To determine the Database Version, Craft a payload that causes the application to reveal the version of the database it's using.
  -  This might involve using functions likeversion()in MySQL or@@VERSIONin Microsoft SQL Server.
2. To identify All Table Names: Modify your payload to extract the names of all tables within the database.
  -  This will likely require knowledge of database-specific system tables or schemas (e.g.,INFORMATION_SCHEMA.TABLESin MySQL).
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:1-flag.txt

### 2. SQLi - Data Exfiltration from a Specific Table

With knowledge of the database structure, your goal is to extract sensitive data from a specific table.The target for this exercise is a flag ⛳️ stored within one of the tables you previously identified.





```bash
Helpful Instructions:
1. Based on your findings from Task 2, choose a table that likely contains the flag.
2. Develop payloads that will allow you to retrieve the contents of the target table.
   - This will involve constructing queries that utilizeUNION SELECTstatements or other techniques suitable for data exfiltration.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:2-flag.txt

### 3. SQLi - Time-Based Blind Injection

In the realm of cybersecurity, not all vulnerabilities are visible or apparent.
Blind SQL injection is a prime example of such hidden vulnerabilities.In this task, you are challenged to detect and exploit a blind SQL injection vulnerability where the only indication of success is a delayed response from the server.Your goal is to craft apayloadthat causes the server to return aflag⛳️  if the query execution takes longer than5seconds.





```bash
Helpful Instructions:
1. Understanding Time-based SQL Injection
   -  Familiarize yourself with how SQL databases can be manipulated to delay responses using specific functions or commands.
2. Your payload should incorporate a command that causes the server to wait or sleep for a specified duration (more than 5 seconds) before responding.
   -  The exact function or command will depend on the database in use (e.g.,SLEEP()for MySQL,pg_sleep()for PostgreSQL,WAITFOR DELAYfor SQL Server).
3. Observing Responses:
   -  Use tools like Burp Suite to send your payloads and accurately measure the response times. This will help you fine-tune your payload to achieve the desired delay.
4. Iterative Testing:
   - You may not get it right on the first try. Use an iterative approach, adjusting your payload based on response times, to zero in on a successful exploitation technique.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:3-flag.txt

### 4. SQLi - Second-Order Blind Injection

Second-order SQL injection requires a nuanced approach, as the payload you inject at one point is executed at another, often without direct feedback.This task involves submitting a payload through a registration form that seems benign until it is processed during login, revealing a flag based on a jinja error whereFLAGis an accessible variable.Your goal is to find theflag⛳️.





* Target URL (Initial Input):Endpoint:http://web0x01.hbtn/api/a3/sql_injection/second_order/registerMethod:POSTContent-Type:JSONBody:Example{"username": "yosri", "name": "Yosri", "password": "password123"}
* Endpoint:http://web0x01.hbtn/api/a3/sql_injection/second_order/register
* Method:POST
* Content-Type:JSON
* Body:Example{"username": "yosri", "name": "Yosri", "password": "password123"}
* Target URL (Trigger):Endpoint:http://web0x01.hbtn/api/a3/sql_injection/second_order/loginMethod:POSTContent-Type:JSONBody:Example{"username": "yosri", "password": "password123"}
* Endpoint:http://web0x01.hbtn/api/a3/sql_injection/second_order/login
* Method:POST
* Content-Type:JSON
* Body:Example{"username": "yosri", "password": "password123"}

```bash
{"username": "yosri", "name": "Yosri", "password": "password123"}
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:4-flag.txt

### 5. NoSQLi - Discovering Injection Vulnerabilities

Unlike SQL databases, NoSQL databases handle queries differently, often using JSON-like structures for queries.Your mission is to detect anendpointwithin the application that is susceptible to NoSQL injection butNOT Harmful.For that you should:





* Navigate to:http://web0x01.hbtn/a3/nosql_injection. (dont forget to edit your /etc/hosts)
* Search for the vulnerable paramters.
* $ echo "/api/some_endpoint/here" > 5-vuln.txt

```bash
$ echo "/api/some_endpoint/here" > 5-vuln.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:5-vuln.txt

### 6. NoSQLi - Bypassing Login via injection

The application you are targeting uses a NoSQL database for user authentication.Due to improper input handling, it’s possible to manipulate the login query through injection.By crafting a specific payload, you can alter the query logic to bypass authentication checks and log in as any user, including administrative accounts.

Your challenge is to find theflag⛳️ by exploiting a login form.





* Target URL:http://web0x01.hbtn/a3/nosql_injection

```bash
Helpful Instructions:
1. Experiment with injecting JSON-like syntax into the username and password fields.
2. Focus on operators that can modify the logic of the database query, such as$ne(not equal).
3. Consider using the$neoperator with a value that is always true, such as{"$ne": null}or{"$ne": ""}, to manipulate query conditions.
4. Try to target specific users by injecting payloads into the username field. Use common usernames likeadminto attempt gaining administrative access.
5. Observe how the application responds to different payloads. Successful bypass might not always be obvious and could require interpreting subtle changes in response behavior or content.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:6-flag.txt

### 7. NoSQLi - Enumerating for Profit

After mastering the technique of bypassing the login mechanism through NoSQL injection, your ultimate challenge within this project emerges.This task requires you to leverage yourNoSQL injectionskills further to enumerate login attempts.Your mission: identify auser profilewith sufficient balance and engage in cryptocurrency exchange activities on the platform to accumulate at least 1 HBTNc coin.Success in this endeavor will not only demonstrate mastery of NoSQL injection techniques but also highlight your ability to apply these skills strategically for financial gain within the simulation.

FLAG will only appear after claiming at least 1HBTNc

* Target URL:http://web0x01.hbtn/a3/nosql_injection

```bash
Useful instructions:
1. Return to the login endpoint where you previously achieved bypass. This time, focus on enumerating different user profiles to find one with a notable account balance.
2. Employ NoSQL injection techniques in the login process to iterate through user accounts. Take note of the structure and feedback from successful bypasses to refine your enumeration process.
3. Upon identifying an account with enough balance, navigate to the cryptocurrency exchange feature within the application. Engage in transactions that will allow you to acquire at least 1 HBTNc coin.
4. Your transactions must be carefully calculated to ensure that the account balance is exchanged for the exact or higher amount of HBTNc coins required.
5. Monitor the application's feedback and responses closely during the exchange process. The acquisition of 1 or more HBTNc coins will trigger the appearance of a `Flag`, signifying your triumph in this comprehensive NoSQL injection challenge.

Remember:
- Approach this task with the mindset of a security professional, understanding that the techniques demonstrated are for educational purposes within this simulated environment.
- The skills applied in this task should be used responsibly and ethically in real-world scenarios, adhering to legal and professional standards.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x03_sql_nosql_injection
* File:7-flag.txt

### Tasks list

* Mandatory
* Advanced


