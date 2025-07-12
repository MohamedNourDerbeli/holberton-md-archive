# Project: Nmap Post Port Scan & Scripting

![Project Image](https://i.imgflip.com/6sv4ow.jpg)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Nmap documentation](/rltoken/yCbXPQiU-iWB8uwCY8nSlw)
* [Nmap Scripting Engine](/rltoken/N_90tiZJDY0qp01rKsDTtg)
* [Tips Nmap Script Engine](/rltoken/PSb6DLWfrIF9AWLaYjccaw)
* [Advanced Port Scanning techniques](/rltoken/JZg3R_ERTATp34tWaatiEg)
* [Nmap Scripts (NSE): The Key To Enhance Your Network Scans](/rltoken/LsWnjgWmSAmWT097-5zntQ)
* [Nmap Scripting](/rltoken/YMJRDznV-DiLmMIMWlGQnQ)
* [List of NMAP Scripts](/rltoken/YaEaw5E0Afoo3B1PPBiduQ)

#### References:

* [Nmap Scripting Engine](/rltoken/cKcd3lN0psEFY7ant5MpmA)


## Learning Objectives

* What is the Nmap Scripting Engine (NSE) and why is it important?
* How does the Nmap Scripting Engine work?
* What are the different script categories in NSE?
* How are scripts organized and executed in NSE?
* What command-line arguments are used for running NSE scripts?
* What can you do with these Nmap scripts?
* How do you write documentation for NSE scripts using NSEDoc?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly two lines long ($ wc -l fileshould print 2)
* You must substitute the IP range for$1.
* All your files should end with a new line (Why?)
* The first line of all your files should be exactly#!/bin/bash.
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* You are not allowed to use backticks,&&,||or;.
* All your scripts should be 2 lines long ($ wc -l file should print = 2).
* You are not Allowed to use Neither echo
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable
* Ensure that$1is used without quotes in your script to prevent unintended argument type alterations.


## Tasks

### 0. Skipping NSE scripting for Nmap is like bringing a spoon to a hacking knife fight!



You might be familiar with the robust open-source network scanning tool Nmap, but have you heard about the even more potent Nmap Scripting Engine?

The Nmap Scripting EngineNSEis an advanced feature of the open-source network scanning toolNmap. It automates network scanning and exploitation tasks, saving time and enhancing capabilities through scripting.

We have observed that many security professionals lack the ability to writeNSEscripts forNmap. This skill is relatively easy to learn, and by neglecting it, you are leaving a lot of value on the table. Let’s dive in and learn everything we need to become experts in the Nmap Scripting Engine today!

Write a bash script that runs the default NSE scripts usingdefaultto perform various analyses and gather necessary information related to the target.

Depending on the scanned network, the output could change.

* Your script should accept a host as an arguments$1

```bash
┌──(maroua)-[~/0x07_nmap_post_port_scan_scripting]
└─🏴 sudo ./0-nmap_default.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-24 13:00 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.19s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open  http
|_http-title: Go ahead and ScanMe!
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 16.19 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:0-nmap_default.sh

### 1. Using Nmap's vulners script: like finding Easter eggs, but with cyber threats!

Nmap’s vulners script is a powerful tool for identifying vulnerabilities on a target host. By leveraging a comprehensive database of known vulnerabilities, this script scans specified ports and services, providing detailed information about potential security issues.

Using thevulnersscript as part of regular security assessments can help organizations maintain robust defenses against emerging threats and ensure their systems remain secure.

Write a bash script that accepts a host as an argument$1.Run thevulnersscript on the specified host, targeting ports80followed by443.

Depending on the scanned network, the output could change.

```bash
┌──(maroua)-[~/0x07_nmap_post_port_scan_scripting]
└─🏴 sudo ./1-nmap_vulners.sh scanme.nmap.org
[sudo] password for maroua:
marouaa@campusna:~/holbertonschool-cyber_security/network_security/0x07_nmap_post_port_scan_scripting$ ./1-nmap_vulners.sh scanme.nmap.org
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-21 15:51 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.28s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

PORT    STATE  SERVICE
80/tcp  open   http
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 1.24 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:1-nmap_vulners.sh

### 2. Scan web apps like a pro – vulnerability sleuth mode activated!



The Nmap Scripting EngineNSEis a powerful feature of the Nmap network scanning tool, designed to automate various tasks, including vulnerability detection.NSEscripts can identify weaknesses in network services, web applications, and configurations by leveraging a vast library of community-contributed scripts.

In this task, you’ll elevate your Nmap skills by using an NSE script to detect vulnerabilities in web applications.

Writea bash scriptthat performs the following tasks:

Depending on the scanned network, the output could change.



* Your script should accepta hostas an arguments$1.
* Use thehttp-vuln-cve2017-5638 NSEscript to check for the Apache Struts 2 vulnerability.
* Save the output tovuln_scan_results.txtfor later analysis.

```bash
┌──(maroua)-[~/0x07nmappostportscan_scripting]
└─🏴 sudo ./2-vuln_scan.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-24 13:50 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.19s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  EliteNmap done: 1 IP address (1 host up) scanned in 12.19 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:2-vuln_scan.sh

### 3. Time to make hackers cry – let's scan smart and secure hard!



In this task, you’ll harness the power of the Nmap Scripting EngineNSEto perform a comprehensive security analysis of a target network

Writea bash scriptthat performs the following tasks:

Depending on the scanned network, the output could change.



* Your script should accepta hostas an arguments$1.
* Use multiple NSE scriptssequentiallyto perform a comprehensive security analysis, including:http-vuln-cve2017-5638for the Apache Struts 2 vulnerability.ssl-enum-ciphersto enumerate supported SSL/TLS ciphers.ftp-anonto check for anonymous FTP login.
* http-vuln-cve2017-5638for the Apache Struts 2 vulnerability.
* ssl-enum-ciphersto enumerate supported SSL/TLS ciphers.
* ftp-anonto check for anonymous FTP login.
* Save the output tocomprehensive_scan_results.txtfor later analysis.

```bash
┌──(maroua)-[~/0x07nmappostportscan_scripting]
└─🏴 sudo ./3-comprehensive_scan.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-20 10:31 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.45s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2fPORT      STATE  SERVICE
21/tcp    closed ftp
22/tcp    open   ssh
80/tcp    open   http
443/tcp   closed https
9929/tcp  open   nping-echo
31337/tcp open   EliteNmap done: 1 IP address (1 host up) scanned in 6.04 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:3-comprehensive_scan.sh

### 4. NSE: Making hackers rethink their career choices, one vulnerability at a time!

In this task, you’ll leverage the Nmap Scripting Engine (NSE) to automate the exploitation of vulnerabilities discovered during a network scan.

Writea bash scriptthat performs the following tasks:

Depending on the scanned network, the output could change.



* Your script should accepta hostas an arguments$1
* Use NSE scripts *sequentially *to detect vulnerabilities across various services:Web Application Vulnerabilities: Your script should identify common vulnerabilities in web applications.Database Vulnerabilities: Your script should detect vulnerabilities inMySQL.Service Exploitation: Your script should check for exploitable conditions inFTPandSMTP.
* Web Application Vulnerabilities: Your script should identify common vulnerabilities in web applications.
* Database Vulnerabilities: Your script should detect vulnerabilities inMySQL.
* Service Exploitation: Your script should check for exploitable conditions inFTPandSMTP.
* Save the output tovulnerability_scan_results.txtfor later analysis.Note: Use*wildcard with NSE scripts for broader vulnerability coverage. exmpleftp-vuln*

```bash
┌──(maroua)-[~/0x07nmappostportscanscripting]
└─🏴 sudo ./4-vulnerability_scan.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-20 14:15 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.23s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http       Apache httpd 2.4.7 ((Ubuntu))
|http-server-header: Apache/2.4.7 (Ubuntu)
9929/tcp  open  nping-echo Nping echo
31337/tcp open  tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernelService detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.67 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:4-vulnerability_scan.sh

### 5. NSE scripts in Nmap: where automation meets network domination!



When utilizing Nmap Scripting Engine (NSE), we harness a powerful capability within Nmap to automate and extend its network scanning functionalities.NSE scripts enable us to perform a wide range of tasks beyond basic port scanning, including service version detection, vulnerability detection, enumeration of specific protocols likeSMBandDNS, and even complex tasks like brute-force attacks and web application scanning.

Writea bash scriptthat performs comprehensive network reconnaissance using Nmap with specific NSE scripts:

Depending on the scanned network, the output could change.



* Your script should accepta hostas an arguments$1
* Your script should probe open ports to determine service/version information.
* Your script should enable OS detection, version detection, script scanning, and traceroute.
* Your script shouldsequentiallyexecute multiple NSE scripts to detect vulnerabilities across various services:Retrieve service banners from open ports.Enumerate supportedSSL/TLSciphers..Run default scriptsdefaultdefined by Nmap for basic enumeration tasks.EnumerateSMB(Server Message Block) domains.
* Retrieve service banners from open ports.
* Enumerate supportedSSL/TLSciphers..
* Run default scriptsdefaultdefined by Nmap for basic enumeration tasks.
* EnumerateSMB(Server Message Block) domains.
* Save the output toservice_enumeration_results.txtfor later analysis.

```bash
┌──(maroua)-[~/0x07nmappostportscanscripting]
└─🏴 sudo ./5-service_enumeration.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-21 11:23 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.35s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
|banner: SSH-2.0-OpenSSH6.6.1p1 Ubuntu-2ubuntu2.13
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open  http       Apache httpd 2.4.7 ((Ubuntu))
|http-server-header: Apache/2.4.7 (Ubuntu)
|http-title: Go ahead and ScanMe!
9929/tcp  open  nping-echo Nping echo
| banner: \x01\x01\x00\x18t@\xD9\x9BfuY?\x00\x00\x00\x00t\xDF\x0A.\xD1>\x
|AD\x82\x03M\xD28\x8D\x8C\xF0\xB3t\x1F'x4Y\x81X5\xD9\x90\x18\xA3\x16...
31337/tcp open  tcpwrapped
Device type: general purpose
Running (JUST GUESSING): Linux 3.X|4.X (85%)
OS CPE: cpe:/o:linux:linuxkernel:3.8 cpe:/o:linux:linuxkernel:4.4
Aggressive OS guesses: Linux 3.8 (85%), Linux 4.4 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 19 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linuxkernelTRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   1.10 ms   _gateway (192.168.1.1)
2   98.52 ms  192.168.60.1
3   98.53 ms  196.203.189.161
4   98.50 ms  193.95.96.6
5   98.54 ms  193.95.0.150
6   ...
7   99.31 ms  195.72.67.33
8   200.80 ms ae24.cr4-nyc6.ip4.gtt.net (213.200.121.6)
9   200.66 ms ip4.gtt.net (98.124.184.66)
10  200.34 ms ae2.r02.lga01.icn.netarch.akamai.com (23.203.156.40)
11  200.38 ms ae13.r01.ewr01.icn.netarch.akamai.com (23.32.63.214)
12  200.39 ms ae19.r01.ord01.icn.netarch.akamai.com (23.193.113.37)
13  303.62 ms ae16.r01.sjc01.icn.netarch.akamai.com (23.32.62.79)
14  303.60 ms ae1.r11.sjc01.ien.netarch.akamai.com (23.207.232.35)
15  303.64 ms a23-203-158-51.deploy.static.akamaitechnologies.com (23.203.158.51)
16  ... 18
19  303.74 ms scanme.nmap.org (45.33.32.156)OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1171.07 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x07_nmap_post_port_scan_scripting
* File:5-service_enumeration.sh

### Tasks list

* Mandatory
* Advanced


