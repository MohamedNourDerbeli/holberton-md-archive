# Project: Metasploit - Scripting

![Project Image](https://media.makeameme.org/created/oh-you-have-593047.jpg)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

How to create a custom Metasploit auxiliary module for scanning ports and identifying open ones?

How to check if a target system is vulnerable to MS17-010 using a Metasploit script?

How to automate the execution of an exploit and payload using a custom Metasploit module?

How to gather system information after gaining access using Metasploit post-exploitation modules?

How to create and encode a custom payload to avoid antivirus detection using Metasploit?

IfMetasploit Frameworkis not already installed on your terminal, follow the instructions in the following link to install it successfully:

you can use the machine from your previous task Understanding Vulnerabilities (Exploitation) :

## Resources

#### Read or watch:

* [Metasploit Scripts](/rltoken/WTwbPAf-Un8xpBDfm3y8-w)
* [Writing Meterpreter Scripts](/rltoken/bfqSrmGIMsedOH7QUBdy3g)
* [Implementing Scripts in Metasploit](/rltoken/dNa3LyvrY5FbIwGW1-K3SQ)
* [Scripting Metasploit for a real-life Pentest](/rltoken/cJ47ntf2SbRQ8AZlDY_P0Q)
* [Meterpreter Scripting](/rltoken/jp-ztXxnC2HLBbnyRXfRLw)
* [Metasploit Resource Files](/rltoken/SDsi_fJJ1TBmzLAL3o10qw)

#### References:

* [Metasploit](/rltoken/JhlYbgxr5l_LWvQdzeoIqg)


## Learning Objectives

* How to create a custom Metasploit auxiliary module for scanning ports and identifying open ones?
* How to check if a target system is vulnerable to MS17-010 using a Metasploit script?
* How to automate the execution of an exploit and payload using a custom Metasploit module?
* How to gather system information after gaining access using Metasploit post-exploitation modules?
* How to create and encode a custom payload to avoid antivirus detection using Metasploit?


## Requirements

### General

* Use vi, vim, or emacs for editing Ruby scripts and Metasploit modules.
* Scripts and modules will be tested in the Metasploit environment on Kali Linux.
* Ensure scripts are appropriately sized. There is no strict length requirement for Metasploit modules, but keep them concise.
* Use placeholders (e.g., $1, RHOST, LHOST) for parameters. Avoid using quotes to prevent unintended alterations.
* All script files should end with a new line to maintain proper formatting.
* For Ruby scripts, include the appropriate shebang line if needed (#!/usr/bin/env ruby).
* Include a README.md file at the root of the project directory with an overview, usage instructions, and relevant details.
* Avoid bash-specific constructs such as backticks, &&, ||, or ; in Ruby scripts. Follow Ruby syntax conventions.
* Adhere to Ruby coding conventions and Metasploit guidelines for readability and maintainability.
* Ensure Ruby scripts are executable where required, and follow standard practices for Metasploit modules.
* Properly handle and validate parameters within your Metasploit scripts.


## Tasks

### 0. Custom Port Scanner

Create a Metasploit auxiliary module that scans a range of ports on a target system and identifies which ones are open.

* Create a new file in the:modules/auxiliary/scanner/namedcustom_port_scanner.rb
* modules/auxiliary/scanner/namedcustom_port_scanner.rb
* Define the module with the necessary metadata.
* Implement the logic to scan a range of ports and print the open ports.

```bash
holbertonschool-cyber_security$ msfconsole
msf6 > loadpath /path/to/modules/
Loaded 1 modules:
    1 auxiliary modules
msf6 > use auxiliary/scanner/custom_port_scanner
msf6 auxiliary(scanner/custom_port_scanner) > set RHOST 172.31.128.202
RHOST => 172.31.128.202
msf6 auxiliary(scanner/custom_port_scanner) > set STARTPORT 20
STARTPORT => 20
msf6 auxiliary(scanner/custom_port_scanner) > set ENDPORT 1000
ENDPORT => 1000
msf6 auxiliary(scanner/custom_port_scanner) > run 
[*] Running module against 172.31.128.202

[+] 172.31.128.202:80 - Port 80 is open on 172.31.128.202
[+] 172.31.128.202:80 - Port 111 is open on 172.31.128.202
[+] 172.31.128.202:80 - Port 139 is open on 172.31.128.202
[+] 172.31.128.202:80 - Port 445 is open on 172.31.128.202
[*] 172.31.128.202:80 - Open ports on 172.31.128.202: 80, 111, 139, 445
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/custom_port_scanner) >
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:vulnerability_research_exploitation/0x04_metasploit_scripting
* File:custom_port_scanner.rb

### 1. Vulnerability Checker

Create a module that checks if a target system is vulnerable to the MS17-010 (EternalBlue) vulnerability

Output:

* Choose the MS17-010 vulnerability
* Write a script to check if the target system is vulnerable to MS17-010.
* Implement the logic to determine if the target is vulnerable.
* Provide meaningful output indicating the presence or absence of the vulnerability.
* Including the targetIP RHOST

```bash
msf6 > use auxiliary/scanner/ms17_010_checker
msf6 auxiliary(scanner/ms17_010_checker) > set RHOST 172.31.128.202
RHOST => 172.31.128.202
msf6 auxiliary(scanner/ms17_010_checker) > run
[*] Checking 172.31.128.202 for MS17-010 vulnerability
[+] 172.31.128.202 is vulnerable to MS17-010.
[*] Auxiliary module execution completed
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:vulnerability_research_exploitation/0x04_metasploit_scripting
* File:vulnerability_checker.rb

### 2. Automated Exploit Launcher

Write a script that automatically launches a chosen exploit against a target system.

Explanation:

This script will automatically configure and launch the specified exploit and payload against the target system

To run:

* Create a new Metasploit module insidemodules/auxiliary
* Accept the target IP, exploit module, and payload as input parameters
* Configure the module to use the specified exploit and payload, and then execute it.

* Initialize the Module: The initialize method sets up the module with the necessary metadata, such as the name, description, author, and license.
* Register Options: The register_options method defines the input parameters for the module, including the target IPRHOST, exploit moduleEXPLOIT, payloadPAYLOAD, local IPLHOST, and local portLPORT.
* Run Method: The run method handles the main logic of the module.It retrieves the input parameters and prints the configuration.It creates an instance of the specified exploit module using framework.exploits.create.It sets the necessary datastore options for the exploit and payload.It creates an instance of the specified payload module using framework.payloads.create.It sets the necessary datastore options for the payload.It launches the exploit using exploit.exploit_simple.
* It retrieves the input parameters and prints the configuration.
* It creates an instance of the specified exploit module using framework.exploits.create.
* It sets the necessary datastore options for the exploit and payload.
* It creates an instance of the specified payload module using framework.payloads.create.
* It sets the necessary datastore options for the payload.
* It launches the exploit using exploit.exploit_simple.

* msfconsole
* Load the module using the command:use auxiliary/automated_exploit_launcher
* Set the target IP address:set RHOST <target-ip>
* Set the exploit module:set EXPLOIT <exploit-module>
* Set the payload:set PAYLOAD <payload>
* Set the local IP address:set LHOST <your-ip>
* Set the local port:set LPORT <your-port>
* Run the module:run

```bash
msf6 auxiliary(automated_exploit_launcher) > run
[*] Launching exploit <exploit-module> against 172.31.128.202 with payload <payload>
[*] Running exploit...
[*] Sending stage (200262 bytes) to 172.31.128.202
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:vulnerability_research_exploitation/0x04_metasploit_scripting
* File:automated_exploit_launcher.rb

### 3. Information Gathering Script

Develop a script that gathers various pieces of information from a target system once access is gained

Explanation:

Usage:

* Create a Metasploit post-exploitation module:modules/post/windows/gather
* Gather information such as the OS version, user accounts, network configuration, and running processes.
* Output the gathered information in a structured format.

* Initialize the Module: The initialize method sets up the module with the necessary metadata, such as the name, description, author, and license.
* Register Options: The register_options method defines the input parameters for the module, including the session ID (SESSION)
* Run Method: The run method handles the main logic of the module. It retrieves the session ID and prints a status message, then calls various methods to gather system information, user information, network information, and running processes.
* gathersysteminfo: Uses the sysinfo command to get the operating system and computer name.
* gatheruserinfo: Uses the getuid command to get the user information.
* gathernetworkinfo: Uses the session.net.config.interfaces method to get network interface details, including IP address, netmask, and broadcast address.
* gatherrunningprocesses: Uses the ps command to get a list of running processes, including their PID and name.

* msfconsole
* use post/windows/gather/information_gathering
* set SESSION <session-id>
* run

```bash
msf6 post(windows/gather/information_gathering) > run
[*] Gathering system information from 172.31.128.202
[*] OS: Windows 10 (Build 14393, 64-bit)
[*] Computer: WIN-ABC1234
[*] User: NT AUTHORITY\SYSTEM
[*] Interface: Ethernet0, IP: 192.168.1.20
[*] Process 1000 - explorer.exe
[*] Process 1050 - cmd.exe
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:vulnerability_research_exploitation/0x04_metasploit_scripting
* File:information_gathering.rb

### 4. Custom Payload Generator

Create a custom payload generator that produces a payload tailored to specific requirements (e.g., a reverse shell with custom encoding)

Hint:

Checkshikata_ga_nai

* Write a Ruby script that generates a custom payload
* Ensure the payload is encoded to avoid detection by antivirus software
* Test the payload to verify it works as expected

```bash
msf6 payload(custom_payload_generator) > run
[*] Generating payload with encoding: x86/shikata_ga_nai
[+] Generated encoded payload: \xfc\xe8\x82...
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:vulnerability_research_exploitation/0x04_metasploit_scripting
* File:custom_payload_generator.rb

### Tasks list

* Mandatory
* Advanced


