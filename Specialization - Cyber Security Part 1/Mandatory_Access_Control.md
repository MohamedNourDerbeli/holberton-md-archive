# Project: Mandatory Access Control

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Introduction to Mandatory Access Control (MAC)](/rltoken/stbOwUkfkItdTPE_ikOcfA)
* [Your visual how-to guide for SELinux policy enforcement](/rltoken/oOoGfzp_9yFX-PV_qK67mg)
* [5 security technologies to know in Red Hat Enterprise Linux](/rltoken/1UsPey78rYXG0ZlG43Pcig)
* [AppArmor: An alternative to SELinux](/rltoken/CLuo9874Gb4E2Dji1YzWpg)
* [Linux Security: MAC, DAC, and RBAC](/rltoken/bCYFjICOFJh8XeHsohgcgA)
* [Security-Enhanced Linux for mere mortals](/rltoken/Gj4YkUCIT-4VPayYb1LwVA)
* [AppArmor vs SELinux: What’s the Difference?](/rltoken/s-ObHwA-z0qXTPolbvV0jg)
* [semanage Command with Examples](/rltoken/wMOJuPUSW-6V5qvFAckbzQ)

#### References:

* [National Institute of Standards and Technology (NIST) on MAC](/rltoken/oHufHmV7azJuBy3HEBwKAQ)
* [SELinux](/rltoken/6STMdb_lGdqjqpyBOujEVw)
* [SELinux Project Wiki](/rltoken/8HNXxRGZLCYnTDDxwwuaLQ)
* [AppArmor Project Wiki](/rltoken/eKXkKT0sPUUi-mHVySzAJw)
* [CentOS Documentation on SELinux](/rltoken/zBAHmmU9xipu3Ugrrdu7Zg)
* [Arch Linux Wiki on Security](/rltoken/WYWkteADEob-FNJlZXRDgw)
* [Linux Kernel Capabilities and MAC](/rltoken/OBODJToIqeaWs4zKIHCaCA)
* [semanage](/rltoken/wJY9RXmcaejENn6sLgSL2g)


## Learning Objectives

* What isMACin Linux?
* How does SELinux enforce MAC?
* What are the differences between SELinux and AppArmor?
* What is the purpose ofpolicyin MAC systems?
* How do labels work in SELinux?
* What areType Enforcement,Role-Based Access Control, andMulti-Level Securityin SELinux?
* How can you check the status of SELinux on a system?
* What are common SELinux management commands?
* How do you set file contexts in SELinux?
* What is anAppArmor profile?
* How do you reload AppArmor profiles?
* What is the concept ofleast privilegein MAC?
* How do you troubleshoot SELinux issues?
* What is the significance ofaudit logsin MAC systems?
* Can you explain the concept ofcapabilitiesin Linux security?
* How to use semanage


## Requirements

### General

* All your files will be run onKali Linux 2023.2
* Allowed editors:vi,vim,emacs
* You must substitute the IP range for$1.
* The first line of all your files should be exactly#!/bin/bash.
* All your files should end with a new line.
* All your scripts should be 2 lines long$ wc -l fileshould print 2.
* Not allowed to useprintf
* You are not allowed to use backticks,&&,||or;.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl


