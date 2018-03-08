# Server Side Vulnerabilities

## Web Server Vulnerabilities

- HTTP Response splitting: Putting HTTP Header data in the requests
- Web Cache Deception
- Use Cache-Control header to prevent
- Problems are not in the core HTTP processing but in the modules come with the webserver
- Modules
  - Proxy
  - SSL/TLS
  - Server side languages
  - Processing capability


### Quiz

- Putting multiple HTTP responses into one packet will cause ________
  - Denial of Service
  - Web Cache Deception
  - **Cache Poisoning**
  - Circulcar Reference
- Which of the following is not one of the big three web servers
  - Apache
  - **Firefox**
  - Nginx
  - IIS
- Approximately how many vulnerabilities have there been in Apache over the past 20 years?
  - 10s
  - **100s**
  - 1000s
  - 10,000s
- mod_rewrite is an example of what kind of module?
  - Proxying
  - SSL/TLS
  - **Processing capability**
  - Server side languages
- True or False: Most classic languages like C and PHP come with their own pre-built webserver
  - True
  - **False**

## Server Side Programming

- Nginx uses FastCGI to communicate with programs via sockets

### Benefits
- Dynamic modification
- Database communication
- Sensitive actions are not performed by clients
- No need for plugins on clients/browsers


### Quiz

- Which of the following is NOT an advantage of Server Side Benefits?
  - Database communication
  - No need for plugins
  - Secure sensative actions
  - **Offload processing**
- Including the server side programming engine directly in the web server is the _____
  - The IIS approach
  - **The Apache approach**
  - The Nginx approach
  - The Node.JS approach
- Which of the following is a possible security problem exclusive to server side programming
  - Code injection
  - Information disclosure
  - **Remote code execution**
  - Authentication Bypass
- FastCGI is used for _____.
  - Caching server side programming calls
  - **Communicating between webserver and programs**
  - Looking up DNS hosts
  - Interfacing between web servers and browsers
- Sockets as used by NGINX+FastCGI are for
  - **Interprocess communication**
  - HTTP Communication
  - Process performance
  - Application managment

## Intro to PHP

### Quiz

- CGI: connectors between webservers and programs

- PHP is written in which underlying ?
  - **C**
  - Perl
  - Cobol
  - Java
- True or False: PHP is the most popular web based programming language
  - **True**
  - False
- True or False: Magic quotes was designed to prevent SQL Injection?
  - **True**
  - False
- PHP 5 got its first stable release in in ______
  - 2002
  - 2005
  - **2008**
  - 2010
-The current version of PHP is PHP ____
  - 4.0
  - 5.0
  - 6.0
  - **7.0**

## Hardening Web Servers

### Information disclosure

- The Server header
- Directory listing by default
- Displaying debug information

### Extra methods and protocols

- Execute in least-privileged mode
- Methods: TRACE
- Protocols other than HTTP: FTP
- Disable mods

### Logging

- Those who can write to the log files usually can gain access to the UID that the webserver is started as, usually root. Be mindful of giving access to log files.

### Quiz

- What PHP contents might be placed in /tmp
  - POST parameters
  - Cookie values
  - **Session data**
  - interprocess calls
- When directory indexing is enabled it means
  - The webserver will cache folder contents
  - The webserver will keep statistics
  - **The webserver will list directory contents**
  - A Webserver module that serves the index file
- Which of the following was a Security header we mentioned
  - **X-Frame-Options**
  - X-Security-Controls
  - X-Strict-TLS
  - X-Security-Options
- What did the apache.org warning regaurding logging advise against
  - Deleting log files
  - **Giving folks access to log files**
  - Putting unfiltered content in log files
  - Writing log files as the user owning apache.
- What was the way we discussed to stop passive eavesdropping
  - **TLS**
  - Covert Channels
  - Content Security Policy
  - Prevent SQL Injection

## Transport Layer Security

- TLS is at the Transport Layer of OSI model
- SSL 3.1 => TLS in 1999
- CA are built-in

### Overview

- TLS Handshake
  - Client => Server: Client Hello
  - Client <= Server: Server Hello + Server Cert (PubKey)
  - Key Exchange:
    - Client => Server: Client Key Exchange E(PK, k)
    - k is the mutual symmetric key that both the client and server agreed to use
  - Finish handshake

### Downsides

- Slow down webservers
- Break caching

### Using SSL/TLS

- Web proxies
  - Using CONNECT header: proxy sees the data coming from the user and just forward it to the specified domain
- Virtual Hosting: Client_hello_extension: server_name options

### TLS Algorithms

- Hashing, integrity: MD5, SHA1
- Channel: DH
- Symmetric: 3DES, AES
- Asymmetric: RSA, El Gamal
- Bad algorithms: DES, 3-DES, RC4, MD5, SHA1
- Bad standards: SSLv2, SSLv3, TLS1.0, TLS1.1
- Key not shorter than 128 bits.

### SSL from a client side

- Extended validation

### Quiz

- TLS was standadized by which organization?
  - Netscape
  - _IETF_
  - W3C
  - ICANN
- Trusted root CAs are provided by (Choose the best otpion
  - **Browsers**
  - Applications
  - Companies
  - Site Based
- True or False: typical HTTP based TLS provides mutual authentication
  - True
  - _False_
- Which of the following is NOT a problem with TLS
  - Slow speeds down
  - **Negotiation of various ciphers**
  - Virtual hosting cant see Host header
  - Caches cannot function
- Which of the following is considered SAFE
  - **Diffie-Hellman**
  - 3DES
  - RC4
  - SHA1
