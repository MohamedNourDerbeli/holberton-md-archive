# Project: Protocols and Servers

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/GY7OKQ5RZNDYLUC9.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Network Protocols Explained (TCP/IP, UDP, ICMP, DNS, DHCP)](/rltoken/ReprlZ-oCtAULssPCjakbg)
* [What is SMTP? - Simple Mail Transfer Protocol Explained](/rltoken/XsRNSc0SZgrTECTUdXtevA)
* [SNMP Explained: Network Monitoring Protocol Made Easy](/rltoken/xvGBOdYUsnSu15DCtajqJw)
* [SMB Protocol Explained: File Sharing Between Devices](/rltoken/6YPSRJox8smjq1wBMzcnnQ)
* [Understanding LDAP: Lightweight Directory Access Protocol](/rltoken/gFkl570X2U-emjGJdwd7OQ)
* [Remote Desktop Protocol (RDP) Explained](/rltoken/NTfYZwgiL8rxeZvqC-Pvig)
* [The Network Stack & Protocols Explained](/rltoken/l8ot0jthlTj5SbpGQBF0nA)
* [Cybersecurity Protocols: Understanding HTTPS, SFTP, SSH](/rltoken/suzPj3-pTu0U02uKGdI_TQ)
* [Understanding Network Protocols: A Beginner’s Guide](/rltoken/Rc_w4kGMdJwhpV1O_iqqEw)
* [Network Protocols Explained: A Comprehensive Guide](/rltoken/jQJkm_3Au7x6TCamXFV1Bw)

#### References:

* [List of Network Protocols](/rltoken/EAE2tW7UMmNhWSn_LSoESw)
* [Glossary of Cyber Security Terms](/rltoken/xKXM3HsOjyxJbpA9lFyjyA)
* [HackerOne Blog - Network Security Resources](/rltoken/WK5ixgu9LEy48zdjydDvAQ)


## Learning Objectives

* What is the purpose of theNSFprotocol?
* How doesSMTPwork to send emails?
* What information doesSNMPprovide about network devices?
* How doesSMBenable file sharing between different operating systems?
* What is the role ofLDAPin authentication and authorization?
* Explain the security risks associated with usingRDP.
* Differentiate between secure protocols likeHTTPSandSFTPfrom their insecure counterparts.
* Explain the benefits of usingSSHfor secure remote access.
* Explain the concept ofport numbersand theirsignificancein network communication.
* Differentiate between different types ofnetwork encryptionprotocols.
* Explain the importance of keeping network protocolsup-to-dateandpatched.


## Requirements

### General

* All your files will be run onKali Linux 2023.2
* Allowed editors:vi,vim,emacs
* You must substitute the IP range for$1.
* The first line of all your files should be exactly#!/bin/bash.
* All your files should end with a new line.
* All your scripts should be 2 lines long$ wc -l fileshould print  2.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl


## Tasks

### 0. Analyze iptables Rules

Write a script to display all currentiptablesrules in a readable format, including line numbers.



```bash
$ sudo ./0-iptables.sh
Chain DOCKER-USER (1 references)
num   pkts bytes target     prot opt in     out     source               destination1        0     0 RETURN     0    --  *      *       0.0.0.0/0            0.0.0.0/0
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:0-iptables.sh

### 1. Audit SSH Configuration

Write a script to check for and report any non-standard SSH configuration settings in/etc/ssh/sshd_config.



```bash
$ sudo ./1-audit.sh
Include /etc/ssh/sshdconfig.d/*.conf
KbdInteractiveAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC*
Subsystem       sftp    /usr/lib/openssh/sftp-server
PasswordAuthentication yes
PermitRootLogin yes
AuthorizedKeysFile .ssh/authorized_keys
TCPKeepAlive yes
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:1-audit.sh

### 2. Harden Linux Server

Write a script to list all world-writable directories and set their permissions to a more secure level.

```bash
$ sudo ./2-harden.sh
/home/user1
/home/user2
/home/user3
/var/www/html/uploads
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:2-harden.sh

### 3. Identify Common Vulnerabilities

Write a script to check for unpatched common vulnerabilities usinglynisaudit tool.

```bash
$ sudo ./3-identify.sh
[ Lynis 3.0.9 ]
################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.
  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################
[+] Initializing program
------------------------------------
  ###################################################################
  #                                                                 #
  #   NON-PRIVILEGED SCAN MODE                                      #
  #                                                                 #
  ###################################################################
  NOTES:
  --------------
  * Some tests will be skipped (as they require root permissions)
  * Some tests might fail silently or give different results
  - Detecting OS...                                           [ DONE ]
  - Checking profiles...                                      [ DONE ]
  ---------------------------------------------------
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:3-identify.sh

### 4. Check for NFS Vulnerabilities

Write a script to scan for NFS shares that are accessible by anyone on the network.

```bash
$ sudo ./4-nfs.sh 192.168.1.100
Export list for 192.168.1.100:
/data (everyone)
/home (10.0.0.2)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:4-nfs.sh

### 5. Audit SNMP Configuration

Write a script to find SNMP configurations that allow public access.

```bash
$ sudo ./5-snmp.sh
com2sec public default public
rocommunity public
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:5-snmp.sh

### 6. Examine SMTP Server Settings

Write a script to check the SMTP server configuration for lack of STARTTLS or other security features.
If STARTTLS not configured returnSTARTTLS not configured

```bash
$ sudo ./6-smtp.sh
smtpd_tls_security_level = may
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:6-smtp.sh

### 7. Simulate DoS Attack on HTTP Server

Write a script to simulate a basic Denial of Service attack on an HTTP server usinghping3.

```bash
$ sudo ./7-dos.sh 192.168.1.100
HPING 192.168.1.100 (eth0 10.0.0.2): rand data
Using eth0, addr: 10.0.0.2, MTU: 1500
HPING 192.168.1.100 (eth0 10.0.0.2) with 1460 data bytes
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:7-dos.sh

### 8. Check for Weak SSL/TLS Ciphers

Write a script to test an SSL/TLS server’s ciphers and report any weak ciphers usingnmap.

```bash
$ sudo ./8-cipher.sh 192.168.1.100
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-11 15:00 UTC
Nmap scan report for some_random_ip
Host is up (0.042s latency).

PORT    STATE SERVICE
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 2.01 seconds

Host script results:
| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:8-cipher.sh

### 9. Implement Basic Firewall Rules

Write a script to set up basic iptables firewall rules that block all incoming traffic except SSH.

Note: For this specific task, wc -l file should print 3.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x03_protocols_servers
* File:9-firewall.sh

### Tasks list

* Mandatory
* Advanced


