# Project: Web Fundamentals

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [How the Web works ?](/rltoken/hl5lYGA63aQsW8eB6m0bBQ)
* [The Fundamentals of Web Development](/rltoken/6OLoQgFZNTwz9e5qIaZvKw)
* [Web 1.0 Vs. Web 2.0 Vs. Web 3.0](/rltoken/8FT0jFP6RBVXhbbcgBiYTg)
* [What are Progressive Web Apps ?](/rltoken/L0uho8TX-shQ6Qx2_f-XSw)
* [Stateful vs Stateless - Web App Design](/rltoken/dcQ8i_tcuHogZqgDQx2yxA)
* [Structured vs. Unstructured Data](/rltoken/k5Gf_sWWeJLMOkCEo1NXVA)
* [Web Application Security Explained](/rltoken/XWIqe4Cu9UpnNcU8rIT97w)
* [Web Application Security Testing](/rltoken/2qe7lybxaRdAheNCU4qgfw)

#### References:

* [Stateful vs Stateless](/rltoken/5ehapwBBmhdlZk9D3D27qQ)
* [How Does the Frontend Communicate with the Backend ?](/rltoken/xhdqZVTSLITndZA8V48Wdw)
* [OWASP Top Ten](/rltoken/_aAdm80YeOcdRH52w6ulGw)
* [Cross-Origin Resource Sharing (CORS)](/rltoken/HkXZmItWns0dijePPeibNA)
* [Bug bounty program](/rltoken/vEiLOnxylbUQW7LQu2NIlw)
* [TOP Bug Bounty Programs](/rltoken/NnWbxiK6wkc0Sbea7z_-gg)


## Learning Objectives

* How theWebworks ?
* Examples ofWeb Applications
* Web 1.0vsWeb 2.0vsWeb 3.0
* PWA- Progressive Web Applications
* How does theFront-Endcommunicate with theBack-End?
* StatefulvsStateless: What’s the difference?
* StructuredvsUnstructured, What’s the difference ?
* Web ApplicationSecurity Risks
* BugBountyPrograms


## Requirements

### General

* All your scripts will be tested onKali Linux 2023.3
* All your scripts should be exactly two lines long ($ wc -l fileshould print 2)
* You must substitute the IP range for$1.
* All your files should end with a new line (Why?)
* The first line of all your files should be exactly#!/bin/bash.
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable


## Tasks

### 0. Welcome

Welcome toWeb Application SecurityModule \o/

Brief discussion:

Through this project we will guide you through exploiting 4 types of vulnerabilities which could occur within a web app:‘)

You should have:

Warming Up:

* Pre-Installed Kali Linux (or Use aSandbox)
* Access to our Network (Through OpenVPN orSandbox)
* Web Browser (We Recommand FireFox)
* Terminal (Forcurlandsqlmap)

* Get aTarget Machine
* Endpoint :http://web0x00.hbtn/login
* Append to yourHostsfile the domainweb0x00.hbtnpointing to the target machine ip.
* Test your connectivityVia terminal:┌──(yosri㉿HBTN-LAB)-[~/0x00webfundamentals]
└─$ curl http://web0x00.hbtn
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/home">/home</a>. If not, click the link.Via Browser:

```bash
+ Collegue:
-   Hear this, My Boss Just asked me forCustomer SupportDashboard.
+ Me:
-   And ? For a Dashboard with Supports UI, Customers UI and Admin
    Portal will takes you at least 4 weeks.
+ Collegue:
-   I challenged him to do it within 3 days for reward;)+ Me:
-   Are you serious:O?
+ Collegue:
-   Yeah, I gotPaidChatGPT 4 by my side:'D...
3 Days later.
...
+ Collegue:
-   I already finish it, Take a look my friendhttp://web0x00.hbtn!
+ Me:
-   Am I allowed to pentest it:p?
+ Collegue:
-   Feel free, It'sHack Proof. I trust AI's Codes,\o/
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:README.md

### 1. Can We Trust Our Hosts?

Write abash scriptthat exploit host header injection usingcurl.

* Initial Endpoint :http://web0x00.hbtn/reset_password
* Your script should accept theNEW HOSTas ARG 1 ("$1").
* Your script should accept theTARGET URLas ARG 2 ("$2").
* Your script should accept theFORM DATAas ARG 3 ("$3").

```bash
┌──(yosri㉿hbtn-lab)-[~/…/web_application_security/0x00_web_fundamentals]
└─$ ./1-host_header_injection.sh new_host http://web0x00.hbtn/reset_password email=test@test.hbtn
...
                                <div class="alert_box">
                                                <span>Email provided not found</span>
                                </div>
                                <button type="submit">Reset</button>
                                <a href="http://new_host/login">Try to sign in again ?</a>
...
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:1-host_header_injection.sh

### 2. Catch The FLAG #1

Hints

Find yourIPin our network



Here is how to connect:

*Once connected, start a Python HTTP server on port 80 to listen for the bot’s click on the reset link.

