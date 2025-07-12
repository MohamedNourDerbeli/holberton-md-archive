# Project: Nmap Advanced Port Scans

![Project Image](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*gz8UhzrUIqbkVWDamGSSbA.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Nmap documentation](/rltoken/xG7kWATvjO_E2DZDHzu0Hw)
* [Nmap Advanced Scan](/rltoken/Fu4PYm5hC7ap_F-73V1nPA)
* [Everything You Need to Know About Port Scanning](/rltoken/hdwWiCr8LeePc7811ZN8Gg)
* [Advanced Port Scanning techniques](/rltoken/dTXazz3nzH6iCEFL1BC9rg)
* [What is a Port Scanner and How Does it Work?](/rltoken/whYd6R7Ry5M5qaTHG8WUgQ)
* [How to use Nmap to Scan for Open Ports?](/rltoken/cRk_Uml5BYRw1RSa_4yKOg)
* [Nmap to scan all ports](/rltoken/UG0ik-9ECEuoT0ijxu6Xzg)
* [How to Use Nmap to Scan for Open Ports](/rltoken/0_BN28sWAc7zT829YFrX8Q)
* [How To Scan All Ports With NMap](/rltoken/9VzSrlW9LOx0TtQqBdBBhQ)
* [Nmap: TCP and UDP port mapping](/rltoken/9univoPoUZTesWgbaE5jOw)

#### References:

* [Port Scanning](/rltoken/xI19Wa-Pg43oZY-D-BQ8Lg)


## Learning Objectives

* How to Use Nmap for Advanced Port Scans?
* What are the Different Types of Advanced Port Scans?
* How Advanced Nmap Scans Work?
* What can be detected with Advanced Port Scans?
* What are the use cases and scenarios for Advanced Port Scans?
* What is the main difference between a standard Nmap scan and an advanced port scan?
* What are the differences between a TCP Connect Scan and a SYN Scan ?
* How does anACKScan help in determining firewall rules?
* What areFIN,NULL, andXmasscans, and how can they be used to determine the status of ports on a target system?
* Why do You need Nmap For Securing System Ports?
* What types of information can an advanced port scan reveal about a network?


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
* All your files must be executable.
* You should start your script withsudo.
* You are not allowed to use ‘echo’.
* Ensure that$1is used without quotes in your script to prevent unintended argument type alterations.


## Tasks

### 0. NULL scan: Hear secrets by pretending not to listen!



Null scanssend empty TCP packets to a target. Open ports might silently accept them, while closed ports may respond,
giving attackers a clue. They’re stealthy.

Write a bash script that executes aTCP NULLscan on ahost, targeting ports20to25.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./0-null_scan.sh www.holbertonschool.com
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-17 15:58 CET
Nmap scan report for www.holbertonschool.com (63.35.51.142)
Host is up (0.078s latency).
Other addresses for www.holbertonschool.com (not scanned): 34.249.200.254 52.17.119.105
rDNS record for 63.35.51.142: ec2-63-35-51-142.eu-west-1.compute.amazonaws.com

PORT   STATE         SERVICE
20/tcp open|filtered ftp-data
21/tcp open|filtered ftp
22/tcp open|filtered ssh
23/tcp open|filtered telnet
24/tcp open|filtered priv-mail
25/tcp open|filtered smtp

Nmap done: 1 IP address (1 host up) scanned in 2.54 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:0-null_scan.sh

### 1. FIN scans: like ghost-knocking on digital doors!



AFIN scanis a network reconnaissance technique used to identify open ports on a target machine.
It works by sending aTCPpacket with only theFINflag set, which typically signifies the end of a connection.
By analyzing the target’s response, attackers can determine if a port is open, closed, or filtered by a firewall.

FINscans are attractive because they can sometimes bypass basic firewalls and offer a stealthier approach compared 
to traditional methods.

Write a bash script that executes aFIN scanon a test network.The scan should identify potential stealth ports,
focusing on ports80to85.

Depending on the scanned network, the output could change, this scan may require some time to finish.

