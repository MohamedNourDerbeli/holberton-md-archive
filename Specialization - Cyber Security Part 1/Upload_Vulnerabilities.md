# Project: Upload Vulnerabilities

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/PDENT1656CE2LW4E.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google: (at least 14 questions)

## Resources

#### Read or watch:

* [File upload vulnerabilities](/rltoken/Uw1E9QxS4M-spOFmZMdUuw)
* [Unrestricted File Upload](/rltoken/jl9A7kJkup9pcGyof7oDpA)
* [File Upload Attacks Explained](/rltoken/A9uDpRc19LomBfqtYR7HXA)
* [File Upload Protection – 10 Best Practices](/rltoken/8BUyL3B9YPzPWhYmKUuG-w)
* [Preventing File Upload Vulnerabilities](/rltoken/bjBJh0B5WSg8QUjKKJWQiQ)
* [Testing for Upload Vulnerability](/rltoken/vQ2QfGdgrthupeVKosyZ4w)
* [Bypass File Upload Restrictions](/rltoken/DO5Ka6kiaqMuoD8jbzRETw)
* [Understanding Content-Type and Content-Disposition Headers in File Uploads](/rltoken/If0cxRrT665HSZI6kGscyw)

#### References:

* [File Upload Protection Cheat Sheet](/rltoken/t8dwQmkhRgc6zxIjV9yUFw)
* [File Upload Security Checklist](/rltoken/3HCPK36Z6W0T-kg7aK5EvA)
* [Understanding MIME Types and File Extensions](/rltoken/cSV4ceDQJDUOktqgAbHRwQ)


## Learning Objectives

* What is anunrestricted file upload?
* Why are file uploads a security risk?
* How canfile upload formsbe exploited?
* What is aweb shell?
* How doMIME typesrelate to upload security?
* What iscontent-type spoofing?
* How canserver-side validationmitigate risks?
* What is the importance offile extension filtering?
* How canclient-side checksbe bypassed?
* What are somesecure file uploadpractices?
* How does filesize limitationhelp security?
* What are therisksof storing files on the same domain?
* How dofile permissionsaffect upload security?
* Why should upload directories not beexecutable?


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetCyber - WebSec 0x05.


## Tasks

### 0. Oops! We forget that endpoint for testing purpose

Your mission is to determine which subdomain contains a web application with an insecure file upload feature.This task requires you to methodically explore each subdomain, looking for any interfaces or functionalities that allow file uploads.Identifying the correctsubdomainsets the stage for deeper vulnerability analysis in subsequent tasks.

* Target Machine:Cyber - WebSec 0x05
* Main Domain:http://web0x05.hbtn
* Example:$ cat 0-target.txt
up3l0d3r.web0x05.hbtn

```bash
$ cat 0-target.txt
up3l0d3r.web0x05.hbtn
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x05_upload_vulnerabilities
* File:0-target.txt

### 1. Some filters are only client-sided !

Having identified the vulnerable subdomain, your next challenge is to bypass the client-side file type filtering mechanism of the web application’s upload feature.Your success in uploading a restricted file type will reveal a hiddenFlag⛳️ as proof of your accomplishment.

You will need to use this php command to read the flag:<?php readfile('FLAG_1.txt') ?>FLAG will only be generated if you upload a php file!

* Target Machine:Cyber - WebSec 0x05
* Target Endpoint:http://[vuln-subdomain].web0x05.hbtn/task1

```bash
Useful Instructions
1. Use browser developer tools to inspect the upload form and any JavaScript code that validates file types. Look for patterns or keywords it checks against.
2. Consider using tools like Burp Suite to intercept and modify the upload request, changing the file name or MIME type to bypass client-side checks.
3. Explore different ways to initiate the file upload (e.g., drag-and-drop functionality) that might not trigger client-side validation as expected.
4. Pay attention to any error messages or feedback from the server after attempting an upload. These messages can offer clues for refining your bypass technique.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x05_upload_vulnerabilities
* File:1-flag.txt

### 2. Special Characters are so special !

