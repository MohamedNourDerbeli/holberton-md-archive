# Project: Buffer overflow

![Project Image](https://pbs.twimg.com/media/EiIqZPbX0AA63KT?format=jpg&name=small)

## Description



At the end of this project, you are expected to be able toexplain to anyone,without the help of Google:

## Resources

#### Read or watch:

* [What is buffer overflow](/rltoken/NczkQKz0IebdFkx-LmSCEw)
* [What Is a Buffer Overflow Attack](/rltoken/ZDnvNv2vH8ogyJcThrUUPw)
* [buffer overflow attack types and prevention methods](/rltoken/8MA4rYQXJs7GJDpC5HHVVQ)
* [How Buffer Overflow Attacks Work](/rltoken/vmmQeXGeupBLJ44zMSKdrw)
* [Buffer Overflow in Cyber Security - What is, Types, & Consequences](/rltoken/cSWx090kiSXu_ZH4ULlOXQ)
* [Overflow Vulnerabilities](/rltoken/2_DJIKLTTW_HXexwr04OGw)
* [Consequences of Buffer Overflow](/rltoken/lMFpFYWBqvgRfZW8uiYmeg)
* [Mitigation Strategies](/rltoken/1aKx_0hKocpDIuw_w0A2gw)
* [Common C Code Vulnerabilities and Mitigations  relate to buffer overflows](/rltoken/TjGzcat4on7uaXek1cw7Ow)

#### References:

* [Buffer Overflow](/rltoken/ky48WX1OqqQV3peAORDbLg)
* [The /proc filesystem](https://www.kernel.org/doc/Documentation/filesystems/proc.txt)


## Learning Objectives

* What is a buffer?
* What is Buffer Overflow?
* What is a Buffer Overflow Attack?
* What causes buffer overflow attacks?
* How do Attackers Orchestrate Buffer Overflow Attacks?
* What are the different types of buffer overflow attacks?
* How to detect buffer overflow?
* What are the consequences of Buffer Overflow?
* How To Prevent and Mitigate Buffer Overflow Attacks?


## Requirements

### Python Scripts

* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS usingpython3(version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thePEP 8style
* All your files must be executable
* The length of your files will be tested usingwc


## Tasks

### 0. Hack the VM

Write a script that finds a string in the heap of a running process, and replaces it.

Terminal 1:

Terminal 2:

* Usage:read_write_heap.py pid search_string replace_stringwherepidis the pid of the running processand strings are ASCII
* wherepidis the pid of the running process
* and strings are ASCII
* The script should look only in the heap of the process
* Output: you can print whatever you think is interesting
* On usage error, print an error message onstdoutand exit with status code1

```bash
┌──(maroua㉿HBTN-LAB)-[~/0x04. Buffer overflow]
└─🏴 cat main.c 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

/**
 * main - uses strdup to create a new string, loops forever-ever
 *
 * Return: EXIT_FAILURE if malloc failed. Other never returns
 */
int main(void)
{
    char *s;
    unsigned long int i;

    s = strdup("Holberton");
    if (s == NULL)
    {
        fprintf(stderr, "Can't allocate mem with malloc\n");
        return (EXIT_FAILURE);
    }
    i = 0;
    while (s)
    {
        printf("[%lu] %s (%p)\n", i, s, (void *)s);
        sleep(1);
        i++;
    }
    return (EXIT_SUCCESS);
}
┌──(maroua㉿HBTN-LAB)-[~/0x04. Buffer overflow]
└─🏴 gcc -Wall -pedantic -Werror -Wextra main.c -o main
┌──(maroua㉿HBTN-LAB)-[~/0x04. Buffer overflow]
└─🏴./main
[0] Holberton (0x555e646e02a0)
[1] Holberton (0x555e646e02a0)
[2] Holberton (0x555e646e02a0)
[3] Holberton (0x555e646e02a0)
[4] Holberton (0x555e646e02a0)
[5] Holberton (0x555e646e02a0)
[6] Holberton (0x555e646e02a0)
[7] Holberton (0x555e646e02a0)
[8] Holberton (0x555e646e02a0)
[9] Holberton (0x555e646e02a0)
[10] Holberton (0x555e646e02a0)
[11] Holberton (0x555e646e02a0)
[12] Holberton (0x555e646e02a0)
[13] Holberton (0x555e646e02a0)
[14] Holberton (0x555e646e02a0)
[15] Holberton (0x555e646e02a0)
[16] Holberton (0x555e646e02a0)
[17] Holberton (0x555e646e02a0)
[18] Holberton (0x555e646e02a0)
[19] Holberton (0x555e646e02a0)
[20] Holberton (0x555e646e02a0)
...
[78] Holberton (0x555e646e02a0)
[79] Holberton (0x555e646e02a0)
[80] Holberton (0x555e646e02a0)
[81] Holberton (0x555e646e02a0)
[82] Holberton (0x555e646e02a0)
[83] Holberton (0x555e646e02a0)
[84] Holberton (0x555e646e02a0)
[85] Holberton (0x555e646e02a0)
[86] Holberton (0x555e646e02a0)
[87] Holberton (0x555e646e02a0)
[88] Holberton (0x555e646e02a0)
[89] Holberton (0x555e646e02a0)
[90] Holberton (0x555e646e02a0)
[91] Holberton (0x555e646e02a0)
[92] maroua (0x555e646e02a0)
[93] maroua (0x555e646e02a0)
[94] maroua (0x555e646e02a0)
[95] maroua (0x555e646e02a0)
[96] maroua (0x555e646e02a0)
[97] maroua (0x555e646e02a0)
[98] maroua (0x555e646e02a0)
[99] maroua (0x555e646e02a0)
[100] maroua (0x555e646e02a0)
[101] maroua (0x555e646e02a0)

...
```

**Repo Info:**
* GitHub repository:holbertonschool-cyber_security
* Directory:linux_security/0x04_buffer_overflow
* File:read_write_heap.py

### 1. Buffer Overflow Attack Report!

Buffer overflowsoccur when a program attempts to write more data to a buffer than it can hold, potentially
overwriting adjacent memory locations. This can be exploited by attackers to gain unauthorized access to systems 
or execute malicious code.

Your task is to create a detailed blog post that covers various aspects of buffer overflow.

Methodology:

Submission Instructions:

This task challenges you to delve into the world of buffer overflow attacks, understand their mechanisms and implications,
and explore methods for safeguarding systems from such vulnerabilities.

**Repo Info:**
### Tasks list

* Mandatory
* Advanced


