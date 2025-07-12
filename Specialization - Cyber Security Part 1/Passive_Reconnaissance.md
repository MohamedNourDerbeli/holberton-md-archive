# Project: Passive Reconnaissance

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/3Y9HL1CRUBULYUWT.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [What is passive reconnaissance ?](/rltoken/gEnQUgTg-S11fTMhq6jFFA)
* [WHOIS](/rltoken/hG2wg3tFATap5hiNKD-LUg)
* [What is DNS?](/rltoken/8MlwNqJkKMPbNKSswEWziA)
* [What is a DNS server?](/rltoken/NfBz5tAmOAVmkcsqQyP4tw)
* [How to Install and Use Subfinder?](/rltoken/vrL42dtLZO83F-9OY901iQ)

#### References

* [Unified Kill Chain](/rltoken/GqQyL1O3sg14GdmiM7xU2g)
* [RFC-3912](https://www.ietf.org/rfc/rfc3912.txt)
* [whois](/rltoken/6lGQN__W4X3m7y9XqdvzpQ)
* [dig](/rltoken/M4GtrEIs13yzu1lq3DssjQ)
* [dnslookup](/rltoken/RL-dKUOOwAwhyqy4mz_JMA)
* [shodan.io](/rltoken/W6H6PoxyfT89fU-3DLrYpA)
* [DNSDumpster](/rltoken/AftzWRfyddpXdrR6ramQLQ)
* [Google Hacking](/rltoken/CoioeSwhbwG78HulIc9n2w)


## Learning Objectives

* What can we learn about aServer
* What is aDNS server
* What happens when we typewww.holbertonschool.comand pressENTER
* How can we find the owner information for adomain name
* What isdig
* What isnslookup
* What are the different types ofDNS RECORDS
* What isDNS Dumpster
* What isShodan.io
* How can we findsubdomains
* What issubfinder
* What is the difference betweenActive reconnaissanceandPassive reconnaissance


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly two lines long ($ wc -l fileshould print 2)
* You must substitute the IP range for$1.
* All your files should end with a new line (Why?)
* The first line of all your files should be exactly#!/bin/bash.
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable
* Ensure that$1(or any other args) is used without quotes in your script to prevent unintended argument type alterations.


## Tasks

### 0. Who is it ?

Write a bash script that extract usingwhoisscan in csv format:

You are only allowed to useawkto format your output

* Registrant Information
* Admin Information
* Tech Information

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./0-whois.sh holbertonschool.com
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$  cat -e holbertonschool.com.csv | sed 's/ /$/g'
Registrant$Name,Holberton$Inc$
Registrant$Organization,Holberton$Inc$
Registrant$Street,5670$Wilshire$Blvd$suite$1802$
Registrant$City,Los$Angeles$
Registrant$State/Province,$
Registrant$Postal$Code,90036$
Registrant$Country,US$
Registrant$Phone,+1.4156227634$
Registrant$Phone$Ext:,$
Registrant$Fax,$
Registrant$Fax$Ext:,$
Registrant$Email,7da97d10931ddb501d08b8f88c7384bc-37846707@contact.gandi.net$
Admin$Name,Holberton$Inc$
Admin$Organization,Holberton$Inc$
Admin$Street,5670$Wilshire$Blvd$Suite$1802$
Admin$City,Los$Angeles$
Admin$State/Province,California$
Admin$Postal$Code,90036$
Admin$Country,US$
Admin$Phone,+1.4153580819$
Admin$Phone$Ext:,$
Admin$Fax,$
Admin$Fax$Ext:,$
Admin$Email,624a82de74a4fa2b64fb39bbe08b290d-37876671@contact.gandi.net$
Tech$Name,Holberton$Inc$
Tech$Organization,Holberton$Inc$
Tech$Street,5670$Wilshire$Blvd$Suite$1802$
Tech$City,Los$Angeles$
Tech$State/Province,California$
Tech$Postal$Code,90036$
Tech$Country,US$
Tech$Phone,+1.4153580819$
Tech$Phone$Ext:,$
Tech$Fax,$
Tech$Fax$Ext:,$
Tech$Email,2c420b43d982c37b7621f2015f3e107b-37876677@contact.gandi.net$
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:0-whois.sh

### 1. A record

Write a bash script that retrieve theA recordof a specified domain usingnslookupcommand:

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./1-a_record.sh holbertonschool.com
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   holbertonschool.com
Address: 75.2.70.75
Name:   holbertonschool.com
Address: 99.83.190.102
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:1-a_record.sh

### 2. MX Record

Write a bash script that retrieve theMX recordof a specified domain usingnslookupcommand:

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./2-mx_record.sh holbertonschool.com
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
holbertonschool.com     mail exchanger = 1 aspmx.l.google.com.
holbertonschool.com     mail exchanger = 10 alt3.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 10 alt4.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 5 alt1.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 5 alt2.aspmx.l.google.com.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:2-mx_record.sh

### 3. Check the TXT

Write a bash script that retrieve theTXT recordof a specified domain usingnslookupcommand:

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./3-txt_record.sh holbertonschool.com
;; Truncated, retrying in TCP mode.
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
holbertonschool.com     text = "1C8BC5F558"
holbertonschool.com     text = "MS=BB8A869E4E8A47D208F560DE7D83F199D1BB8F4F"
holbertonschool.com     text = "apple-domain-verification=sqTGlUgV9vVTnBuB"
holbertonschool.com     text = "dropbox-domain-verification=pvxn88z3e06i"
holbertonschool.com     text = "google-site-verification=lnffgexG_GGal6Fa53z0Ve4dJY4z4GXAmy1I2_ldotk"
holbertonschool.com     text = "intacct-esk=A3E9DCEA8FB6B747E0539A220D0A9719"
holbertonschool.com     text = "loaderio=67a0fbf5fb42755902d5415639d826a6"
holbertonschool.com     text = "v=spf1 include:mailgun.org include:_spf.google.com include:spf.exclaimer.net include:mail.zendesk.com include:servers.mcsv.net include:_spf.intacct.com ip4:104.209.35.28 ip4:191.237.4.149 ~all"
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:3-txt_record.sh

### 4. Dig it all !

Write a bash script that retrieveAll recordof a specified domain usingdigcommand:

Your output should contains answers only,noall

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./4-dig_all.sh holbertonschool.com
holbertonschool.com.    300     IN      A       99.83.190.102
holbertonschool.com.    300     IN      A       75.2.70.75
holbertonschool.com.    300     IN      NS      ns-1455.awsdns-53.org.
holbertonschool.com.    300     IN      NS      ns-1619.awsdns-10.co.uk.
holbertonschool.com.    300     IN      NS      ns-176.awsdns-22.com.
holbertonschool.com.    300     IN      NS      ns-792.awsdns-35.net.
holbertonschool.com.    300     IN      SOA     ns-1455.awsdns-53.org. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400
holbertonschool.com.    300     IN      MX      1 aspmx.l.google.com.
holbertonschool.com.    300     IN      MX      10 alt3.aspmx.l.google.com.
holbertonschool.com.    300     IN      MX      10 alt4.aspmx.l.google.com.
holbertonschool.com.    300     IN      MX      5 alt1.aspmx.l.google.com.
holbertonschool.com.    300     IN      MX      5 alt2.aspmx.l.google.com.
holbertonschool.com.    60      IN      TXT     "1C8BC5F558"
holbertonschool.com.    60      IN      TXT     "MS=BB8A869E4E8A47D208F560DE7D83F199D1BB8F4F"
holbertonschool.com.    60      IN      TXT     "apple-domain-verification=sqTGlUgV9vVTnBuB"
holbertonschool.com.    60      IN      TXT     "dropbox-domain-verification=pvxn88z3e06i"
holbertonschool.com.    60      IN      TXT     "google-site-verification=lnffgexG_GGal6Fa53z0Ve4dJY4z4GXAmy1I2_ldotk"
holbertonschool.com.    60      IN      TXT     "intacct-esk=A3E9DCEA8FB6B747E0539A220D0A9719"
holbertonschool.com.    60      IN      TXT     "loaderio=67a0fbf5fb42755902d5415639d826a6"
holbertonschool.com.    60      IN      TXT     "v=spf1 include:mailgun.org include:_spf.google.com include:spf.exclaimer.net include:mail.zendesk.com include:servers.mcsv.net include:_spf.intacct.com ip4:104.209.35.28 ip4:191.237.4.149 ~all"
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:4-dig_all.sh

### 5. Find the sub !

Write a bash script that fetch subdomains of given domain usingsubfindercommand:

* Show only subdomains in output
* Write output inHost,IPformat
* File to write output to<domain>.txt

```bash
┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ ./5-subfinder.sh holbertonschool.com
www.holbertonschool.com
yriry2.holbertonschool.com
read.holbertonschool.com
apply.holbertonschool.com
rails-assets.holbertonschool.com
staging-rails-assets-apply.holbertonschool.com
staging-apply-forum.holbertonschool.com
staging-apply.holbertonschool.com
apply-staging.holbertonschool.com
webflow.holbertonschool.com
blog.holbertonschool.com
support.holbertonschool.com
fr.holbertonschool.com
smile2021.holbertonschool.com
assets.holbertonschool.com
fr.webflow.holbertonschool.com
v3.holbertonschool.com
v2.holbertonschool.com
v1.holbertonschool.com
lvl2-discourse-staging.holbertonschool.com
beta.holbertonschool.com
hippokampoi.holbertonschool.com
holbertonschool.com
alpha.holbertonschool.com
en.fr.holbertonschool.com
blog-new.holbertonschool.com
help.holbertonschool.com
22support.holbertonschool.com

┌──(yosri㉿HBTN-LAB)-[~/holbertonschool-cyber_security/network_security/0x01_passive_reconnaissance]
└─$ cat holbertonschool.com.txt
fr.webflow.holbertonschool.com,151.139.128.10
en.fr.holbertonschool.com,151.139.128.10
alpha.holbertonschool.com,54.157.56.129
rails-assets.holbertonschool.com,52.85.96.82
read.holbertonschool.com,13.37.98.87
blog.holbertonschool.com,192.0.78.131
assets.holbertonschool.com,52.85.96.95
smile2021.holbertonschool.com,63.35.51.142
webflow.holbertonschool.com,63.35.51.142
v2.holbertonschool.com,34.203.198.145
holbertonschool.com,99.83.190.102
staging-apply-forum.holbertonschool.com,13.38.122.220
fr.holbertonschool.com,63.35.51.142
www.holbertonschool.com,63.35.51.142
v1.holbertonschool.com,54.86.136.129
lvl2-discourse-staging.holbertonschool.com,13.38.216.13
v3.holbertonschool.com,54.89.246.137
apply.holbertonschool.com,13.36.10.99
support.holbertonschool.com,104.16.53.111
yriry2.holbertonschool.com,52.47.143.83
help.holbertonschool.com,75.2.70.75
staging-apply.holbertonschool.com,35.180.20.42
staging-rails-assets-apply.holbertonschool.com,18.66.196.8
beta.holbertonschool.com,44.214.9.111
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:5-subfinder.sh

### 6. Search for us

For this task, we need you to gather as much information as possible about the holbertonschool.com domain usingShodan*:

* Collect all ip ranges within holbertonschool.com domaine
* Collect Technologies and frameworks used within all subdomains ofholbertonschool.com
* Write up your notes as a report in markdown format.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:holbertonschool_report.md

### 7. Catch The flag - TXT

Here we come to our first CTF within this module.\o/

For this challenge we are expecting you to:

Hints

* Target Domainpassive.hbtn
* Connect to the VPN server
* Get acyber_netsec_0x01Target Machine
* Use this <target IP> as a dns resolver withindigcommanddig @<target IP> passive.hbtn

* The flag is hidden withinTXTrecord

```bash
dig @<target IP> passive.hbtn
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:100-flag.txt

### 8. Catch The flag - NS

For this challenge we are expecting you to:

* Target Domainpassive.hbtn
* Connect to the VPN server
* Get acyber_netsec_0x01Target Machine
* Use this  <target IP> as a dns resolver withindigcommanddig @<target IP> passive.hbtnHints
* The flag is hidden withinTXTrecord
* Try to search withinnameserverdomains

```bash
dig @<target IP> passive.hbtn
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:101-flag.txt

### 9. Catch the flag - MX

For this challenge we are expecting you to:

Hints

* Target Domainpassive.hbtn
* Connect to the VPN server
* Get acyber_netsec_0x01Target Machine
* Use this <target IP> as a dns resolver withindigcommanddig @<target IP> passive.hbtn

* The flag is hidden withinTXT record
* Try to search withinmail serverdomains

```bash
dig @<target IP> passive.hbtn
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x01_passive_reconnaissance
* File:102-flag.txt

### Tasks list

* Mandatory
* Advanced