After successfully navigating past the client-side restrictions, you’re faced with a more formidable challenge: bypassing the server-side validation that scrutinizes the file formats being uploaded.This task requires you to cleverly use special characters in the file name to deceive the server-side checks, allowing you to upload a file type that is normally restricted.Successfully uploading such a file will unveil a hiddenFlag⛳️.

You will need to use this php command to read the flag:<?php readfile('FLAG_2.txt') ?>,FLAG will only be generated if you upload a php file!

* Target Machine:Cyber - WebSec 0x05
* Target Endpoint:http://[vuln-subdomain].web0x05.hbtn/task2

```bash
Useful Instructions
1. Investigate how the server processes file names and extensions. Some servers might strip or ignore certain special characters, altering the file name after processing.
2. Experiment with adding special characters like spaces, dots, or null bytes (`%00`) in the file extension. For example, attempting to upload a file named "payload.php.jpg" might be blocked, but "payload.php%00.jpg" could bypass the filter if the server improperly handles null bytes.
3. Utilize tools like Burp Suite to intercept and modify your upload requests, carefully crafting the file names with special characters to test the server's validation logic.
4. Keep an eye on the server's response to each upload attempt. A successful bypass might not always be explicitly confirmed by the application’s UI. Check for any changes in behavior or new functionalities accessible after your upload.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x05_upload_vulnerabilities
* File:2-flag.txt

### 3. What mystery the Magic Numbers Hide ?

With client-side and basic server-side restrictions behind you, the challenge now escalates to bypassing server-side validation that inspects the content of uploaded files, specifically through magic numbers.Magic numbers are unique values at the beginning of files that identify the file format to the system.This task involves manipulating an uploaded file’s magic numbers to pass it off as a benign type while maintaining its malicious functionality.Successfully fooling the server’s content inspection will reveal another hiddenFlag⛳️.

You will need to use this php command to read the flag:<?php readfile('FLAG_3.txt') ?>,FLAG will only be generated if you upload a php file!

* Target Machine:Cyber - WebSec 0x05
* Main Domain:http://[vuln-subdomain].web0x05.hbtn/task3

```bash
Useful Instructions
1. Research and understand the concept of magic numbers in file formats. Identify the magic numbers for both the file type you intend to upload and a benign file type that is allowed by the server.
2. Craft a file that begins with the magic numbers of an allowed file type but contains payload or code typical of a restricted file type. Tools like hex editors can help you modify the file content directly.
3. Test your crafted file by attempting to upload it through the application's upload feature. Pay close attention to how the application responds to determine if your bypass was successful.
4. If direct modification of magic numbers does not yield success, consider more advanced techniques such as embedding your malicious payload within a benign file in a way that does not affect the file's ability to pass as the benign type but still allows execution of the payload under certain conditions.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x05_upload_vulnerabilities
* File:3-flag.txt

### 4. Does File Length matter ?

This sophisticated security measure aims to prevent the upload of potentially malicious files by imposing a strict limit on the file size.Your objective is to bypass this restriction and successfully upload a file that exceeds the server-imposed limit, revealing a hiddenFlag⛳️ as a marker of your success.

There is also a another backdoor, just take a look at the response headersYou will need to use this php command to read the flag:<?php readfile('FLAG_4.txt') ?>,FLAG will only be generated if you upload a php file!

* Target Machine:Cyber - WebSec 0x05
* Main Domain:http://[vuln-subdomain].web0x05.hbtn/task4

```bash
Useful Instructions
1. Begin by understanding the server's file length restrictions. Attempt to upload files of varying sizes to pinpoint the exact limit imposed by the server-side validation.
2. Explore compression techniques or file manipulation methods that can reduce the apparent size of your payload without compromising its functionality. Consider formats that support compression natively and can be decompressed by the application or server.
3. Investigate alternative upload methods provided by the application that might not enforce the same file length checks as the primary upload feature. This could include APIs, legacy upload forms, or other indirect file submission functionalities.
4. Leverage tools like Burp Suite to intercept and modify upload requests, experimenting with ways to either compress your payload further or trick the server into misjudging the file size (e.g., by manipulating HTTP headers related to content length).
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x05_upload_vulnerabilities
* File:4-flag.txt

### Tasks list

* Mandatory
* Advanced


