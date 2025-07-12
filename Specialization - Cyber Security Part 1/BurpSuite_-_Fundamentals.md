# Project: BurpSuite - Fundamentals

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/7TBPVHGMTL1C13U1.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Burp Suite Tutorial for Beginners](/rltoken/XL_7C1TMgT6rneQf5Kye6Q)
* [Getting Started with Burp Suite](/rltoken/l93Dx35egkoGu2qu2QUiNw)
* [Using Burp to Test for the OWASP Top Ten](/rltoken/hbMoBwo9qYGWEPbVpzeiHA)
* [How to Use Burp Suite - A Beginners Guide](/rltoken/Vtw0bgASHbaokm54ImaGFQ)
* [How to Use Burp Suite to Audit Web Application](/rltoken/kIzdTu2cqSUxBzi_-52IIA)

#### References:

* [Official Burp Suite Documentation](/rltoken/jBUbIiaItSl2HdeYKDG6Mg)
* [OWASP Testing Guide](/rltoken/s_W-kF8Eb_qcc9xjXEZSBw)
* [Testing for SQL Injection with Burp Suite](/rltoken/0xiI18dZIPe9MB7-PMu6nQ)
* [Burp Suite as a Web Vulnerability Scanner](/rltoken/JPRQFYDV9KdBQKxRIMRafg)


## Learning Objectives

* What isBurp Suite?
* How do you set up a proxy inBurp Suite?
* What areBurp Suite‘s main components?
* How doesSpiderwork inBurp Suite?
* What is the purpose ofRepeaterinBurp Suite?
* How canIntruderbe used for attacks?
* What isBurp Scannerand when to use it?
* How to interpret results fromBurp Suite?
* What are some common issues thatBurp Suitecan identify?
* How do you configureBurp Suitefor HTTPS traffic?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targethttps://web0x02.hbtn.


## Tasks

### 0.  Getting Started with Burp Suite

Burp Suite stands as a cornerstone tool in web application security testing, offering a vast array of features tailored for security professionals and ethical hackers.Your first mission is to get Burp Suite up and running, configure it for web traffic interception, and uncover hidden data within TLS certificate details.

Step 1: Downloading and Installing Burp Suite

Step 2: Starting up BurpSuite

Step 3: DNS Resolution Configuration

Step 4: Discovering theFLAG

* Download Burp Suite Community Edition from the officialPortSwigger website.
* Follow the installation instructions for your operating system to install Burp Suite.
* Launch Burp Suite and familiarize yourself with the initial setup screens.

* Method 1: Proxy Setup and Certificate InstallationUpon opening Burp Suite, start a new project and navigate to theProxy->Optionstab.Set the Burp Suite proxy to listen on127.0.0.1:8080or another port of your choice.Configure your preferred web browser to route traffic through the Burp proxy by setting the HTTP proxy to127.0.0.1with the port you selected.With your browser configured, attempt to navigate to any HTTPS website. You’ll be blocked by a security warning due to the browser not recognizing Burp’s certificate.Return to Burp Suite and navigate toProxy->Intercept. EnsureIntercept is off. Accesshttp://burpsuitefrom your browser to download the CA certificate provided by Burp.Install this certificate in your browser’s certificate store to avoid further security warnings.
* Upon opening Burp Suite, start a new project and navigate to theProxy->Optionstab.
* Set the Burp Suite proxy to listen on127.0.0.1:8080or another port of your choice.
* Configure your preferred web browser to route traffic through the Burp proxy by setting the HTTP proxy to127.0.0.1with the port you selected.
* With your browser configured, attempt to navigate to any HTTPS website. You’ll be blocked by a security warning due to the browser not recognizing Burp’s certificate.
* Return to Burp Suite and navigate toProxy->Intercept. EnsureIntercept is off. Accesshttp://burpsuitefrom your browser to download the CA certificate provided by Burp.
* Install this certificate in your browser’s certificate store to avoid further security warnings.
* Method 2: Open BrowserNavigate toProxyTab.Click onOpen BrowserButton.
* Navigate toProxyTab.
* Click onOpen BrowserButton.

* Navigate toProject options->Connectionsin Burp Suite and find the section titledHostname Resolution Overrides.
* Add a new record with the hostnameweb0x02.hbtnand the IP address provided by your container or virtual lab environment.

* Ensure your configured browser’s proxy settings are directing traffic through Burp Suite.
* Visithttps://web0x02.hbtn, allowing Burp Suite to intercept the request.
* After successfully accessing the site, navigate toProject options->TLSin Burp Suite, then toServer TLS Certificate.
* Carefully examine the server certificate details presented by Burp Suite, looking for aFlagencapsulated within.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:0-flag.txt

### 1.  Client-Side TLS Authentication with Burp Suite

This task involves navigating client-side TLS authentication—a critical aspect of ensuring secure connections between clients and servers.Upon accessinghttps://web0x02.hbtn, you’ll encounter a welcome screen offering a download link for a.p12certificate.Your mission is to correctly install this certificate within Burp Suite to authenticate and reveal hidden content guarded by TLS client authentication.

