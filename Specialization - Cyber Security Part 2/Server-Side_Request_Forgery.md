# Project: Server-Side Request Forgery

![Project Image](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/03/image-23.png?resize=768%2C532&ssl=1)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

PS: All App are Port forwarded pay attention to port when redirecting

## Resources

#### Read or watch:

* [Server Side Request Forgery](/rltoken/7KPd7MJ0D0b6t6QcTMAHxg)
* [Server-Side Request Forgery (SSRF)](/rltoken/FQyxRdzQQPBzkpKpMy5Ecg)
* [What is SSRF](/rltoken/g4FPJtviUBqJ1BtULH_fyw)
* [Find and Exploit Server-Side Request Forgery (SSRF)](/rltoken/37wVD_uhNLl4LwU3YQ__tA)
* [Exploiting Server Side Request Forgery (SSRF) in an API](/rltoken/7F744BAFTyfLtxqGMjk2fA)
* [SSRF Explained](/rltoken/iFEnAO1DAd45e6O226S0GA)
* [How to Defend Against Server-Side Request Forgery](/rltoken/seaeWBeAIYrr2KGlmdPOrw)

#### References:

* [SSRF](/rltoken/y-03CDmN1lHMEJUOyIZEcg)


## Learning Objectives

* What isSSRF?
* How DoesSSRFWork?
* What is anSSRFAttack and How Does it Work?
* What is the types ofSSRFAttacks?
* What is the impact of SSRF attacks?
* What Are the Risks ofSSRF?
* What Are Some CommonSSRFAttack Scenarios?
* How to Protect AgainstSSRFAttacks?
* How prevent theSSRFattacks?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetCyber - WebSec 0x08.


## Tasks

### 0. Unlocking security, one exploit at a time!



Shielding Shop Security..

Welcome to the gateway of Server-Side Request ForgerySSRF, where you’ll embark on a journey through the digital landscape of vulnerabilities, set against the backdrop of our meticulously designed shop website. Your mission commences with probing the foundational element ofSSRFvulnerabilities: uncovering potential gateways to unauthorized requests.

Before diving into the main challenge, let’s get you familiar withSSRFvulnerabilities.SSRFoccurs when an attacker can make the server perform requests to arbitrary destinations on their behalf, often exploiting how URLs and parameters are handled. By learning about SSRF, we can start to uncover hidden security risks in systems. Let’s dive into the world ofSSRFvulnerabilities and become experts at navigating the digital world.

Your mission is to test and secure our internal admin dashboard by identifying and exploiting potentialSSRFvulnerabilities.

Hints: Harness the power ofBurp Suiteto uncover SSRF vulnerabilities.

* Target Application:ShopAdmin
* Initial Endpoint:http://web0x08.hbtn/

```bash
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Param articleApi is vulnerable.
5. This App is Forwarded on Port 3000
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x08_ssrf
* File:0-flag.txt

### 1. Is our security a fortress or a sieve? Let's SSRF and find out!



Following a thorough pentest, security measures were implemented to address known vulnerabilities. What about now, is it secure?

It’s time to put our defenses to the test and see if they can weather the storm of cyber threats.
Your mission is to assess the effectiveness of these security enhancements and determine whether the system remains susceptible to SSRF attacks.

Even after adding mitigations, this stage remains focused on the SSRF vulnerability within the check reduction functionality. Let’s see if our enhancements are enough to secure the system

* Target Application:ShopAdmin
* Initial Endpoint:http://web0x08.hbtn/app2/

```bash
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Bypass the filter by providing decimal representation of the localhost.
5. This App is Forwarded on Port 3001
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x08_ssrf
* File:1-flag.txt

### 2. Exploit SSRF to breach our security!



We’ve been working on improving our security, and now it’s time to see how well it holds up. We’re especially focused on weaknesses that could allow unauthorized requests on the serverSSRFvulnerabilities. By putting our system through rigorous testing, we’ll identify any areas that need more protection. Let’s find the chinks in our armor before anyone else does!

It’s time to pentest our added security by probing the SSRF vulnerability.

This stage also focuses on the  SSRF vulnerability within the check reduction functionality. ThearticleApiparameter is vulnerable, and your goal is to exploit it to gain access to the internal admin dashboard.

* Target Application:ShopAdmin
* Initial Endpoint:http://web0x08.hbtn/app3/

```bash
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Param artcileApi is vulnerable.
5.  This App is Forwarded on Port 3002
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x08_ssrf
* File:2-flag.txt

### 3. New security layers in town! Let's break 'em in and see if they hold up!



Let’s see if our security makeover is more than just a fresh coat of paint! Time to poke some holes and find out!

This challenge focuses on the SSRF vulnerability within the check reduction functionality. Despite previous vulnerabilities, we’ve implemented new security measures. Now, it’s time to see if they’ve done the job.

Your mission is to test the new security layers: Attempt to exploit the SSRF vulnerability with the implementation of new security measures.

* Target Application:ShopAdmin
* Initial Endpoint:http://web0x08.hbtn/app4-1/

```bash
Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. Navigate to Check Reduction Functionality: Explore the feature where the articleApi parameter is utilized.
3. There is New Feature To Navigate Product Now Trying Exploiting The Redirection in That  Feature  
4. Try Using The New Feature  as refer in your payload to  Exploit The Vulnerability 
5. Pay Attention To Other API Call to Backend Services & Port
6. This App is Forwarded on Port 8080
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x08_ssrf
* File:3-flag.txt

### Tasks list

* Mandatory
* Advanced