* Check theSource-Codefor known Customers emails
* ABotwill click the reset link delivered to the customer.
* The Flag will be displayed on the<header>section after you sign in as aCustomer.

* Target Machine
* Initial Endpoint :http://web0x00.hbtn/login

```bash
$ ip addr show tun0
16: tun0:mtu 1500 qdisc fqcodel state UNKNOWN group default qlen 500
    link/none 
    inet6.190.192.2/18 scope global tun0
       validlft forever preferredlft forever
    inet6 fe80::c749:5490:295:a827/64 scope link stable-privacy proto kernelll 
       validlft forever preferredlft forever
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:2-flag.txt

### 3. Stealing Cookies from Managers is delicious !

Create a JavaScript payload that exploits Cross-Site Scripting (XSS) vulnerabilities within a ticketing system.

* Craft your payload using JavaScript.It must be encapsulated within<script>tags.Example format for your payload file:$ cat 3-xss_payload.txt
<script>// Your JavaScript code goes here</script>
* It must be encapsulated within<script>tags.
* Example format for your payload file:$ cat 3-xss_payload.txt
<script>// Your JavaScript code goes here</script>
* Your code should be as short as possible.
* You are not allowed to declare any variables within your payload.
* Your payload must utilize thefetchfunction to send the cookies of the ticket system’s visitor.
* The cookies should be included in the request’s pathname and sent to your designated web server.Example: http://[your_ip]/.session=Tm90aGluZyBIZXJl]
* Example: http://[your_ip]/.session=Tm90aGluZyBIZXJl]
* Target  App
* Initial Endpoint :http://web0x00.hbtn/login

```bash
$ cat 3-xss_payload.txt
<script>// Your JavaScript code goes here</script>
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:3-xss_payload.txt

### 4. Catch The FLAG #2

Hint

To Change your cookies, steps are simple:

* ABotwill load the ticket as a Support and response to it.
* Never forget that theXSS Payloadwill load on your side too !
* The Flag will be displayed on the<header>section after you sign in as aSupport.

* Target Machine
* Initial Endpoint :http://web0x00.hbtn/home

```bash
ViaFireFox:-> HitF12(open dev tools)
-> Got to Storage (top menu)
-> Select Cookies
-> Change Value
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:4-flag.txt

### 5. Can we trust our Managers ?

Here we are now, logged as aSupportmember. Now we can check tickets and reply to them!What’s more interesting ?Yes!theTicket IDwhich smell likeSQLi\o/

Dev Tools -> Network, is the best path to go



* Write a text file containing theHTTP Requestto exploit the potential SQL Injection in the ‘Ticket ID’ parameter.

```bash
┌──(yosri㉿hbtn-lab)-[~/…/webapplicationsecurity/0x00webfundamentals]
└─$ sqlmap -r 5-ticket.txt
        ___H___[']__ ___ ___  {1.7.10#stable}
|--|.["]|.'|.|
||["]||_|,|__|
      ||V...       |_|   https://sqlmap.org
[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
[*] starting @ 09:31:09 /2023-11-13/
[09:31:09] [INFO] parsing HTTP request from '5-ticket.txt'
[09:31:10] [INFO] testing connection to the target URL
[09:31:10] [INFO] testing if the target URL content is stable
[09:31:10] [INFO] target URL content is stable
[09:31:10] [INFO] testing if GET parameter 'id' is dynamic
got a 302 redirect to'http://web0x00.hbtn/support'. Do you want to follow? [Y/n]
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:5-ticket.txt

### 6. Catch The FLAG #3

Hints

* You will need the file5-ticket.txtfrom the previous task.
* For the admin credentials, they could be atAdminsTable.SQLmapcould--dumpit for you.
* You could find the Admin login page athttp://web0x00.hbtn/admin.
* The Flag will be displayed on the<header>section after you sign in as anAdmin.
* Target Machine
* Initial Endpoint :http://web0x00.hbtn/admin

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:6-flag.txt

### 7. Why would an Admin have such a function ?

Welcome toAdminPanel!Things are getting dangerous here..As we notice, there is a ping check function, which the admin use to up devices.

Write a payload that exploits poor input validation to achieve Remote Code Execution (RCE):

Your output should match this screenshot



* Ensure there are no unnecessary spaces.
* Ensure your payload doesexactlythe following:Download thencstatic binary usingwgetfromhttps://github.com/yunchih/static-binaries/raw/master/nc.Grant execute permission tonc.Display thencversion using the -V option.
* Download thencstatic binary usingwgetfromhttps://github.com/yunchih/static-binaries/raw/master/nc.
* Grant execute permission tonc.
* Display thencversion using the -V option.

```bash

```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:7-rce_payload.txt

### 8. Catch The FLAG #4

Hints

* Start a listner for reverse shell.
* ./ncto use netcat from the previous task.
* The Flag could be found atroot‘shome directory

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x00_web_fundamentals
* File:8-flag.txt

### Tasks list

* Mandatory
* Advanced


