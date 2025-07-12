# Project: Nmap Live Host Discovery

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/9TAMD978EUX8X4V1.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Nmap documentation](/rltoken/pPySvd9FKOQG5qMlmfM-nw)
* [Nmap Description](/rltoken/EBExB-iJML696ojWK8fzeg)
* [Nmap Options Summary](/rltoken/uMq8QusTd62UCNCRHQ_eeQ)
* [Target Specification](/rltoken/TgdUAwm-r-FqnFNUdmYX5g)

#### References:

* [Host Discovery](/rltoken/LivAd8kNi8PCyYUqn6CE4g)


## Learning Objectives

* What isnmap.
* How to usenmap.
* How doesnmapscan work
* What isSubnetworks.
* How to enumerateTargets.
* What is ARP Scan
* What is ICMPEchoScan
* What is ICMP Timestamp Scan
* What is ICMP Address Mask Scan
* What is TCPSYNPing Scan
* What is TCPACKPing Scan
* What isUDPPing Scan
* What cannmapdetect
* How to scan an IP address withnmap.
* How to check ports withnmap.


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
* Ensure that$1is used without quotes in your script to prevent unintended argument type alterations.


## Tasks

### 0.  Will arp be enough ?

Writea bash scriptthat scana subnetworkto discover live host usingARPscan.

Depending on the scanned subnetwork, the output could change.We can’t expect to learn about the Target MAC Address, unless we are in the the samesubnetwork.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./0-arp_scan.sh 192.168.65.0/24
[sudo] password for yosri:
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-22 05:02 CDT
Nmap scan report for 192.168.65.1
Host is up (0.00064s latency).
MAC Address: C6:91:0C:4B:4E:64 (Unknown)
Nmap scan report for 192.168.65.2
Host is up.
Nmap done: 256 IP addresses (2 hosts up) scanned in 2.03 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:0-arp_scan.sh

### 1.  Host, do you hear me ?

Writea bash scriptthat scana subnetworkto discover live host usingICMP Echoscan.

Depending on the scanned subnetwork, the output could change.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./1-icmp_echo_scan.sh 6.19.100.0/24
[sudo] password for yosri:
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:02 CDT
Nmap scan report for 6.19.100.2
Host is up (0.14s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.03 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:1-icmp_echo_scan.sh

### 2.  Time always matter

Writea bash scriptthat scana subnetworkto discover live host usingICMP Timestampscan.

Depending on the scanned subnetwork, the output could change.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./2-icmp_timestamp_scan.sh 6.19.100.0/24
[sudo] password for yosri:
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:17 CDT
Nmap scan report for 6.19.100.2
Host is up (0.16s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.93 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:2-icmp_timestamp_scan.sh

### 3.  Sometimes we need Masks !

Writea bash scriptthat scana subnetworkto discover live host usingICMP Address Maskscan.

Depending on the scanned subnetwork, the output could change.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./3-icmp_address_mask_scan.sh 6.19.100.0/24
[sudo] password for yosri
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 254 IP address (0 hosts up) scanned in 53.01 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:3-icmp_address_mask_scan.sh

### 4.  SYN Scan me



Writea bash scriptthat scana subnetworkto discover live host usingTCP SYN Pingscan.

Depending on the scanned subnetwork, the output could change.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* Your code should scan for those ports22,80,443.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./4-tcp_syn_ping.sh 6.19.100.0/24
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:40 CDT
Nmap scan report for 6.19.100.2
Host is up (0.12s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 22.42 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:4-tcp_syn_ping.sh

### 5.  Are your privileged enough to scan me ?



Writea bash scriptthat scana subnetworkto discover live host using  *TCP ACK Ping*scan.

Depending on the scanned subnetwork, the output could change.Unprivileged users have no choice but to complete the 3-way handshake if the port is open.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* Your code should scan for those ports22,80,443.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./5-tcp_ack_ping.sh 6.19.100.0/24
[sudo] password for yosri:
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 256 IP addresses (0 hosts up) scanned in 154.50 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:5-tcp_ack_ping.sh

### 6.  UDP is our last hope

Writea bash scriptthat scana subnetworkto discover live host usingUDP Pingscan.

* You should usenmap.
* Your code should tell nmapnotto do a port scan after host discovery.
* Your code should scan for those ports53,161,162.
* You should run your code as privileged user.rootorsudoers.
* Your script should accepta subnetworkas an arguments$1.

```bash
┌──(yosri)-[~/0x04_nmap_live_hosts_discovery]
└─🏴 ./6-udp_ping_scan.sh 6.19.100.0/24
[sudo] password for yosri:
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 15:10 CDT
Nmap scan report for 6.19.100.2
Host is up (0.13s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 23.39 seconds
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:6-udp_ping_scan.sh

### 7.  Simple Catch, is it mimicked ?

Time To PingThe Target(cybernetsec_0x04)

Catch the flag time is on, here is some tips:

* You should run your scan as privileged user.rootorsudoers.
* The Current Flag is hidden withinUDPopened port serviceVERSION
* Two hundred, Three hundred but no more.-p200-300

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x04_nmap_live_hosts_discovery
* File:100-flag.txt

### Tasks list

* Mandatory
* Advanced


