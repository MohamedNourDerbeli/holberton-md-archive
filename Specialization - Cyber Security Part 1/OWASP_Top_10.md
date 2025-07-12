# Project: OWASP Top 10

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/D83JMW6UVK83JGL2.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [OWASP Top 10:2021](/rltoken/YBs1n6-O5vlboawG0M9kDA)
* [Explaining the OWASP Top 10](/rltoken/diRIyp4IaMy2f__EqUmoUQ)
* [Understanding the OWASP Top 10 with Examples](/rltoken/gxBvuFbfIWil9UUsJe3zGw)
* [OWASP Top 10: The Big Picture](/rltoken/8486PgR5EcJ_rFwhI3He4Q)
* [OWASP Top 10 Risks – Mitigation Strategies](/rltoken/P7VlUTsQRxmZpcN1yTQzxA)
* [How to Choose a Password](/rltoken/CcZHn-GBOIhhbekQ4jcfdg)

#### References:

* [OWASP Official Website](/rltoken/x6EGF70zEXMrwvPTy59APw)
* [OWASP Top 10 - Wikipedia](/rltoken/UVg9Zt8rQTnX-9fITqNM5g)
* [OWASP Top 10 Proactive Controls](/rltoken/faYCimMO6ZYMW78tmt8dfw)
* [OWASP Cheat Sheet Series](/rltoken/YrcNNIzfSg-PWG1JBYsMEg)
* [OWASP ZAP - Web Application Penetration Testing Tool](/rltoken/wUUVyExHSduL_zeM6ahQkw)
* [OWASP Amass - Subdomain Enumeration Tool](/rltoken/4CfDC-LEd3CqbyEnlKEnbg)
* [OWASP Juice Shop - Vulnerable Web Application](/rltoken/JmNeKjsOm0lW6nnPB5hjew)
* [OWASP Dependency-Check - Software Composition Analysis Tool](/rltoken/UVWEvRsWhz6Enhjp2K9lEA)


## Learning Objectives

* What is theOWASP Top 10?
* Why is injection dangerous?
* How doesXSSaffect web applications?
* What is the risk ofbroken authentication?
* Can you explain sensitive data exposure?
* Describe a security misconfiguration.
* What is XML External Entity (XXE)?
* How dobroken access controlsimpact security?
* What are common web application security flaws?
* How to preventInsecure Deserialization?
* What is the use of security logging and monitoring?
* Explain the risks of using components with known vulnerabilities.
* How can usingAPIsincrease security risks?


## Requirements

### General

* All your files will be run onKali Linux 2023.2
* Allowed editors:vi,vim,emacs
* You must substitute the IP range for$1.
* The first line of all your files should be exactly#!/bin/bash.
* All your files should end with a new line.
* You are not allowed to use backticks,&&,||or;.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl


## Tasks

### 0. (A1:2021) - Broken Access Control



Creating your ownsession IDs?, Make sure they’re as unpredictable as a plot twist in a mystery novel.
If they’re too simple, it’s like leaving the keys in the ignition for hackers.
Complexity and randomness are your locks and alarms.

For this task, tamper thehijack_sessioncookie to sneak into someone else’s session.

hints: you get new cookie each time you visit the target url using fresh session, just figure the pattren..

* Target machine:Cyber - WebSec 0x01
* Target Url:http://web0x01.hbtn/a1/hijack_session

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x01_owasp_top_10
* File:0-flag.txt

### 1. (A2:2021) - Cryptographic Failures - Scripting



Create aBash scriptthat decodeXOR WebSphere. Your Script should:

* Accept the Hash args:$1.
* Match the following output.

```bash
┌──(yosri㉿hbtn-lab)-[~/…/web_application_security/0x1_owasp_top_10]
└─$ ./1-xor_decoder.sh {xor}KzosKw==
test
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x01_owasp_top_10
* File:1-xor_decoder.sh

### 2. (A2:2021) - Cryptographic Failures - Catch The Flag

For this task:

Your goal is finding out the the login credentials in order to retreive the flag on sign in.

Where to start ?(Hints)

hints:

* Turn back to the target machinecyber_websec_0x01,
* Heads out to: A2 - Cryptographic Failures -> Encoding Failure.

* Login Page:http://[MACHINE-IP]/a2/crypto_encoding_failure/

* Profile Page:/a2/crypto_encoding_failure/profile

* Think about the headers of all Fetch/XHR made requests.
* Use the previous task to decrypt the password.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x01_owasp_top_10
* File:2-flag.txt

### 3. (A3:2021) - Injection [Stored XSS] - part 1/3

Your first task is to identify three specific profiles within our web application that you need to follow. These profiles are crucial for the next steps of this exercise.

Instructions:

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x01_owasp_top_10
* File:3-flag.txt

### 4. (A3:2021) - Injection [Stored XSS] - part 2/3

Identify which input field in the profile edit page is vulnerable to Cross-Site Scripting (XSS).

Instructions:

```bash
$ echo "name" > 4-vuln.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x01_owasp_top_10
* File:4-vuln.txt

### Tasks list

* Mandatory
* Advanced


