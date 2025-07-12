# Project: Cryptography Basics

![Project Image](https://hbtn-gallery.s3.eu-central-1.amazonaws.com/8PQPHB4TJA5CWR97.png)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [What is cryptography](/rltoken/k9yYDtlUU7AjRQI8HJq7wQ)
* [The importance of cryptography](/rltoken/5jss8MOFz_zEqD44QqXTNg)
* [What is cryptography in cyber security](/rltoken/HRj8MhuOksib-4gyqKbcGw)
* [Cryptography](/rltoken/YFlLqUCXlZASsxkMH-SuHw)
* [OpenSSL](/rltoken/DLwcrfBMRL4EIdiLr0B_gA)
* [John The Ripper Hash Formats](/rltoken/v6_kxNz0d4Y0dTQlN-40UQ)
* [How to use hashcat](/rltoken/9hmqmxQs_C3SMAPph6vjUQ)

#### References

* [John the Ripper](/rltoken/tOaOl322_vXnq5zLMhDQvA)
* [hashcat](/rltoken/PETfFwBUifZ12fdvT-WA1A)


## Learning Objectives

* What is cryptography in cybersecurity
* What are the different types of cryptography
* What is Encryption
* What is Decryption
* What is the importance of cryptography
* What are the types of cryptography
* What are the applications of cryptography
* What is a hash algorithm
* What SHA stands for
* What isJohn the Ripper
* How to useJohn the Ripper
* How to crack advanced hashes withJohn the Ripper
* What ishashcat
* How to usehashcat


## Requirements

### General

* Allowed editors:vi,vim,emacs.
* All your scripts will be tested onKali Linux.
* All your scripts should be exactly two lines long ($ wc -l fileshould print 2)
* You must substitute the IP range for$1.
* All your files should end with a new line (Why?)
* The first line of all your files should be exactly#!/bin/bash.
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* You are not allowed to use backticks,&&,||or;.
* Your code should use theBettystyle. It will be checked usingbetty-style.plandbetty-doc.pl
* All your files must be executable


## Tasks

### 0. SHA1

Writea bash scriptthat hashes a givenpassword

Depending on the given password, the output could change

* You should useSHA-1algorithm
* Your script should accept apasswordas an arguments$1
* The resulting hash must be stored in0_hash.txt

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./0-sha1.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 0_hash.txt
808f94d2847fb381839b4bbbd7cdf30804fd47ac
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:0-sha1.sh

### 1. SHA256

Writea bash scriptthat hashes a givenpassword

Depending on the given password, the output could change

* You should useSHA-256algorithm
* Your script should accept apasswordas an arguments$1
* The resulting hash must be stored in1_hash.txt

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./1-sha256.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat 1_hash.txt
77c4925c01e8d9f79c8a6a61685c6b3182be10f2fa553de915f3733ee19c0204
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:1-sha256.sh

### 2. MD5

Writea bash scriptthat hashes a givenpassword

Depending on the given password, the output could change



* You should useMD5algorithm
* Your script should accept apasswordas an arguments$1
* The resulting hash must be stored in2_hash.txt

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 ./2-md5.sh "Holberton"
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 2_hash.txt
f3b21c0205fba4fc7e6cb96ae6edc950
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:2-md5.sh

### 3. Secure Password Hash

Encrypting passwords with OpenSSL: because even secret handshakes need a touch of pizzazz!

Writea bash scriptthat accepts a password as argument$1, combines it with a random 16-character value usingOpenSSL, and generate SHA-512 hash of the new password usingOpenSSL.

Depending on the given password, the output could change



* The resulting hash must be stored in3_hash.txt

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴./3-password_hash.sh "maroua@123"┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 3_hash.txt
SHA512(stdin)= e6ec54449afad599a6e98cf37e9cd541e6d758ae30760080f1c7a2c6934e94edb5fa358e21633c6ed9cfced7dcf60cff7291ac96e2ac21f9df4429e137ae240f
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:3-password_hash.sh

### 4. Wordlist Mode

In Wordlist Mode, we’ll provide John with a list of passwords, we will use the well-knownRockYouwordlist

Writea bash scriptthat crack the password usingJohn the Ripperbased on the filehash.txt

* You should usejohn
* You should use John the Ripper’sWordlist Modeto attempt password cracking
* Your script should accepthash.txtas an arguments$1
* You should find the hashed passwords.echo "<hashed_passwords>" > 4-password.txt

```bash
echo "<hashed_passwords>" > 4-password.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:4-wordlist_john.sh, 4-password.txt

### 5. Windows Authentication Cracking

Let’s explore NThash orNTLM, a hash format used in modern Windows systems to secure user and service passwords.

Writea bash scriptthat crack the password usingJohn the Ripperbased on the filehash.txt.

Hints

* You should find the hashed password
* Your script should accepthash.txtas an arguments$1echo "<hashed_passwords>" > 5-password.txt

* You need to set the format flag tont┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat hash.txt
895F465356A0403458759A6B104B7242
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 ./5-windowsjohn.sh hash.txt
john --wordlist=rockyou --format=nt window.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
****            (?)1g 0:00:00:00 DONE (2023-09-22 16:16) 50.00g/s 3312Kp/s 3312Kc/s 3312KC/s jonny123..gatasalvaje
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed.
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptography_basics]
└─🏴 cat 5-password.txt
****

```bash
echo "<hashed_passwords>" > 5-password.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:5-windows_john.sh, 5-password.txt

### 6. John Cracking!

Writea bash scriptthat crack the password usingJohn the Ripperbased on the filecrack.txt.

* You should find the hashed password
* Your script should acceptcrack.txtas an arguments$1echo "<hashedpasswords>" > 6-password.txt┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat crack.txt
aee408847d35e44e99430f0979c3357b85fe8dbb4535a494301198adbee85f27
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴./6-crackjohn.sh crack.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA256 [SHA256 256/256 AVX2 8x])
Warning: poor OpenMP scalability for this hash type, consider --fork=2
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
*******          (?)1g 0:00:00:00 DONE (2023-09-21 14:23) 25.00g/s 819200p/s 819200c/s 819200C/s 
Use the "--show --format=Raw-SHA256" options to display all of the cracked pa
Session completed. 
┌──(maroua㉿HBTN-LAB)-[~/0x03cryptographybasics]
└─🏴 cat 6-password.txt
*******