* Your script should accepthostas an arguments$1.
* Your script should use packet fragmentation to evade packet filters.
* Your script should Adjust the timing option to2to reduce scan detectability.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./1-fin_scan.sh www.holbertonschool.com
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-22 13:30 CET
Nmap scan report for www.holbertonschool.com (52.17.119.105)
Host is up (0.17s latency).
Other addresses for www.holbertonschool.com (not scanned): 63.35.51.142 34.249.200.254 64:ff9b::3411:7769 64:ff9b::22f9:c8fe 64:ff9b::3f23:338e
rDNS record for 52.17.119.105: ec2-52-17-119-105.eu-west-1.compute.amazonaws.com

PORT   STATE         SERVICE
80/tcp open|filtered http
81/tcp open|filtered hosts2-ns
82/tcp open|filtered xfer
83/tcp open|filtered mit-ml-dev
84/tcp open|filtered ctf
85/tcp open|filtered mit-ml-dev

Nmap done: 1 IP address (1 host up) scanned in 17.14 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:1-fin_scan.sh

### 2. Xmas scans: turning network packets into holiday lights!



AnXmasscan utilizes TCP packets flagged withFIN,PSH, andURGto stealthily detect open ports,
leveraging its unique packet configuration to potentially bypass firewall detection.

This technique, named for itsilluminatedpacket headers, primarily receives responses from closed ports, 
making it a subtle tool for network analysis.

