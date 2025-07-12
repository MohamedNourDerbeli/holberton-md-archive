# Project: Insecure Direct Object Reference

![Project Image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*_FH1ngj9OF4jc6O7FJQUpQ.jpeg)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Insecure direct object references (IDOR)](/rltoken/koZpdwLFrtFDhb8IImLbKA)
* [All About Insecure Direct Object Reference(IDOR)](/rltoken/t6y-NIfrOmVRyxeF3CWzfg)
* [Insecure Direct Object Reference (IDOR) Explained](/rltoken/kkP2tVvwmSOwjmyvKdT_-w)
* [IDOR ? Ok but what is it finally ?](/rltoken/2oJLAb587cNyXeVko6n-7Q)
* [OWASP TOP 10: Insecure Direct Object Reference](/rltoken/lQ9XT_Abublrf_UMJtiyVg)
* [Insecure Direct Object Reference (IDOR) - A Deep Dive](/rltoken/KkZk04wJs0RTWCLguRU1eg)
* [Everything You Need to Know About IDOR](/rltoken/Q3xq8cJOxNfjrcJqau-y-A)
* [Types of IDOR](/rltoken/KQgbPOYaqFWm29nH0_NYEA)
* [How to find more IDORs](/rltoken/PavnNCkeTZuXZCMtZqen5Q)
* [IDOR Mitigation Best Practices](/rltoken/AjUxfvad3wRrxGeZke70MQ)

#### References:

* [IDOR](/rltoken/koZpdwLFrtFDhb8IImLbKA)
* [Testing for IDOR](/rltoken/nMIOu54fhEyElsucU0Vqtg)
* [Cheat Sheet](/rltoken/HAE5k1H4C9csbc1Zxzn7gg)


## Learning Objectives

* What is anIDOR?
* What does insecure direct object reference mean?
* HowIDORworks?
* What is the difference betweenIDORand other vulnerabilities?
* How anIDORAttack Happens?
* What are the types ofIDOR?
* What is the impact ofIDOR?
* How to detectIDORvulnerabilities?
* How to preventIDORattacks?
* What are theIDORMitigation Best Practices?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetCyber - WebSec 0x06.


## Tasks

### 0. Uncovering User IDs



Warmning up..

Welcome to the first step in your journey through the realm of Insecure Direct Object References (IDOR), set against the backdrop of a carefully craftedbanking application.Your mission begins with the foundational element of many IDOR vulnerabilities: discovering otherusers’ IDs.

Understanding how user IDs are structured, assigned, and exposed can provide you with the initial foothold required to explore deeper vulnerabilities within the application.Let’s dive in.

* Target Application:CyberBank
* Initial Endpoint:http://web0x06.hbtn/dashboard

```bash
Useful instructions:
1. Log into CyberBank using provided credentials and start exploring features, paying close attention to any mention or use of user IDs.
2. Observe the URL structure, page content, and any API requests for patterns in how user IDs are displayed or transmitted.
3. Investigate other areas of the application where user-specific actions occur (e.g., transaction history, settings) for additional exposure of user IDs.
4. Experiment with altering user ID values in URLs or requests to access information pertaining to other users.
5. Within the info of a target user, identify and note down a unique flag as proof of successfully uncovering user IDs.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x06_idor
* File:0-flag.txt

### 1. Enumerating Account Numbers for Balance Disclosure



Having successfully identifieduser IDsin the previous task, your next challenge in the CyberBank environment is focused on account numbers.

Specifically, you will leveragethe user IDsobtained to enumerate account numbers and subsequently disclose account balances.This stage underscores the potential depth of IDOR vulnerabilities in financial applications.

* Target Application:CyberBank
* Relevant Endpoint:http://web0x06.hbtn/dashboard

```bash
Useful instructions:
1. Utilize the user ID(s) discovered in Task 1 to explore areas of the application where user account numbers might be displayed or referenced.
2. Pay attention to transaction history, fund transfer features, or profile/account settings that might reveal account numbers associated with the user IDs.
3. Once you have an account number, craft a request to the `/accounts/` API  endpoint, incorporating the account number to retrieve the balance information.
4. Experiment with modifying request parameters or paths using different account numbers to assess the application's response and to check for unauthorized access to account balances.
5. In the account balance information of a target account, look for a unique flag as evidence of successful enumeration and access.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x06_idor
* File:1-flag.txt