```bash
echo "<hashedpasswords>" > 6-password.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:6-crack_john.sh, 6-password.txt

### 7. Hashcat Straight Attack!

Writea bash scriptthat crack the password usinghashcatbased on the filehash.txt.

* You should find the hashed password
* Your script should accepthash.txtas an arguments$1echo "<hashed_passwords>" > 7-password.txt

```bash
echo "<hashed_passwords>" > 7-password.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:7-crack_hashcat.sh, 7-password.txt

### 8. Hashcat Combination!

Writea bash scriptthat combine two wordlists usinghashcat

* You should find the final wordlists after combination
* Your script should acceptwordlist1.txtas an arguments$1
* Your script should acceptwordlist2.txtas an arguments$2

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat wordlist1.txt 
pass
123
hello
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 cat wordlist2.txt 
word
world
000
┌──(maroua㉿HBTN-LAB)-[~/0x03_cryptography_basics]
└─🏴 ./8-combination_hashcat.sh wordlist1.txt wordlist2.txt 
password
passworld
pass000
123word
123world
123000
helloword
helloworld
hello000
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:8-combination_hashcat.sh

### 9. Hashcat Combination Attack

Writea bash scriptthat crack the password usinghashcatbased on the previous task

Hints

* You should usehashcat
* Your script should accepthash.txtas an arguments$1
* You should find the hashed password.echo "<hashed_password>" > 9-password.txt

* You should usewordlist1.txt,wordlist2.txtafter combination

```bash
echo "<hashed_password>" > 9-password.txt
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:cybersecurity_basics/0x03_cryptography_basics
* File:9-attack_hashcat.sh, 9-password.txt

### Tasks list

* Mandatory
* Advanced


