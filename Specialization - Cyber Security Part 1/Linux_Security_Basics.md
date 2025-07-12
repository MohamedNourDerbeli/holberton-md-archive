# Project: Linux Security Basics

![Project Image](https://pbs.twimg.com/media/ESceIFMX0AIocbv.jpg)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [What is the Shell](/rltoken/B-ebXdT32Vp4WIaxc8Z8xA)
* [What is kali linux](/rltoken/OIpvnCrPiyPYECy3xG75KA)
* [File System Hierarchy](/rltoken/KADSNAsH0t1-JKvF6c9vHQ)
* [Linux file system](/rltoken/kJQK0pl_2rspnksOT6TOXQ)
* [Linux Security Command](/rltoken/ox5oIeDP1WGe0D5PIhpNYQ)
* [What are the Advantages of Using Linux ) Cybersecurity](/rltoken/S3YRE3a1ZeIHLtQoAO_2ZA)
* [Linux Networking](/rltoken/mjAlkTLQxVn3sfohSCAVVQ)
* [How to Securely Transfer Files in Linux Using SCP](/rltoken/jbx5u8OpXcbtzgCeuRKc8Q)
* [How to Set Up a Firewall with UFW on Ubuntu](/rltoken/UBJpqbmeh6pFunQvlt_NVw)
* [Guide to the Linux Firewall](/rltoken/oZ70DUm7TcDm2ou3pXq8CA)


## Learning Objectives

* What is Linux
* What is a Linux Command
* What is the structure of the Linux operating system
* What is the purpose of the FHS and what are the benefits of using it
* What are the different directories in the Linux file system, and what are their purposes
* How to protect files and directories
* How to monitor and investigate system activity
* How to securely transfer files and data
* How to configure and manage a firewall
* How to identify and terminate malicious processes


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
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable


## Tasks

### 0. What secrets hold

Write a bash script that shows you the last 5 logins session for users with their corresponding dates and times.

Depending on your machine, the output could change.

* You should run your code as privileged user.rootorsudoers.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./0-login.sh
[sudo] password for maroua: 
root     tty1                          Thu Oct 12 10:08:24 2023   still logged in
root     ttyS0                         Thu Oct 12 10:08:23 2023   still logged in
reboot   system boot  6.5.0-kali1-clou Thu Oct 12 10:08:10 2023   still running
root     tty1                          Tue Oct 10 15:08:21 2023 - down                      (19:26)
root     ttyS0                         Tue Oct 10 15:08:21 2023 - down                      (19:26)

wtmp begins Mon Sep 25 16:29:08 2023
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:0-login.sh

### 1. Shows your Linux connections, not your social status!

Write a bash script that display a list of network socket connections

The task should use iproute2 version5.x

Depending on your machine, the output could change.

* 1 You should run your code as privileged user root or sudoers.
* 2 You should Show all sockets, including listening and non-listening sockets.
* 3  You should Display numerical addresses (IP addresses and port numbers).
* 4  You should Limit the output toTCPsockets.
* 5  You should Display the process information associated with each socket.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./1-active-connections.sh
State   Recv-Q   Send-Q     Local Address:Port   Peer Address:Port   Process                                              
LISTEN  0        128                                          0.0.0.0:22                                           0.0.0.0:*                                                                          
LISTEN  0        100                                          0.0.0.0:5000                                         0.0.0.0:*                                                                          
LISTEN  0        5                                          127.0.0.1:5901                                         0.0.0.0:*                      users:(("Xtigervnc",pid=923,fd=9))                  
ESTAB   0        0                                          127.0.0.1:5901                                       127.0.0.1:36828                  users:(("Xtigervnc",pid=923,fd=38))                 
ESTAB   0        0                                          127.0.0.1:36828                                      127.0.0.1:5901                                                                       
ESTAB   0        0                                         6.19.156.8:5000                                      6.19.0.167:60812                                                                      
LISTEN  0        128                                             [::]:22                                              [::]:*                                                                          
LISTEN  0        5                                              [::1]:5901                                            [::]:*                      users:(("Xtigervnc",pid=923,fd=10))
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:1-active-connections.sh

### 2. Firewall rules: Your network's first line of defense!

Write a bash script that allow only incoming connections with the TCP protocol through port80.

Depending on your machine, the output could change.

* You should run your code as privileged user.rootorsudoers.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./2-incoming_connections.sh
[sudo] password for maroua:
Rules updated
Rules updated (v6)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:2-incoming_connections.sh

### 3. Securing your network, one rule at a time!

Write a bash script that list all the rules in the security table of the firewall.

Depending on your machine, the output could change.



* You should run your code as privileged user.rootorsudoers.
* You should use the verbose mode.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./3-firewall_rules.sh
[sudo] password for maroua: 
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destinationChain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destinationChain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:3-firewall_rules.sh

### 4. See what's talking, and who's listening!