### 2. Manipulating Wire Transfers to Inflate Account Balance

After uncovering user IDs and account numbers, leading to the disclosure of account balances, your journey through the CyberBank simulation progresses to exploiting wire transfer functionalities.This task demands a keen understanding of how theapplication processes transactions.You’re tasked with manipulating wire transfer requests to artificially inflate your account balance beyond$ 10K.Achieving this milestone will trigger a uniqueFlag⛳️ as proof of your advanced exploitation capabilities.

* Target Application:CyberBank
* Wire Transfer Endpoint:http://web0x06.hbtn/dashboard

```bash
Useful instructions:
1. Review the functionality of the wire transfer feature within CyberBank, taking note of how transactions are initiated, especially the parameters required (e.g., source account, destination account, amount).
2. Begin with smaller transactions to understand the application's validation checks and response behaviors, such as how it handles negative amounts or transfers between accounts you control.
3. Incrementally adjust the transaction amount, or experiment with other parameters like source and destination accounts, to identify any possible oversight in the transaction processing logic.
4. Your goal is to perform valid transactions that cumulatively increase your account balance over 10k. Pay attention to transaction limits, rate limiting, or other security controls that might prevent rapid or large transactions.
5. Once your balance exceeds 10k, observe the application's response for the appearance of a `Flag`, indicating successful exploitation of the wire transfer functionality.

Remember:
- Your actions within this simulation are for educational purposes. Applying these techniques in real-world scenarios without authorization is illegal and unethical.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x06_idor
* File:2-flag.txt

### 3. Bypassing 3D Secure Verification for Unauthorized Payment



In this culminating interactive challenge within theCyberBank simulation,you’re tasked with executing a payment transaction using another account holder’s details while cleverly diverting the3D Secure verificationto your account.This advanced task simulates an attack vector targeting the payment authorization process, specifically the 3D Secure verification mechanism designed to add an extra layer of security for online credit and debit card transactions.This tasks sound crazy I know, just take your time with a deep breath.To understand the logic behind the payment flow, try anormal paymentwith your account information.

* Target Application:CyberBank
* Payment Endpoint:http://web0x06.hbtn/upgrade
* OTP Confirmation Endpointhttp://web0x06.hbtn/confirmation

```bash
Useful instructions:
1. Initiate a payment transaction on the `/upgrade` page using the account details of another holder but ensure the transaction amount is within legitimate bounds to avoid immediate flags by fraud detection systems.
2. When redirected to the 3D Secure verification page (`/cards/3dsecure/`), carefully observe the request made when submitting the OTP (One-Time Password).
3. Intercept and modify this OTP submission request in a way that the verification appears to be from your account, but ensure the charge is still made to the other account holder's account.
4. Consider manipulating parameters within the request, such as session identifiers or account numbers, to redirect the verification process successfully.
5. Achieving successful verification under these altered conditions will trigger a transaction completion message along with a unique `Flag` as evidence of exploiting the 3D Secure process.

Remember:
- This simulation is designed to enhance your understanding of financial web application vulnerabilities and should only be applied in ethical, authorized testing environments.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x06_idor
* File:3-flag.txt

### 4. Crafting a Comprehensive Vulnerability Report

After navigating the complexities ofIDORvulnerabilities within the CyberBank simulation, your final task is to compile and present your findings ina detailed vulnerability report.This report should not only recount the vulnerabilities you’ve directly encountered during the project tasks but also include any additional security flaws discovered through your exploration.The goal is to createa documentthat could realistically be presented to a financial institution to help them understand and remediate the identified vulnerabilities.

Your report should be structured and detailed, adhering to professional standards. Consider using a Google Doc for its collaborative features and accessibility. Here are key elements to include:

**Repo Info:**
### Tasks list

* Mandatory
* Advanced