Step 1: Downloading the PKCS#12 Certificate

Step 2: Configuring Burp Suite with Client TLS Certificate

Step 3: Reloading the Page to Reveal Hidden Content

* Visithttps://web0x02.hbtnthrough your browser configured to use Burp Suite as its proxy.
* On the welcome screen, download the.p12certificate provided via the download link.
(Or Simply through:https://web0x02.hbtn/static/web0x012.p12)

* With the.p12certificate downloaded, open Burp Suite and navigate toProxy->Options.
* Scroll down to theTLSsection, then click onClient TLS Certificate.
* Ensure the “Override options” checkbox is selected.
* Click onAddto configure a new client certificate.
* In theDestination Hostfield, enterweb0x02.hbtn.
* ForCertificate Type, choose “PKCS#12” from the dropdown menu.
* ClickSelect fileand browse to the location where you saved the downloaded.p12certificate.
* When prompted for a password, enterholberton, which is the password for the certificate.

* After successfully configuring the client TLS certificate in Burp Suite, revisithttps://web0x02.hbtnin your browser.
* If everything is configured correctly, upon reloading, you should bypass the initial welcome screen and gain access to a new page—a direct result of successful client-side TLS authentication.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:1-flag.txt

### 2.  Modifying Page Responses to Reveal Hidden Information

In this task, you will delve deeper into the functionalities of Burp Suite, particularly focusing on manipulating web server responses.By intercepting and altering responses, you’ll learn how to modify web page content in real-time.Your objective is to reveal a hiddenFlag⛳️ on the/task2page by spoofing the frontend through response modification.

Step 1: Intercepting the Download Request

Step 2: Modifying the Server Response

Step 3: Revealing the Flag

* Ensure Burp Suite is configured correctly with your browser’s proxy settings.
* Visit/task2or click the “Continue” button from the previous task’s page to navigate there.
* In Burp Suite, make sureIntercept is Onin theProxy->Intercepttab.
* On the/task2page, click the “Download” button. Burp Suite should capture the outbound request to the web server.

* With the request captured, click onActionin Burp Suite, then chooseDo intercept->Response to this request.
* Click onIntercept is onto toggle it off, allowing you to modify the intercepted response.
* In the response body, edit the content to reveal or unhide theFlag.
This might involve modifying JSON while maintaining format integrity.
* Once you’ve made your modifications, clickForwardto send the altered response to your browser.

* After forwarding the modified response if needed value aFLAGwill reveal!

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:2-flag.txt

### 3.  Exploring the Repeater Tool

Burp Suite’s Repeater tool is pivotal for testing and tweaking requests without repeatedly interacting with the web application itself.Your objective in this task is to utilize Repeater to guess login credentials on a page designed to mimic a router’s login portal.By examining the request details and making educated adjustments, you’ll aim to gain unauthorized access and uncover a hiddenFlag⛳️.

Step 1: Capturing the Login Request

Step 2: Guessing Credentials with Repeater

Step 3: Uncovering the Flag

* Navigate to/task3or continue from the previous task’s page by clicking the “Continue” button.
* Ensure thatIntercept is Onin Burp Suite’sProxy->Intercepttab.
* On the/task3page, click the designated button to initiate a login request. Once the request is captured in Burp Suite, use the shortcutCtrl + R(or right-click and selectSend to Repeater) to send it to the Repeater tool.

* In the Repeater tab, you’ll see the captured login request ready for modification. Based on the hint that the page uses default router credentials, attempt common combinations likeadmin/admin,admin/password, or similar.
* Pay attention to other fields in the request, such asroleandremember meoptions. Altering these values could impact the server’s response and might be necessary for successful authentication.

* Continue tweaking and resending your request as needed based on server responses until you successfully authenticate.
* A successful login will reveal a success message along with a hiddenFlag.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:3-flag.txt

### 4.  The Intruder's Path to Hidden Profiles

Burp Suite’s Intruder tool is engineered for automating customized attacks against web applications.This task will have you utilize Intruder to discover hidden user profiles by automating requests with varying parameters.Your mission is to find a specific profile ID that reveals a hiddenFlag⛳️ by systematically testing different ID values.

Step 1: Capturing the Request

Step 2: Setting Up and Executing an Intruder Attack

Step 3: Identifying the Correct Profile ID

Step 4: Retrieving the Flag

* Navigate to/task4or proceed by clicking the “Continue” button from the previous task’s page.
* EnsureIntercept is Onin Burp Suite’sProxy->Intercepttab.
* Click the “Refresh” button on the/task4page to generate a request. Once captured, send it to Intruder by pressingCtrl + Ior manually via the context menu.

* Within the Intruder tab, go to the “Positions” section. Here, you’ll find the captured request ready for modification.
* Identify and highlight the profile ID parameter in the request. Click “Add” to set this parameter as the point of attack.
* Switch to the “Payloads” tab. Select “Numbers” as the payload type.
* Paste the copied ID into the “From” field. Add 100 or 200 to this value and enter the result into the “To” field, setting a range for Intruder to test.
* Start the attack by clicking on the “Start attack” button and observe the responses from the server.

* Monitor the attack’s progress and results, looking for responses with a status code of 200, indicating successful access to a profile.
* Once you find a profile ID that yields a 200 response, note this ID (this profile bio contains theFLAG). It signifies access to a hidden or non-public user profile.

* Return to the original intercepted request in theProxy->Intercepttab.
* Replace the profile ID in the request with the ID discovered during your Intruder attack.
* Forward the modified request and then turn off Intercept.
* The response should now render a hidden user profile page, unveiling the sought-afterFlag.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:4-flag.txt

### 5.  Deciphering Tokens with Sequencer

Burp Suite’s Sequencer tool is designed for testing the randomness of session tokens, cookies, and other critical data that should be unpredictable and resistant to guessing attacks.In this exercise, you’ll use Sequencer to analyze a specific cookie,hijack_session, to uncover patterns or weaknesses in how it’s generated.Ultimately, your analysis will lead you to a valid session cookie that reveals a hiddenFlag⛳️.

Step 1: Capturing the Request

Step 2: Preparing for Sequencer Analysis

Step 3: Configuring and Starting Sequencer

Step 4: Analyzing Token Pattern and Hijacking Session

Step 5: Revealing the Flag

* Navigate to/task5or continue from the previous task’s page by clicking the “Continue” button.
* Make sureIntercept is Onin Burp Suite’sProxy->Intercepttab.
* Once the page loads, capture this initial request and send it to the Repeater by pressingCtrl + Ror through the context menu.

* In the Repeater tab, locate theCookieheader and remove thehijack_sessionvalue from the request.
* Right-click on the modified request and select “Send to Sequencer.”

* In the Sequencer tab, ensure the tool detects thehijack_sessionparameter for analysis.
* Before starting the live capture, enter Sequencer settings and adjust the “Throttle between requests (ms)” to 25 to regulate the pace of token generation without overwhelming the server.
* Close the settings and initiate the live capture of tokens. Aim to generate around 200 tokens before halting the capture.

* After stopping the capture, export or copy the tokens into your preferred text editor for analysis.
* Review the sequence of tokens to identify any discernible patterns or anomalies, such as skipped or repeating values.
* Locate a skipped cookie value—this represents a valid session that can be exploited.
* Replace your current session cookie in the browser (using developer tools or a cookie management extension) with the identified validhijack_sessionvalue.

* With the valid session cookie set, reload/task5in your browser.
* Interact with any newly accessible features or content on the page (e.g., scratching a card) to uncover the hiddenFlag.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:5-flag.txt

### 6.  `Decoder` Tab - Manipulating Base64 Encoded Bearer Tokens

In the final task of this series, you’ll delve into the intricacies of Bearer Token manipulation.By intercepting a request that includes a Bearer Token, you’ll decode, modify, and re-encode the token to escalate privileges and reveal a hiddenFlag⛳️.This task emphasizes the importance of secure token handling and validation by web applications.

Step 1: Intercepting the Request

Step 2: Modifying the Bearer Token

Step 3: Decoding and Editing the Token

Step 4: Replacing the Modified Token

Step 5: Revealing the Flag

* Navigate to/task6or continue from the previous task by clicking the “Continue” button at the bottom of the page.
* EnsureIntercept is Onin Burp Suite’sProxy->Intercepttab.
* Click the “Check All” button on the/task6page to generate a request.
* Intercept this request in Burp Suite.

* Locate theAuthorizationheader in the intercepted request, which contains the Bearer Token.
* Right-click on the token and select “Send to Decoder” or navigate to the Decoder tab and paste the token there.

* In the Decoder tab, follow these steps to decode and modify the token:Decode the token from Base64.Decompress the decoded data (GZIP).You should now see a JSON object with an"admin": falsevalue.Edit the JSON to change"admin": falseto"admin": true.Compress the modified JSON using GZIP.Encode the compressed data back to Base64.
* Decode the token from Base64.
* Decompress the decoded data (GZIP).
* You should now see a JSON object with an"admin": falsevalue.
* Edit the JSON to change"admin": falseto"admin": true.
* Compress the modified JSON using GZIP.
* Encode the compressed data back to Base64.

* Copy the newly encoded token.
* Return to theProxy->Intercepttab, and replace the original Bearer Token in theAuthorizationheader with your modified token.
* Forward the request.

* With the modified Bearer Token sent, monitor the application’s response for any changes or newly accessible content that indicates elevated privileges.
* Look for and document the hiddenFlagthat is revealed as a result of your successful token manipulation.

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x02_burpsuite_fundamentals
* File:6-flag.txt

### Tasks list

* Mandatory
* Advanced


