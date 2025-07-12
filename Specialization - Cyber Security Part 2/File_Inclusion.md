# Project: File Inclusion

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch

* [Local File Inclusion (LFI) – OWASP](/rltoken/Jo-oWJ4OTJ558e9KRpRJfg)
* [Remote File Inclusion (RFI) – OWASP](/rltoken/D5ZZtnV2YpXGQCkKcZqelg)
* [LFI to RCE: Basic Exploitation Guide](/rltoken/wghsBdA0992jpWUBy5_yOQ)
* [File Inclusion Types, Examples, and Prevention](/rltoken/M3vOpIpqErPRLUtohINb0Q)
* [File Inclusion Path Traversal](/rltoken/Npf1OZ_k2aGnVq_N4macyw)

#### References

* [PHP Manual on include() and require()](/rltoken/6MOpxcDYuz4vJLngsYfoVQ)
* [File Inclusion Cheat Sheet](/rltoken/zlrMkYHW0yKUrjxBaUFHxg)
* [File Inclusion Payload Github](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_linux.txt)


## Learning Objectives

* What is LFI?
* What is RFI?
* How to prevent FI attacks?
* What is../../used for in FI?
* How can LFI lead to RCE?
* What are the mechanisms through which file inclusion vulnerabilities can be exploited?
* What is the potential impact of successful file inclusion attacks on a system?
* What techniques can be used to detect file inclusion vulnerabilities in web applications?
* How can effective mitigation strategies be implemented to safeguard against file inclusion vulnerabilities?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetCyber - WebSec 0x07.


## Tasks

### 0. File Hub

Your initial objective entails identifying the vulnerable endpoint and securing the flag located at /etc/0-flag.txt.

* Target Machine:Cyber - WebSec 0x07
* Main Endpoint:http://web0x07.hbtn/task0/list_file

```bash
Useful instructions:
1. Try to upload a file.
2. Check page source for evey endpoint.
3. Investigate links and how they are processed, and what parameters are accepted.
4. Experiment with altering the path and file names and check the result.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x07_file_inclusion
* File:0-flag.txt

### 1. Another filter won't help

Your Mission

A critical file named 1-flag.txt is hidden somewhere within the system. You’ve discovered a vulnerable endpoint that should let you retrieve it, but the path to the file might not be exactly what you expect. A developer note hints at a small typo or oversight in the path something about extra slashes or a hidden directory that could help you sneak past the filter `..//.

PS : a filter has been implemented to prevent unconventional paths.

Hints & Instructions

Useful instructions:

* Target Machine:Cyber - WebSec 0x07
* Main Endpoint:http://web0x07.hbtn/task1/list_file

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x07_file_inclusion
* File:1-flag.txt

### 2. Not even this can be bypassed

A critical flag is hidden deep within /etc/2-flag.txt. The system guarding it has implemented multiple layers of filtering and validation, making traditional techniques ineffective. However, every defense has its blind spot—your mission is deconstructing it.

Your task is to investigate, exploit, and secure the endpoint.

Challenge yourself to bypass it while respecting security boundaries.

* Target Machine:Cyber - WebSec 0x07
* Main Endpoint:http://web0x07.hbtn/task2/list_file

```bash
Useful instructions:
1. Test Boundaries: Experiment with different encoding and payload techniques to understand how inputs are processed.
2.  Think Outside the Box: Consider less conventional methods of bypassing security filters.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x07_file_inclusion
* File:2-flag.txt

### 3. The Jinja template

Your objective as usual is identifying the vulnerable endpoint and securing the flag located at /etc/3-flag.txt.

Hint : all the rapport are a jinja template

* Target Machine:Cyber - WebSec 0x07
* Main Endpoint:http://web0x07.hbtn/task3/list_file

```bash
Useful instructions:
1. Create a rapport.
2. Try multiple types of payloads in the rapport.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x07_file_inclusion
* File:3-flag.txt

### 4. Poison the logs

As usual the objective is to capture the flag however this time the flag would be set to a random path on the server.
to get it you will need to at least have a decent shell access .

* Target Machine:Cyber - WebSec 0x07
* Main Endpoint:http://web0x07.hbtn/find_your_shell/

```bash
Useful instructions:
1. Investigate what files you have permission to access.
2. Check paths under root
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x07_file_inclusion
* File:4-flag.txt

### Tasks list

* Mandatory
* Advanced