Write a bash script that list services, their current state, and their corresponding ports.

Depending on your machine, the output could change.



* 1  You should run your code as privileged user.rootorsudoers.
* 2  You should show the PID and name of the program to which each socket belongs.
* 3  You should show numerical addresses (IP addresses and port numbers).
* 4  You should display listening sockets.
* 5  You should display TCP sockets.
* 6  You should display UDP sockets.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./4-network_services.sh
[sudo] password for maroua: 
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program nametcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      881/sshd: /usr/sbin 
tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      913/python3tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      923/Xtigervnctcp6       0      0 :::22                   :::*                    LISTEN      881/sshd: /usr/sbin 
tcp6       0      0 ::1:5901                :::*                    LISTEN      923/Xtigervncudp        0      0 0.0.0.0:68              0.0.0.0:*                           525/dhclientudp6       0      0 fe80::85e:34ff:fea6:546 :::*                                622/dhclient
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:4-network_services.sh

### 5. Where it talks, we all listen!

Write a bash script that initiate a system audit for scanning the machine.

Depending on your machine, the output could change.

* You should run your code as privileged user. `root`  or  `sudoers`.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./5-audit_system.sh
[sudo] password for maroua: 

[ Lynis 3.0.8 ]

################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.

  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################


[+] Initializing program
------------------------------------
  - Detecting OS...                                           [ DONE ]
  - Checking profiles...                                      [ DONE ]

  ---------------------------------------------------
  Program version:           3.0.8
  Operating system:          Linux
  Operating system name:     Kali Linux
  Operating system version:  Rolling release
  Kernel version:            6.5.0
  Hardware platform:         x86_64
  Hostname:                  kali
  ---------------------------------------------------
  Profiles:                  /etc/lynis/default.prf
  Log file:                  /var/log/lynis.log
  Report file:               /var/log/lynis-report.dat
  Report version:            1.0
  Plugin directory:          /etc/lynis/plugins
  ---------------------------------------------------
  Auditor:                   [Not Specified]
  Language:                  en
  Test category:             all
  Test group:                all

...

================================================================================

  Lynis 3.0.8

  Auditing, system hardening, and compliance for UNIX-based systems
  (Linux, macOS, BSD, and others)

  2007-2021, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)

================================================================================

  [TIP]: Enhance Lynis audits by adding your settings to custom.prf (see /etc/lynis/default.prf for all settings)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:5-audit_system.sh

### 6. Your eyes and ears on the network!

Write a bash script that capture and analyze network traffic going through the system.

Depending on your machine, the output could change.



* You should run your code as privileged user.rootorsudoers.
* You should limit the number of packets captured to 5

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./6-captureanalyze.sh
[sudo] password for maroua: 
tcpdump: data link type LINUXSLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
09:10:03.397281 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 3466652703:3466652721, ack 3521647673, win 24559, options [nop,nop,TS val 17390194 ecr 4276499227], length 18
09:10:03.397474 lo    In  IP localhost.34870 > localhost.5901: Flags [P.], seq 4075666532:4075666544, ack 2019255620, win 24573, options [nop,nop,TS val 1065549505 ecr 1065549431], length 12
09:10:03.398937 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 18:66, ack 1, win 24559, options [nop,nop,TS val 17390195 ecr 4276499227], length 48
09:10:03.398990 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 66:82, ack 1, win 24559, options [nop,nop,TS val 17390195 ecr 4276499227], length 16
09:10:03.399029 eth0  Out IP ip-6-19-156-8.eu-central-1.compute.internal.5000 > ip-6-19-0-167.eu-central-1.compute.internal.36014: Flags [.], ack 82, win 455, options [nop,nop,TS val 4276499301 ecr 17390194], length 0
5 packets captured
27 packets received by filter
0 packets dropped by kernel
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:6-capture_analyze.sh

### 7. So fast, it'll make your router sweat!

Write a bash script that scan a subnetwork to discover live host using scan.

Depending on the scanned subnetwork, the output could change.



* You should run your code as privileged userrootorsudoers.
* Your script should accept a subnetwork as an arguments$1.

```bash
┌──(maroua㉿HBTN-LAB)-[~/Linux Security Basics]
└─🏴 ./7-scan.sh www.holbertonschool.com
[sudo] password for maroua:
[sudo] password for maroua: 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-19 15:46 UTC
Nmap scan report for www.holbertonschool.com (34.249.200.254)
Host is up (0.026s latency).
Other addresses for www.holbertonschool.com (not scanned): 52.17.119.105 63.35.51.142
rDNS record for 34.249.200.254: ec2-34-249-200-254.eu-west-1.compute.amazonaws.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  httpsNmap done: 1 IP address (1 host up) scanned in 4.23 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x00_linux_security_basics
* File:7-scan.sh

### Tasks list

* Mandatory
* Advanced


