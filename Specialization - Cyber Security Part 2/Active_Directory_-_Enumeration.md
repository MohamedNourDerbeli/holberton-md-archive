# Project: Active Directory - Enumeration

## Description

At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

Needed ISOS:

Note: You must create two virtual machines in the same network one will be a user machine and
the other will be the domain controller

## Resources

#### Read or watch:

* [Active Directory Methodology - HackTricks](/rltoken/pv-i_2KGBHEvCdQsH0qJ6g)
* [Active Directory: Designing, Deploying, and Running Active Directory by Brian Desmond](/rltoken/kONsTEc4t0-4qb7O8qhaTw)
* [Active Directory Security Deep-dive](/rltoken/qESHX-x8blfIffE8JWmEzA)
* [Red Teaming Active Directory](/rltoken/vUeC2Jl0q6ApzN4eD_iyAA)
* [Active Directory Enumeration](/rltoken/VcwHG-DtFy3-2vCmdpA3zg)
* [Enumerating Active Directory: A Comprehensive Guide](/rltoken/8JC6if0KmPBjWtNa9S3X-w)


## Learning Objectives

* Grasp why AD enumeration is crucial for both administrators and attackers.
* Acquire skills in using various tools and methods to extract information from AD, such as LDAP queries, built-in Windows commands, PowerShell scripts, and third-party tools.
* Recognize how information gathered through enumeration can be used to strengthen security or exploit weaknesses.
* Develop the ability to enumerate users, groups, computers, domain controllers, trusts, policies, and permissions within AD.
* Understand how to interpret the data obtained from these enumeration activities.
* Learn to identify potential security vulnerabilities and misconfigurations within AD environments.
* Enhance your ability to detect suspicious activities and potential attacks on AD environments through enumeration data.


## Tasks

### 0. IP Addresses

Objective

What are the IP addresses of the user machine and the domain controller?

Provide a screenshot of your Nmap scan results showing the discovered IP addresses. Along With The Command

* Enumerate the Active Directory environment using Nmap.
* Identify the IP addresses of the user machine and the domain controller.
* Detect any potential security vulnerabilities and associated attacks.
* List the services running on the domain controller and their ports.

**Repo Info:**
### 1. SMB Relay Attack

Is there anything strange about the user machine?
What potential attack could this lead to ?

Provide a screenshot of the Nmap scan results showing the relevant information.

```bash
Hint: Check the SMB configuration.
```

**Repo Info:**
### 2. Domain Controller

What are the services running on the domain controller and their ports?

Provide a list of the services and their corresponding ports.

Provide a screenshot of your Nmap scan results showing the services.

**Repo Info:**
### 3. User Machine

What are the services running on the user machine and their ports?

Provide a list of the services and their corresponding ports.

Provide a screenshot of your Nmap scan results showing the services.

**Repo Info:**
### 4. Enumerate Domain Admins

Use BloodHound to find the list of Domain Admins in the Active Directory.

Provide the names of the Domain Admin accounts

**Repo Info:**
### 5. Identify Users with Delegated Privileges

Identify and list all users who have delegated privileges on the

domain. What specific permissions do they have?

**Repo Info:**
### 6. Shortest Path to Domain Admin

Determine the shortest path to a Domain Admin account from a given user account (e.g., the one they are using).

What are the steps involved?

**Repo Info:**
### 7. Identify Computers with Unconstrained Delegation

Find all computers in the domain that have unconstrained delegation
enabled.

Why is this a potential security risk?

**Repo Info:**
### 8. Analyze Kerberoastable Users

Identify and list users that are susceptible to Kerberoasting attacks.

What service principal names (SPNs) are associated with these accounts?

**Repo Info:**
### 9. Enumerating Active Directory using Various Tools

* Use a domain user for this exercise.
* Install or verify the availability of the following tools on thestudentsmachines:ldapsearch(available in many LDAP toolkits)CrackMapExecdsquery(available on Windows systems)
* ldapsearch(available in many LDAP toolkits)
* CrackMapExec
* dsquery(available on Windows systems)
* We have the credentials from our previous lab (after cracking the password)We will use those credentials above to answer the question about bloodhound.
* We will use those credentials above to answer the question about bloodhound.

* What are the rights acquired by this service?
* What are the ways to get access to the Domain Controller?

**Repo Info:**
### 10. Find Domain Controllers with ldapsearch

Use ldapsearch to find the domain controllers in the Active Directory environment.

* We notice that one of the users/services has made a mistake by publicly setting a sensitive information.
* Should extract it and list the names and IP addresses of the domain controllers from the output

**Repo Info:**
### 11. Enumerate SMB Shares using CrackMapExec

Use CrackMapExec to enumerate SMB shares on a specified domain controller.

For this task, we will use smbclient tool

* What shares are available, and what permissions are associated with them ?
* What is the content of the file in the share for privileged users ?
* Should list the shares and their associated permissions.

**Repo Info:**
### Tasks list

* Mandatory
* Advanced


