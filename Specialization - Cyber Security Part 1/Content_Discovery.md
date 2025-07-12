# Project: Content Discovery

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/F2RRT5SQW6J7GXGQ.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [Content discovery](/rltoken/4dKBGD7DLjPuXgjQBhTO6g)
* [Content Discovery for Web Application Security](/rltoken/yhtbr36Nj0RrdeoIKKDPHg)
* [Content Discovery: Understanding Your Web Attack Surface](/rltoken/J6og7oVbNao-XjH5WzdEfQ)
* [What are the content discovery](/rltoken/f9FHolUrW9elZm7y-CsxeQ)
* [OWASP Testing Guide: Content Discovery](/rltoken/gpyeuuZMBYcNL72n1wOf6A)
* [Exploiting: Content Discovery](/rltoken/oKdUCYkY8bI5MudGf7ktkw)

#### References:

* [dirb](/rltoken/aV_fib1S2MvoIXc7OFErZA)
* [nikto](/rltoken/qahRpmkHk9sCIA3I5Uijtw)
* [sfuzz](/rltoken/LVmLwXfBsI4A5AGZ0ePwnw)
* [wfuzz](/rltoken/qYnWfGgRFFc8xe-exVvnmw)
* [gobuster](/rltoken/BnKYJp_5dIyR6gFpC-wtJA)
* [dirbuster](/rltoken/wywUfmG_ZZwnLa3yZqHJIw)
* [feroxbuster](/rltoken/QcdGw7G7rchkJ6uN0_LuMQ)


## Learning Objectives

* What iscontent discovery?
* Why is content discovery important?
* How does directorybruteforcingwork?
* What isGobusterand how is it used?
* Explain the use ofBurp Suitein content discovery.
* How doesOWASP ZAPassist in content discovery?
* What arewordlistsand how are they used in content discovery?
* Describe the purpose of tools likeDirBuster.
* What arehiddendirectories and files in web security?
* Explainfuzzingin the context of web security.


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly one line long ($ wc -l fileshould print 1)
* All your files should end with a new line (Why?)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* For this project, your focus will be on the targetCyber - WebSec 0x04.


## Tasks

### 0. Manual Discovery - Secrets in Plain Sight

Your goal is to uncover a hidden flag by thoroughly exploring the site’s structure.

Use all available discovery methods, including analyzing files such asrobots.txt,sitemap.xml, andfavicon.ico

1 . Sitemap Exploration

Start by reviewing the sitemap located at/sitemap.xml. The sitemap may reveal unusual or hidden routes not linked from anywhere else on the site.

One of these routes contains your flag.

2 . Additional Discovery

Investigate any common files such asrobots.txtorfavicon.ico, as they may contain further clues or hidden paths.

* Target Machine:Cyber - WebSec 0x04
* Target Endpoint:http://web0x04.hbtn/

```bash
Useful Instructions
1.Start by navigating to /robots.txt. Look for any Disallow entries that might hint at hidden or restricted paths. These paths could lead to interesting or hidden resources.
2.Access /sitemap.xml. Sitemaps are used to help search engines index web content, but they may also reveal hidden resources. Find the resource that is not linked from anywhere else on the site to discover your flag.
3.Download the site's favicon.ico and analyze it using tools or online resources like the OWASP favicon database. By matching the favicon to known frameworks, you might uncover more information about the site.
4.Pay close attention to details in each file. Each file could contain direct paths or subtle hints that lead to the next step in your discovery process.
5.Utilize online tools for favicon analysis and comparison to help identify the framework and speed up your search for hidden resources.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:0-flag.txt

### 1.  Manual Discovery - Headers, Headers, Always Check Headers

HTTP Headers often hide secrets 🤫.In this task, you’ll meticulously inspect HTTP response headers to unearth a hiddenFlag⛳️.This requires a keen eye and an understanding of how developers might conceal information within the HTTP protocol.

* Target Machine:Cyber - WebSec 0x04
* Target Endpoint:http://web0x04.hbtn/

```bash
Useful Instructions
1. Utilize `curl`, browser developer tools, or similar tools to examine the complete set of HTTP response headers returned from the target endpoint.
2. Do not overlook non-standard headers; the flag may be tucked away within a custom or uncommon header field.
3. Be aware that servers can dynamically alter headers based on the request's nature. Vary your request type, user-agent, and other headers to provoke different responses.
4. Certain headers might appear only under specific circumstances (e.g., receiving error codes or when making requests with unique headers). Adjust your requests to explore these possibilities.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:1-flag.txt

