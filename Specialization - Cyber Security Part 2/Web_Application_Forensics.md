# Project: Web Application Forensics

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

Files Used in This Project

## Resources

#### Read or watch:

* [What is computer forensics?](/rltoken/cvvRzgtM2zOoo_bX-9voPg)
* [What Does a Cyber Forensic Investigation Do and How Much Does It Cost](/rltoken/s24APUzl-UePQO6BVYhHMw)
* [Types of Forensics](/rltoken/OVebRJ1AU0xACz4VmeW83g)
* [DFIR Reports](/rltoken/jWmITf72gC7p1HIT9iGuIg)
* [Linux IPtables](/rltoken/BH078cl_z6_dXzjcNWJWDg)
* [Linux firewalls](/rltoken/QacznS3u1YhTTE3CJljrCQ)
* [What is the difference between firewalld and iptables?](/rltoken/N5cLR08fQNKkSc12Pxf0Dg)


## Learning Objectives

* What isDigital Forensics?
* What are the core concepts of Web Application Forensics?
* How to analyze Web Application Logs?
* How can Log Files andAccess Logs be used to trace the origin of an attack?
* How to use tools like Wireshark and Burp Suite in a web application forensic investigation?
* What are the Legal Frameworks and best practices for conducting forensic investigations?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your files should end with a new line (Why?)
* The first line of all your files should be exactly#!/bin/bash.
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* You are not allowed to use backticks,&&,||or;.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable
* Ensure that$1is used without quotes in your script to prevent unintended argument type alterations.


## Tasks

### 0. Attacker Service



The objective of this project is to develop scripts that analyze logs from web application attacks. These logs contain crucial information that can help us understand the nature of the attacks, identify the attackers, and uncover the vulnerabilities exploited. By scrutinizing these logs, we can gather actionable intelligence to strengthen our web application’s security posture.

Which service did the attackers use to gain access to the system?  Write a script that scan the logs and help you  figure what service was used

```bash
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./0-service.sh 
34806 pam_unix(sshd:auth):
  20339 Failed
  14478 Invalid
    214 Address
    200 pam_unix(sshd:session):
    169 reverse
    118 Accepted
     44 Did
     20 error:
     20 Server
     10 subsystem
      9 syslogin_perform_logout:
      7 Received
      5 PAM
      5 Jax
      2 Bad
      1 new
      1 changed
      1 change
      1 Kayn
      1 Exiting
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:0-service.sh

### 1. Operation System

What is the operating system version of the targeted system

File Concerned isdmseg

```bash
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./1-operating.sh 
[    0.000000] Linux version 2.6.24-26-server (buildd@crested) (gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)) #1 SMP Tue Dec 1 18:26:43 UTC 2009 (Ubuntu 2.6.24-26.64-server)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:1-operating.sh

### 2. Account Compromised

What is the name of the compromised account

```bash
* Tips: 
* Analyse last 1000 line of logs 
* Check if the user had multiple unsuccessful break in and then success  this will be mostly compromised account 
* Check for Suspected Activity
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:2-accounts.sh

### 3. Sum Attack

Consider each unique IP address as representing a different attacker. How many distinct attackers gained access to the system

```bash
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./3-ips.sh 
18
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:3-ips.sh

### 4. Mitigation Firewalls

How many rules have been added to the firewall

* Check the auth.log file for entries related to adding firewall rules.

```bash
┌──(imen㉿hbtn-lab)-[…/web_application_security/0x0c_web_application_foresics]
└─$ ./4-firewall.sh
6
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:4-firewall.sh

### 5. Users Accounts

Multiple accounts were created on the target system. What are the users?

Example:Aphelios,Debian-exim,Fido....





```bash
┌──(imen㉿hbtn-lab)-[…/webapplicationsecurity/0x0cwebapplication_foresics]
└─$ ./5-users.sh
Aphelios,Debian-exim,Fido,Jax,Nidalee,Senna,dhg,messagebus,mysql,packet,sshd
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x0c_web_application_foresics
* File:5-users.sh

### 6. Future Mitigations

In cybersecurity, understanding and mitigating the risks associated with web application vulnerabilities is crucial. This report is the first entry in a comprehensive series on web application forensics, in which we explore the essential principles and strategies that can protect technology-enabled organizations against cyberthreats.

Instructions:

**Repo Info:**
### Tasks list

* Mandatory
* Advanced


