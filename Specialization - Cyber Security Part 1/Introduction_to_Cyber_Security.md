# Project: Introduction to Cyber Security

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/CZ2WGOHCYQXCN7LE.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Important:

* [Kali Setup - Virtual Machine](/rltoken/KwhEKwRldMeZVxH-S-tyUQ)
* [Kali Setup - desktops & laptops](/rltoken/8bEycGRpB2dZFKYZtIqmWA)

#### Read or watch:

* [What is Cybersecurity?](/rltoken/i39Tr7zSc0fyG2A-2X8_WQ)
* [The 5 Types of Cybersecurity](/rltoken/vPGOJOENPiMFrzDLHM-sXA)
* [The 5 Most Important Cybersecurity Concepts](/rltoken/IZiw0Ikzdoro3xUe3iCA9Q)
* [Cybersecurity Basics: A Hands-on Approach](/rltoken/zEx3Opx3jAx69HP7a_dA7g)
* [Understanding Cybersecurity Threats](/rltoken/_dDFivYeH_dBhax7O53xJQ)
* [Understanding the Fundamentals of Cybersecurity Frameworks](/rltoken/SKrlHSY97akssTgvuHTRlA)
* [The CIA Triad](/rltoken/-0HDx3VBZU1co6qYYPsxww)
* [Cyber Security Risk Management](/rltoken/Qsn9XZeyMTXxVdBk_0vgwg)

#### References:

* [CISA](/rltoken/YehQpMc0nkvDoSGds3biPg)
* [NIST](/rltoken/W04lkczMLXuu-eLj3rariw)
* [OWASP](/rltoken/r09i7XrUY7n5_pWj0EPVNg)
* [SANS](/rltoken/ppbAeZx4dfs5fJSPRqcnKQ)
* [ISF](/rltoken/BR318HQIPdLsrPpEYLSFtQ)
* [ISC²](/rltoken/ukZArUOlbR97-t3OQw7aNg)


## Learning Objectives

* What isCybersecurity?
* What are the core principles of cybersecurity?(CIA Triad)
* How doesencryptioncontribute to security?
* What isrisk managementin cybersecurity?
* What are the different types of cybersecuritythreats?
* What is the difference between avirusanda worm?
* What issocial engineeringin the context of security?
* What are the key components of an information security program?
* How do security policies and frameworks contribute to an organization’s security posture?
* What is the purpose of theOWASPTop Ten?
* What is the role ofaccess controlin cybersecurity?
* How doesmulti-factorauthentication enhance security?
* What are the common methods for securing a network?


## Requirements

### General

* All your files will be run onKali Linux 2023.2
* Allowed editors:vi,vim,emacs
* You must substitute the IP range for$1.
* The first line of all your files should be exactly#!/bin/bash.
* All your files should end with a new line.
* All your scripts should be less than 2 lines long ($ wc -l file should print <= 2).
* You are not allowed to use backticks,&&,||or;.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* You are not Allowed to use NeitherPrintf.


## Tasks

### 0. Did you install kali ?

Write a bash script that display thedistributor IDin a concise single-line output.

Do not useawk

* Your Script Should Have one Line and New Line Only

```bash
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_cybersecurity_basics]
└─$ ./0-release.sh
Kali
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x00_introduction_cybersecurity
* File:0-release.sh

### 1. We always need strong Passwords

Create a Bash script that generates a strong random password:

The output may vary for each execution

* Your script should be less than 3 lines long.
* You should accept password length as an args.
* You should use/dev/urandom
* You should use[:alnum:]as character classes.

```bash
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./1-gen_password.sh 20
MkPpprPyC3i6navUB3Lj
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x00_introduction_cybersecurity
* File:1-gen_password.sh

### 2. Verify the integrity of a file

Create a Bash script that validate the integrity of a file:

* Your script should be less than 3 lines long.
* You can useechoin this task

```bash
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./2-sha256_validator.sh test_file e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855             
test_file: OK
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x00_introduction_cybersecurity
* File:2-sha256_validator.sh

### 3. We need an SSH key pair!

Create a Bash script that generates an RSA SSH key pair.

* Your key size should be4096
* You Should UseOpen-ssh

```bash
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./3-gen_key.sh new_key
Generating public/private rsa key pair.
Your identification has been saved in new_key
Your public key has been saved in new_key.pub
The key fingerprint is:
SHA256:aq73wv2/5u6k/qoGF83U3DZNsy5jg7Omv+zCSHkdbUM yosri@hbtn-lab
The key's randomart image is:
+---[RSA 4096]----+
|           o . +.|
|          . oE+ +|
|         +  o. o |
|        . o..+.  |
|        S..oo=.. |
|      .+.. .+ +  |
|     .+++  o.    |
|     o+.oo+o.    |
|    .o.+o=O&O.   |
+----[SHA256]-----+
                                                                                                                                                                                                                                            
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ls -l new_key*
-rw------- 1 yosri yosri 3381 Dec 19 18:50 new_key
-rw-r--r-- 1 yosri yosri  740 Dec 19 18:50 new_key.pub
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x00_introduction_cybersecurity
* File:3-gen_key.sh

### 4. Let's Monitor root activity

Create a Bash script that monitors all processes started by specified user.

The output may vary depending on your active processes

* Your script should acceptuseras 1st agrs.
* Your script should usegrep -vto exclude processes with VSZ and RSS values of 0
* You Should Usepscommand

```bash
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./4-root_process.sh root
root           1  0.0  0.0  21172 12376 ?        Ss   07:38   0:01 /sbin/init splash
root         598  0.0  0.1  66380 19908 ?        Ss   07:39   0:00 /lib/systemd/systemd-journald
root         614  0.0  0.0 152264  1548 ?        Ssl  07:39   0:00 vmware-vmblock-fuse /run/vmblock-fuse -o rw,subtype=vmware-vmblock,default_permissions,allow_other,dev,suid
root         619  0.0  0.0  28688  8192 ?        Ss   07:39   0:00 /lib/systemd/systemd-udevd
root         768  0.0  0.0   8264  5304 ?        Ss   07:39   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         779  0.0  0.0 315484 12708 ?        Ssl  07:39   0:30 /usr/bin/vmtoolsd
root        1005  0.0  0.0 311384  9268 ?        Ssl  07:39   0:00 /usr/libexec/accounts-daemon
root        1006  0.0  0.0   7032  2432 ?        Ss   07:39   0:00 /usr/sbin/cron -f
root        1014  0.0  0.0  17592  8320 ?        Ss   07:39   0:00 /lib/systemd/systemd-logind
root        1048  0.0  0.1 333664 20784 ?        Ssl  07:39   0:02 /usr/sbin/NetworkManager --no-daemon
root        1056  0.0  0.0 392124 11992 ?        Ssl  07:39   0:00 /usr/sbin/ModemManager
root        1119  0.0  0.0 382288  8900 ?        SLsl 07:39   0:00 /usr/sbin/lightdm
root        1121  0.0  0.2 2091040 44628 ?       Ssl  07:39   0:41 /usr/bin/containerd
root        1605  0.0  0.0 314176 12784 ?        Ssl  07:39   0:00 /usr/libexec/upowerd
root        1838  0.0  0.1 471588 18520 ?        Ssl  07:39   0:00 /usr/libexec/udisks2/udisksd
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x00_introduction_cybersecurity
* File:4-root_process.sh

### Tasks list

* Mandatory
* Advanced