### 2.  Manual Discovery - Stalking the Stack: A Template Tale

Behind every sleek website lies a framework or template, often leaving subtle clues for a keen investigator.Your mission is to uncover the origin of the frontend template used bycod.hbtn.ioTo do this, you’ll need to investigate its JavaScript source code and follow breadcrumbs to identify the vendor or framework behind it.

Your task is to submit the URL of the live preview of the frontend template used by cod.hbtn.io, as found on the vendor’s website.

* Target Website:https://cod.hbtn.io

* Example submission format:$ cat 2-vendor.txt
https://vendorwebsite.com/template-name/

```bash
$ cat 2-vendor.txt
https://vendorwebsite.com/template-name/
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:2-vendor.txt

### 3. Manual Discovery - Time Travelers: Unearthing the Past with OSINT

Open Source Intelligence (OSINT) tools provide a treasure trove of information if you know where to look.From understanding a website’s technology stack with:

Each tool offers a unique lens to view a target’s digital footprint.Your mission will extend beyond mere observation; you’ll apply these skills in a practical challenge.

For this endeavor, your destination isholbertonschool.com, but not as it exists today.You’re tasked with journeying back in time toFebruary 2016using the Wayback Machine.Your objective: identify the individual who was proudly mentioned on the index page as a “Sr. Software Engineer at Microsoft.”

* Diving into its version history via theWayback Machine
* Exploring code repositories onGitHub
* Discovering misconfiguredS3 buckets
* LeveragingGoogle dorkingfor targeted search results.
* Exploring used framework withWappalyzer

* Target Website:https://www.holbertonschool.com
* Example:$ cat 3-senior.txt
Yosri Ghorbel

```bash
$ cat 3-senior.txt
Yosri Ghorbel
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:3-senior.txt

### 4. The Buster Series - Initiating with Gobuster `dir mode`

Gobuster is a powerful tool designed to automate the process of content discovery.It employs various modes, making it indispensable for the modern cybersecurity toolkit.Your quest involves mastering Gobuster’s modes to unearth hidden resources, subdomains, and much more.We start our journey with an overview of the seven key modes Gobuster offers:

This comprehensive feature set makes Gobuster adept at revealing the unseen parts of web applications and infrastructure.

Your first mission is to familiarize yourself with Gobuster’sdirmode by conducting a directory brute-force attack against a target website.You’ll leverage this mode to discover hidden directories that will return aFlag⛳️ as content withTask #4as Website title.

Hints

* Target Machine:Cyber - WebSec 0x04
* Target Website:http://web0x04.hbtn
* Dir Word List
* WP Word List

```bash
Useful Instructions
1. Select a wordlist for the directory brute-forcing operation. You can use common wordlists provided by tools like `dirb` or `SecLists`.
2. Execute Gobuster in `dir` mode against the target website, specifying your chosen wordlist.
3. Analyze the output, focusing on HTTP status codes that indicate the presence of a directory (e.g., 200 OK, 403 Forbidden).
4. Document any interesting directories you discover, noting their paths and any content or functionality they reveal.Remember:
- Experiment with different wordlists and options (e.g., specifying file extensions) to uncover as much as possible.
- Be mindful of the network and server load you're generating with your requests to ensure responsible use of the tool.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:4-flag.txt

### 5. The Buster Series - Unveiling Hidden Subdomains `dns mode`

This powerful feature is designed for DNS subdomain enumeration,allowing you to uncover hidden or unlinked subdomains which could expose additional facets of the target’s online presence or infrastructure vulnerabilities.Unlock the secrets of DNS by performing a zone transfer to uncover hidden records.You’ll use advanced DNS querying techniques to reveal alternative DNS records that may not be easily discoverable through standard methods.You’ll leverage this mode to discover hidden subdomain that will return aFlag⛳️ as content withTask #5as Website title.

dns_wordlist.txt

* Target Machine:Cyber - WebSec 0x04
* Target Domain:web0x04.hbtn

```bash
Useful Instructions
1. Choose a wordlist tailored for DNS subdomain brute-forcing. The `SecLists` project offers comprehensive lists suited for this purpose.
2. Use Gobuster in `dns` mode to enumerate subdomains for the target domain.
3. Pay careful attention to the output, particularly any discovered subdomains. These entries can reveal development, staging, or other sensitive environments related to the target.
4. Record the subdomains found, noting any that were previously unknown or particularly interesting in terms of security or functionality.Remember:
- Utilizing a high thread count with `-t` can speed up the scan but ensure it's within reasonable limits to avoid network or service disruption.
- Some discovered subdomains may not be immediately accessible or resolve to public IP addresses, necessitating further investigation or different attack vectors.
5. Use the appropriate DNS query tools to attempt retrieving the DNS zone file for the target domain. Some DNS record types might contain hidden or valuable information.
6. Once you’ve performed the zone transfer, examine all returned records carefully. Look for any entries that seem out of the ordinary or contain unusual data.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:5-flag.txt

