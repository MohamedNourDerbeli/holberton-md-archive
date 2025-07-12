# Project: Wireshark Basics

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/J4QLEZM61NAORC8V.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

Example:



cyber-sec@ubuntu$



IfWiresharkis not already installed on your terminal

## Resources

#### Read or watch:

* [TCP/IP Packet Formats and Ports](/rltoken/HyNzjFW3bi1yrAB76Lj7Dw)
* [Wireshark-Filters](/rltoken/mFJvTfTYzgnPLhPJTDK4ng)
* [Working With Captured Packets](/rltoken/9XYIDMH6eOrRnIZIvUwI7Q)
* [Examine a captured packet using Wireshark](/rltoken/hORJTvP7LurmWw8zO3BKEA)
* [How to Read Packets in Wireshark](/rltoken/51gfdEvNztw12z3XNrezCA)


## Learning Objectives

* What isWireshark.
* How to useWiresharkfilters .
* Analyzing a Package withWireshark.


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* AREADME.mdfile, at the root of the folder of the project, is mandatory .
* You are free to choose any IP address for testing.


## Tasks

### 0.  IP protocol scan

Create a Wireshark filter to detect packets sent by thenmap -sO <target>command for IP protocol scanning.

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
    370 11.616723413   172.22.101.90         216.58.205.206        ICMP     34     

Frame 370: 34 bytes on wire (272 bits), 34 bytes captured (272 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 216.58.205.206
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:0-ip_scan.txt

### 1.  TCP SYN scan

Create a Wireshark filter to detect packets sent by thenmap -sS <target>command for TCP SYN scan.

Hint: run the nmap command and try to capture your own packet .Hint: check thewindow_size.

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
     86 6.873523942    172.22.101.90         172.217.17.110        TCP      58 60792 → 3306 [SYN] Seq=0 Win=1024 Len=0 MSS=1460

Frame 86: 58 bytes on wire (464 bits), 58 bytes captured (464 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 172.217.17.110
Transmission Control Protocol, Src Port: 34124, Dst Port: 443, Seq: 0, Len: 0
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:1-tcp_syn.txt

### 2.  TCP Connect() scan

Create a Wireshark filter to detect packets sent by thenmap -sT <target>command for TCP Connect() scan.

Hint: run the nmap command and try to capture your own packet .Hint: check thewindow_size.

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
     27 1.540073953    172.22.101.90         142.250.200.206       TCP      74     58264 → 21 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=737940926 TSecr=0 WS=128

Frame 27: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 142.250.200.206
Transmission Control Protocol, Src Port: 58264, Dst Port: 21, Seq: 0, Len: 0
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:2-tcp_connect_scan.txt

### 3.  TCP FIN scan

Create a Wireshark filter to detect packets sent by thenmap -sF <target>command for TCP FIN scan .

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
    182 12.253459933   172.22.101.90         172.217.17.110        TCP  54  51895 → 53 [FIN] Seq=1 Win=1024 Len=0

Frame 182: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 172.217.17.110
Transmission Control Protocol, Src Port: 34380, Dst Port: 23, Seq: 1, Len: 0
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:3-tcp_fin.txt

### 4.  TCP ping sweeps

Create a Wireshark filter to detect packets sent by thenmap -sn -PS/-PA <subnet>command for TCP SYN Ping/TCP ACK Ping .

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.   Time              Source          Destination     Protocol  Length  Info
1     0.000000          192.168.1.100   203.0.113.5     TCP       74      56789 > 80 [SYN] Seq=0 Win=8192 Len=0
2     0.001000          203.0.113.5     192.168.1.100   TCP       74      80 > 56789 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0
3     0.002000          192.168.1.100   203.0.113.5     TCP       74      56789 > 80 [ACK] Seq=1 Ack=1 Win=17520 Len=0


Frame 17: 58 bytes on wire (464 bits), 58 bytes captured (464 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 142.250.200.206
Transmission Control Protocol, Src Port: 44255, Dst Port: 80, Seq: 0, Len: 0
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:4-tcp_ping_sweep.txt

### 5.  UDP port scan

Create a Wireshark filter to detect packets sent by thenmap -sU <target>command for UDP port scan .

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
   1340 4.982253065    142.250.200.206       172.22.101.90         ICMP     70     Destination unreachable (Port unreachable)

Frame 1340: 70 bytes on wire (560 bits), 70 bytes captured (560 bits) on interface wlo1, id 0
Ethernet II, Src: d4:76:a0:53:43:94 (d4:76:a0:53:43:94), Dst: b4:0e:de:92:17:97 (b4:0e:de:92:17:97)
Internet Protocol Version 4, Src: 142.250.200.206, Dst: 172.22.101.90
Internet Control Message Protocol
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:5-udp_port_scan.txt

### 6.  UDP ping sweeps

Create a Wireshark filter to detect packets sent by thenmap -sn -PU <subnet>command for UDP ping sweeps .

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
     92 6.850769581    172.22.101.90         142.250.200.206       UDP      42     59791 → 40125 Len=0

Frame 92: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 142.250.200.206
User Datagram Protocol, Src Port: 59791, Dst Port: 40125
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:6-udp_ping_sweep.txt

### 7.  ICMP ping sweep

Create a Wireshark filter to detect packets sent by thenmap -sn -PE <subnet>command for ICMP ping sweeps .

Hint: run the nmap command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
     29 1.667485121    172.22.101.90         142.250.1.0           ICMP     42     Echo (ping) request  id=0x1d0b, seq=0/0, ttl=54 (no response found!)

Frame 29: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface wlo1, id 0
Ethernet II, Src: b4:0e:de:92:17:97 (b4:0e:de:92:17:97), Dst: d4:76:a0:53:43:94 (d4:76:a0:53:43:94)
Internet Protocol Version 4, Src: 172.22.101.90, Dst: 142.250.1.0
Internet Control Message Protocol
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:7-icmp_ping_sweep.txt

### 8.  ARP scanning

Create a Wireshark filter to detect packets sent by thearp-scan -lcommand for ARP scanning .

Hint: run the arp command and try to capture your own packet .

* Your Filter string should be able to capture packets similar to this:

```bash
No.     Time           Source                Destination           Protocol Length Info
      1 0.000000000    d4:76:a0:53:43:94     Broadcast             ARP      60     Who has 172.22.101.231? Tell 172.22.101.254

Frame 1: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface wlo1, id 0
Ethernet II, Src: d4:76:a0:53:43:94 (d4:76:a0:53:43:94), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x05_wireshark_basics
* File:8-arp_scanning.txt

### Tasks list

* Mandatory
* Advanced