Write a bash script that executes axmas scanon a test network.The scan should identify potential stealth ports,
focusing on ports440to450.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.
* Your script should only show open (or possibly open) ports.
* Your script should show all packets sent and received.
* Your script should display the reason each port is set to a specific state.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./2-xmas_scan.sh www.holbertonschool.com
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-18 15:54 CET
SENT (0.1584s) ICMP [10.5.202.26 > 52.17.119.105 Echo request (type=8/code=0) id=40212 seq=0] IP [ttl=56 id=56105 iplen=28 ]
SENT (0.1584s) TCP 10.5.202.26:57513 > 52.17.119.105:443 S ttl=49 id=2579 iplen=44  seq=1688269977 win=1024SENT (0.1584s) TCP 10.5.202.26:57513 > 52.17.119.105:80 A ttl=43 id=33442 iplen=40  seq=0 win=1024 
SENT (0.1584s) ICMP [10.5.202.26 > 52.17.119.105 Timestamp request (type=13/code=0) id=36086 seq=0 orig=0 recv=0 trans=0] IP [ttl=45 id=39982 iplen=40 ]
RCVD (0.2425s) TCP 52.17.119.105:443 > 10.5.202.26:57513 SA ttl=107 id=0 iplen=44  seq=960423197 win=62727NSOCK INFO [0.2810s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [0.2810s] nsock_connect_udp(): UDP connection requested to 127.0.0.53:53 (IOD #1) EID 8
NSOCK INFO [0.2810s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 18
NSOCK INFO [0.2810s] nsock_write(): Write request for 44 bytes to IOD #1 EID 27 [127.0.0.53:53]
NSOCK INFO [0.2810s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [127.0.0.53:53]
NSOCK INFO [0.2810s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [127.0.0.53:53]
NSOCK INFO [0.5500s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [127.0.0.53:53] (107 bytes)
NSOCK INFO [0.5500s] nsock_read(): Read request from IOD #1 [127.0.0.53:53] (timeout: -1ms) EID 34
NSOCK INFO [0.5500s] nsock_iod_delete(): nsock_iod_delete (IOD #1)

[...]

Nmap scan report for www.holbertonschool.com (52.17.119.105)
Host is up, received syn-ack ttl 107 (0.083s latency).
Other addresses for www.holbertonschool.com (not scanned): 34.249.200.254 63.35.51.142
rDNS record for 52.17.119.105: ec2-52-17-119-105.eu-west-1.compute.amazonaws.com

PORT    STATE         SERVICE       REASON
440/tcp open|filtered sgcp          no-response
441/tcp open|filtered decvms-sysmgt no-response
442/tcp open|filtered cvc_hostd     no-response
443/tcp open|filtered https         no-response
444/tcp open|filtered snpp          no-response
445/tcp open|filtered microsoft-ds  no-response
446/tcp open|filtered ddm-rdb       no-response
447/tcp open|filtered ddm-dfm       no-response
448/tcp open|filtered ddm-ssl       no-response
449/tcp open|filtered as-servermap  no-response
450/tcp open|filtered tserver       no-response

Nmap done: 1 IP address (1 host up) scanned in 3.17 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:2-xmas_scan.sh

### 3. Maimon scans: the silent knock of network probing!

Maimonscans: like knocking on doors with a magic wand — some ignore you, some slam the door, 
but you walk away without a trace!

A Maimon scan sendsTCPpackets with bothFINandACKflags set to determine port status on a target machine.

Write a bash script that executes aMaimonscan on a test network.The scan should identify potential stealth ports,
focusing on scanning the following service ports:http,https,ftp,ssh, andtelnet.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.
* Your script should scan ports with high verbosity.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./3-maimon_scan.sh www.holbertonschool.com
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-22 13:43 CET
Warning: Hostname www.holbertonschool.com resolves to 6 IPs. Using 34.234.52.18.
Initiating Ping Scan at 13:43
Scanning www.holbertonschool.com (34.234.52.18) [4 ports]
Completed Ping Scan at 13:43, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:43
Completed Parallel DNS resolution of 1 host. at 13:43, 0.00s elapsed
Initiating Maimon Scan at 13:43
Scanning www.holbertonschool.com (34.234.52.18) [5 ports]
Completed Maimon Scan at 13:43, 2.95s elapsed (5 total ports)
Nmap scan report for www.holbertonschool.com (34.234.52.18)
Host is up, received syn-ack ttl 105 (0.17s latency).
Other addresses for www.holbertonschool.com (not scanned): 3.233.126.24 52.206.163.162 64:ff9b::3411:7769 64:ff9b::3f23:338e 64:ff9b::22f9:c8fe
rDNS record for 34.234.52.18: ec2-34-234-52-18.compute-1.amazonaws.com
Scanned at 2024-04-22 13:43:45 CET for 3s

PORT    STATE         SERVICE REASON
21/tcp  open|filtered ftp     no-response
22/tcp  open|filtered ssh     no-response
23/tcp  open|filtered telnet  no-response
80/tcp  open|filtered http    no-response
443/tcp open|filtered https   no-response

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 5.96 seconds
           Raw packets sent: 15 (596B) | Rcvd: 2 (88B)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:3-maimon_scan.sh

### 4. TCP ACK scans: When you knock on the firewall's door just to see who yells back!



TheTCP ACKscan is a network probing technique used primarily to determine the filtering rules of a firewall. 
By sending a packet with theACKflag set to various ports, and observing whether the target responds with 
anRSTpacket, security professionals can infer whether ports are statefully inspected.

You are a network administrator responsible for verifying the firewall rules for a newly deployed section of your
corporate network. Before deploying critical services, you want to ensure that the firewall is properly filtering 
unexpected external ACK packets, which should all be blocked or filtered to enhance security against potential 
reconnaissance activities by attackers.

Write a bash script that performs a TCP ACK scan on a specified test network. The scan should identify potential stealth ports,
focusing on ports80,22,25.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.
* Your script should acceptportsas an arguments$2.
* Your script should display the reason each port is set to a specific state.
* Your script should enforce a time limit of1000milliseconds for each host response.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./4-ask_scan.sh www.holbertonschool.com 80,22,25
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-19 13:28 CET
Nmap scan report for www.holbertonschool.com (52.17.119.105)
Host is up, received reset ttl 31 (0.17s latency).
Other addresses for www.holbertonschool.com (not scanned): 63.35.51.142 34.249.200.254 64:ff9b::3f23:338e 64:ff9b::3411:7769 64:ff9b::22f9:c8fe
rDNS record for 52.17.119.105: ec2-52-17-119-105.eu-west-1.compute.amazonaws.com

PORT   STATE      SERVICE REASON
22/tcp unfiltered ssh     reset ttl 20
25/tcp unfiltered smtp    reset ttl 18
80/tcp unfiltered http    reset ttl 27

Nmap done: 1 IP address (1 host up) scanned in 0.57 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:4-ask_scan.sh

### 5. TCP Window Scan: Like checking a letter's fine print to see if you're invited!



TheTCP Windowscan refines the technique used inACKscans by analyzing the |TCP windowsize ofRSTpackets returned from a target.
If a port is open, theTCP windowsize in theRSTpacket is often non-zero, subtly indicating an active listening state,
whereas closed ports generally return a zero window size.

This method is useful when more common scans like SYN are blocked, offering an alternative for deducing port status.

Write a bash script that performs a aTCP Windowscan on a specified test network. The scan should identify potential stealth ports,
in the range from20to30, but exclude ports from25to28.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.
* Your script should acceptportsas an arguments$2.
* Your script should accept a range of ports to exclude as an argument$3.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./5-window_scan.sh www.holbertonschool.com 20-30 25-28
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-19 15:38 CET
Nmap scan report for www.holbertonschool.com (3.233.126.24)
Host is up (0.22s latency).
Other addresses for www.holbertonschool.com (not scanned): 34.234.52.18 52.206.163.162 64:ff9b::22f9:c8fe 64:ff9b::3f23:338e 64:ff9b::3411:7769
rDNS record for 3.233.126.24: ec2-3-233-126-24.compute-1.amazonaws.com

PORT   STATE SERVICE
20/tcp open  ftp-data
21/tcp open  ftp
22/tcp open  ssh
23/tcp open  telnet
24/tcp open  priv-mail
29/tcp open  msg-icp
30/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.86 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:5-window_scan.sh

### 6. Custom Scan: Because even network security likes its coffee made a certain way!



ACustom Scanis a targeted method used in network security to evaluate specific vulnerabilities or areas within 
a network. It enables cybersecurity experts to focus on particular segments, ports, or protocols, optimizing
resources and identifying critical weaknesses more effectively.

The security team decides to use an advancedNmapscan that manipulatesTCP flagsto create non-standard packets, 
which are typically not used in regular communications but might be utilized by attackers to probe and exploit 
vulnerabilities in network defenses.

Write a bash script that executes acustom scan. The script should configure Nmap to send packets with all possibleTCP flagsset, targeting ports80to90on a specified host.

Depending on the scanned network, the output could change.

* Your script should accepthostas an arguments$1.
* Your script should acceptportsas an arguments$2.
* Your script should save the output to the filecustom_scan.txt.
* Your script should redirect both error messages and standard output to ensure nothing appears on the screen.

```bash
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 ./6-custom_scan.sh www.holbertonschool.com 80-90
[sudo] password for maroua:
┌──(maroua)-[~/0x06_nmap_advanced_port_scans]
└─🏴 cat custom_scan.txt
# Nmap 7.80 scan initiated Fri Apr 19 19:30:06 2024 as: nmap -scanflags URGACKPSHRSTSYNFIN -p 80-90 -oN custom.txt www.holbertonschool.com
Nmap scan report for www.holbertonschool.com (3.233.126.24)
Host is up (0.16s latency).
Other addresses for www.holbertonschool.com (not scanned): 34.234.52.18 52.206.163.162 64:ff9b::34ce:a3a2 64:ff9b::22ea:3412 64:ff9b::3e9:7e18
rDNS record for 3.233.126.24: ec2-3-233-126-24.compute-1.amazonaws.com

PORT   STATE    SERVICE
80/tcp filtered http
81/tcp filtered hosts2-ns
82/tcp filtered xfer
83/tcp filtered mit-ml-dev
84/tcp filtered ctf
85/tcp filtered mit-ml-dev
86/tcp filtered mfcobol
87/tcp filtered priv-term-l
88/tcp filtered kerberos-sec
89/tcp filtered su-mit-tg
90/tcp filtered dnsix

# Nmap done at Fri Apr 19 19:30:10 2024 -- 1 IP address (1 host up) scanned in 4.55 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x06_nmap_advanced_port_scans
* File:6-custom_scan.sh

### Tasks list

* Mandatory
* Advanced