### 6. FFuf Series - Subdomain Fuzzing Frenzy

Explore the web infrastructure by using ffuf to brute-force subdomains (virtual hosts) on the target server.Discover hidden subdomains that might contain important information, such as a flag or access to alternative environments.

* Target Machine:Cyber - WebSec 0x04
* Target Domain:web0x04.hbtn

```bash
Useful Instructions
1. Wordlist Preparation:
        Use a wordlist tailored to subdomain enumeration. Make sure it includes common subdomains, environment names, and other relevant terms.
2. Fuzz Subdomains:
         Run ffuf to fuzz for potential subdomains of the target domain. Pay attention to the responses and any unusual or unexpected status codes.
3. Examine Responses:
         Analyze the output and investigate any discovered subdomains.
         Some may return useful content that could contain sensitive information, such as a flag or further clues for your reconnaissance.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:6-flag.txt

### 7. The Buster Series - Fuzzing for Fun and Profit `fuzz mode`

Fuzzing is a powerful technique used to discover unknown vulnerabilities, misconfigurations, or hidden content by sending a wide range of inputs and observing the application’s responses.You’ll leverage this mode to find a page that will return aFlag⛳️ .

list_fuzz

* Target Machine:Cyber - WebSec 0x04
* Target Website:http://web0x04.hbtn/{¶}/hbtn-{¶}

```bash
Useful Instructions
1. Constructing a fuzzing attack requires a precise location to be efficient.
2. Create or select a wordlist tailored for fuzzing. Your wordlist should include common filenames, extensions, or parameters that could unveil hidden content.
3. Execute Gobuster in `fuzz` mode, replacing the target URL's specific component `{¶}` with the keyword `FUZZ`.
4. Analyze the responses for status codes or content lengths that stand out from the norm. These anomalies could indicate successful discovery of hidden content or functionality.
5. Document any findings from your fuzzing efforts, highlighting how the discovered resources could impact the target's security posture or provide further avenues for exploration.Remember:
- Fuzzing can generate a significant amount of traffic. Be mindful of the target server's capacity and any legal or ethical considerations.
- The effectiveness of fuzzing is highly dependent on the quality and relevance of your wordlist. Customizing your wordlist for the target environment can greatly enhance your results.
- Don't forget you are checking for two FUZZ
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:7-flag.txt

### 8. The Buster Series - Tackling TFTP with Brute Force `tftp mode`

Your final challenge in the Gobuster series focuses on thetftpmode,a specialized approach aimed at brute-forcing filenames on servers using the Trivial File Transfer Protocol (TFTP).TFTP servers are commonly used for booting network devices or for simple file transfers in environments where security is not a primary concern.However, misconfigured or unauthorized TFTP servers can expose sensitive information or system files to an attacker.You’ll leverage this mode to find afilethat contains aFlag⛳️.

* Target Machine:Cyber - WebSec 0x04
* Target Host:web0x04.hbtn

```bash
Instructions
1. Given the nature of TFTP, compile a wordlist of common system configuration filenames, bootloader files, or backup file names that might exist on a TFTP server.
2. Use Gobuster’s `tftp` mode to enumerate files on the target TFTP server.
3. Be attentive to successful hits in Gobuster’s output, which can indicate the existence of a file on the server. Each found file warrants further analysis to understand its contents and implications.
4. Compile a list of discovered files, offering insights into any potentially sensitive data or system information they might reveal.Remember:
- TFTP does not support authentication by default, making it inherently insecure. Ensure that your testing is authorized and does not disrupt the target environment.
- Brute-forcing a server can lead to network congestion or server performance issues. Conduct your tests responsibly and consider the impact on the target server and network.
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:web_application_security/0x04_content_discovery
* File:8-flag.txt

### Tasks list

* Mandatory
* Advanced


