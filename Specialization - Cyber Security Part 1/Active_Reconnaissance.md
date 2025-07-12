# Project: Active Reconnaissance

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/FRQ15B48W19YVNRB.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [What is a ping?](/rltoken/d52-3EwIDd6rsLreRUDkAg)
* [What does Traceroute Do?](/rltoken/i9PRL7EfBf5Y8HYWqpwEbA)
* [Top 8 Nmap Commands](/rltoken/TAFHoY9NJiMmZ2ZoCv6fOw)
* [How Hackers Use Reconnaissance ?](/rltoken/WPo2FG4foyflu9MQAFCI_A)
* [SQLMap cheat sheet](/rltoken/JErfIcKNjTTYGlM3y96v3w)

#### References:

* [ping](/rltoken/gPZGlU51fEKxk4xGtitgqw)
* [traceroute](/rltoken/WYEYt2M9BPhojYScWcbCMg)
* [telnet](/rltoken/CdSukjxMS_VjO3RH3_VTlQ)
* [netcat](/rltoken/ucplzIMi02FuhUyHDgS9FA)
* [Wappalyzer](/rltoken/E9_SXWeHi-bgq_K_inXnHg)


## Learning Objectives

* What isactive reconnaissance?
* Why isactive reconnaissanceit important for cyber security?
* How canWappalyzerbe used for active reconnaissance?
* What isDNS enumeration?
* How to enumerateSMTPs using command-line tools?
* How should we performOS fingerprinting?
* What issqlmap? How to use it ?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetcyber_netsec_0x02.


## Tasks

### 0.  Are there any opened Ports ?

In this project, tasks are arranged in a sequential manner to help you understand the basic principles of hacking and develop a logical approach to performing actions



For this task we need you to:

* Connect to the VPN server
* Get Target Machine ->cyber_netsec_0x02
* App
* Endpoint:http://active.hbtn
* Scan that Machine top ports usingnmap.
* echo "<openport>, <openport>" > 0-ports.txt

```bash
echo "<openport>, <openport>" > 0-ports.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:0-ports.txt

### 1.  Inspect the runner



For this task we need you to:

* Edit/etc/hoststo pointactive.hbtndomain name to theTarget IP.sudo bash -c 'echo "<target_ip>    active.hbtn" >> /etc/hosts'
* Inspect the found website.
* UsingWappalyzer, check forwebservername and versionecho "<webservername> <webserverversion>" > 1-webserver.txt
* App
* Endpoint:http://active.hbtn

```bash
sudo bash -c 'echo "<target_ip>    active.hbtn" >> /etc/hosts'
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:1-webserver.txt

### 2.  Nothing defeat Manual inspection



For this challenge we need you to:

Hints

* Browseactive.hbtn
* Search for the first flag.
* echo "<FLAG_1>" > 100-flag.txt

* Some Developer forgets comments in production.
* App
* Endpoint:http://active.hbtn

```bash
echo "<FLAG_1>" > 100-flag.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:100-flag.txt

### 3.  Trypanophobia

For this task we need you to:

Don’t include params

Example: http://active.hbtn/orders/1511515



* Search for vulnerable page.
* echo "/<pathname>" > 2-injectable.txt

* App
* Endpoint:http://active.hbtn

```bash
echo "/<pathname>" > 2-injectable.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:2-injectable.txt

### 4.  SQLmap is an army \o/

Here we are at our first SQL Injection test

For this task we need you to:

Hints

* Find the mainDatabasename.echo "<database_name>" > 3-database.txt
* Check how manyTablesit does containecho "<tables_count>" > 4-tables.txt

* You need to usesqlmap
* --dbsto fetch databases names
* -D <database_name> --tablesTo fetch tables names
* App
* Endpoint:http://active.hbtn

```bash
echo "<database_name>" > 3-database.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:3-database.txt, 4-tables.txt

### 5.  Injections hurt :')



For this challenge we need you to:

Hints

* Search for the second flag.
* echo "<FLAG_2>" > 101-flag.txt

* -D <database_name> --dumpto dump the database.
* Check for theUserstable
* Flag is exposed clearly inactive.hbtn
* App
* Endpoint:http://active.hbtn

```bash
echo "<FLAG_2>" > 101-flag.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:101-flag.txt

### 6.  My NAV doesn't include all my pages



For this task we need you to:

Hints

* Find the admin panel login page.echo "/<pathname>" > 5-hidden_dir.txt

* You need to usegobusterwithdiroption
* -b 302to ignore 302 status code.
* -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txtfor the wordlist
* App
* Endpoint:http://active.hbtn

```bash
echo "/<pathname>" > 5-hidden_dir.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:5-hidden_dir.txt

### 7.  It may look the same, but it’s not

For this challenge we need you to:

Hints

* Search for the third flag.
* echo "<FLAG_3>" > 102-flag.txt

* Flag is exposed clearly inactive.hbtnatAdminpanel
* App
* Endpoint:http://active.hbtn

```bash
echo "<FLAG_3>" > 102-flag.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:network_security/0x02_active_reconnaissance
* File:102-flag.txt

### Tasks list

* Mandatory
* Advanced


