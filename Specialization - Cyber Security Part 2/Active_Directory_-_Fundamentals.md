# Project: Active Directory - Fundamentals

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

Needed ISOS:

Note: You must create two virtual machines in the same network one will be a user machine and
the other will be the domain controller

## Resources

#### Read or watch:

* [What is Active Directory and how does it work?](/rltoken/IZojc0iSIFYqjaxc4Dlk0A)
* [What is an Active Directory Domain?](/rltoken/oSAKafbkPHL5BWvdcERJgQ)
* [What are the Benefits of Using Active Directory?](/rltoken/E8_k7yKSLl1nypb5NLEUtg)
* [Active Directory Prerequisites.](/rltoken/Yb6hTImQyjjvjiQP4ZQ5QA)
* [how to create test users, group and organizational uni?](/rltoken/JPxjB1Er5gAxzZzCC6DFAQ)


## Learning Objectives

* What isActive Directory?
* What isAuthorization?
* What isAuthentication?
* What isDomain Controllers?
* What isDomains?
* What isLDAP?


## Tasks

### 0. initial Setup

Perform the initial Setup of the domain controller on a server. This involves using the Server Manager to add the Active Directory Domain Services role.

**Repo Info:**
### 1. Post-Setup Configuration of the Domain Controller

Complete the post-Setup   configuration for the newly installed domain controller by promoting the server and setting up a new forest.

* Domain Name Should BeHOLBERTON.local
* Password :P@$$w0rd!

**Repo Info:**
### 2. Configuring Active Directory Users, Groups

Set up users, groups, and policies in Active Directory on a Windows 10 Enterprise machine. This involves creating organizational units, users, and configuring file shares.

PS: keep everything in default if not mentioned

That would be for setting spn it will be needed to set Kerberoasting attack later

* Install Windows 10 Enterprise
* Create Organizational Units inHOLBERTON.localcalledGroups
* Create New Userholbertonuser1
* Create Domain Admin
* Create Additional Users ExampleSQLService
* Configure File Shares  On the Server Management
* Name the share,hackme
* Set Service Principal Name (SPN) To Be The Following

```bash
Holberton-DC/SQLService.HOLBERTON.local:60111 HOLBERTON\SQLService
```

**Repo Info:**
### 3. Setting Up Group Policies

Create and configure Group Policies to disable Windows Defender Antivirus on all machines within the HOLBERTON.local domain.

This configuration will ensure that Windows Defender Antivirus is disabled on all computers within the HOLBERTON.local domain.

* Name the new GPODisabled Windows Defender.
* Don’t forget to Enforce the GPO

**Repo Info:**
### 4. Joining Users to Domain

Join a user machine to the HOLBERTON.local domain and set up a user as a local administrator.

Requirements :

This process ensures the user machine is joined to the HOLBERTON.local domain and that the user HolbertonUser1 is set up as a local administrator on the machine.

* Create a Shared Folder inC:\calledShared
* Configure Network Settings
* Join the DomainHOLBERTON.local
* Log In Using administrator Admin
* Set Up a Local Administrator usingHolbertonUser1

**Repo Info:**
### Tasks list

* Mandatory
* Advanced


