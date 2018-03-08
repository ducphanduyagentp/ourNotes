# HTTP Continued

## HTTP Requests

- Minimum requirements:
  - Method, request URL, HTTP version
  - Host

### Virtual Host (VHost)

- Hosting multiple hosts domain names on one server
  - Name-based, most common
  - IP-based
  - Port-based

### Quiz

- How do we typically shorten the term Virtual Host?
  - VH
  - VirtualHost
  - **VHost**
  - VirHost
- What is the other common method of hosting multiple web servers
  - IP Based
  - Port Based
  - Host Based
  - Site Based
- When did Host headers become required
  - 0.9
  - 1.0
  - **1.1**
  - 2.0
- How do we delimiate headers headers from one another
  - Spaces
  - **CRLF**
  - Colens
  - Periods
- Which of the following is NOT a required part of an HTTP Message
  - **Message Body**
  - Method
  - Version
  - Request URI

## Introduction to headers

- User-Agent is client-side and totally optional, just for statistical purposes only.
- Referer: Can contain params, client-controlled, should not be used for CSRF protection. Just don't
- Accept type: media, charsets, encoding (typically compression), language.

## HTTP Cookies

- Idempotent
- Set-Cookie header comes from the server
- Generally cookies persist on the disk
- Cookies are sent based on the data specified
- httpOnly: javascript cannot access the cookie

### Cookie lifetime

- Expiration > Current
  - Store on disk
  - Delete after expiration
- No expiration 
  - Store on memory
  - Delete when browser closed
- Expiration < Current
  - Delete
- Expiration dates are modified in privacy browsing

### Quiz

- The RFC for cookies, RFC 6265 is the most recent version of cookies?
  - **True**
  - False
- If no expiration date is provided what will occur?
  - The cookie will be stored for the maximum amount of time
  - **The cookie will be deleted at the end of the browsing session**
  - No cookie will be stored
  - Store cookies for a default 4 hours
- Which of the following is the default cookie for Java
  - ASPSESSIONID
  - **JSESSIONID**
  - CFID
  - PHPSESSID
- Which of the following options has security ramifications?
  - **httponly**
  - domain
  - expiration date
  - path
- Which header is used to install a cookie?
  - **Set-Cookie**
  - Cookie
  - Add-Cookie
  - Define-Cookie

## Sending Data

- Content-Length is not required
- If no Content-Type is presented, the browser will try to guess the data type. And it's not good
- You can do POST and GET params at the same time but that's gonna mess up. Who knows?

### Quiz

- What method is typically used for sending data?
  - GET
  - **POST**
  - DELETE
  - OPTIONS
- Which of the following is a valid media type?
  - html:application
  - html
  - application/html
  - **text/html**
- True or False: Content-length is required
  - True
  - **False**
- Which of the following is a common media subtype
  - **x-www-form-urlencoded**
  - html-form-data
  - form-data-urlencoded
  - www-form-urlencoded 
- Which header is used for describing the media type
  - location
  - content
  - encoding
  - **content-type**

## Receiving Data

- Response headers
  - General: Applied on either requests or responses
    - Cache-Control
    - Connection
    - Date
  - Entity: Metadata
    - Allow
    - Content-Encoding
    - Content-Language
    - Content-Length
    - Content-Location
    - Content-MD5
    - Content-Rage
    - Content-Type
    - Expires
    - Last-Modified
    - Extention-header
  - Response
    - Server: Apache, ...
    - ETag: Entity tag: hash of the data for caching purposes, etc. There are 3 types of ETags: strong, weak.
    - Location
- Status numbers
  - 1xx: Informational
  - 2xx: Success
  - 3xx: Redirection
  - 4xx: Client error
  - 5xx: Server error
- Response message body:

### Quiz

- 4xx status codes typically represent ______.
  - Informational
  - **Client Errors**
  - Server Errors
  - Redirection 
- Which of the following is a general header?
  - **Cache-Control**
  - User-Agent
  - Server
  - Allows 
- Which of the following is a response header?
  - Cache-Control
  - User-Agent
  - **Server**
  - Allows
- Which of the following is a entity header?
  - Cache-Control
  - User-Agent
  - Server
  - **Allows**
- Which of the following is NOT part of a Status-Line
  - **Method**
  - Status Code
  - Reason Phrase
  - HTTP Version

## HTTP Optimization

### Optimization methods

- Pipelining: doing concurent downloads for different resources. Usually browsers limit this to 6 concurent downloads on one domain. So people come up with the following
- Domain sharding: Having multiple domains for the resources to increase the number of concurent downloads

#### SPeeDY

- Made by Google
- Plaintext support (is insane)
- Remove the plaintext support so it can be represented in binary
- Issue: getting things out-of-order
- Head of line blocking
- Deprecated in Jan 2016 by Google
- Multiplexing: sending all resources in 1 TCP connection

### Quiz

- Speedy was designed by whom?
  - Cloudflare
  - Amazon
  - Microsoft
  - **Google**
- Head-of-line blocking was solved in part by?
  - **Pipelining**
  - FIFO
  - Feed-line-support (FLS)
  - Multi Layer Buffering
- Sending multiple files over one TCP connection is known as?
  - **Multiplexing**
  - Multipathing
  - Multibuffering
  - Multilining 
- Speedy was deprecated in what year?
  - 2014
  - 2015
  - **2016**
  - 2017 
- Allowing multiple simultanious downloads from different domains is called?
  - **Domain Sharding**
  - Multiplexing
  - Thread Requesting
  - Pipelining

## HTTP2

### Features

- Multiplexing
- Stream dependencies: Some resources are more important than others.
- Compression of headers: doesn't need to send the header again, just send new data, after the initial request.
- Server push: server sends data that the client hasn't requested yet, but will need in the future.

### Compressing headers

- HPACK
- SPDY used gzip but there's the CRIME attack that target SSL, taking advantages of gzip
- HTTP/2 switched to its own compression algorithm HPACK
- HTTP/2 does not require TLS but all major vendors only support HTTP/2 over TLS connections

### Next Protocol Negotiation (NPN)

- Upgrade header: value of h2 or h2c. But that doesn't matter because the server need to read the header => not using TLS => chicken & egg problem
- TLS Server Name header during negotiation because the Host header cannot be decrypted before TLS is established


### Quiz

- True or False: HTTP/2 was approved AFTER Speedy was deprecated
  - True
  - **False**
- HPACK deals with what area of HTTP
  - Multipathing
  - **Compression**
  - Binary Protocol
  - Server Push 
- True or False: HTTP/2 is present in all new major browsers
  - **True**
  - False 
- What was the name of the attack that targeted previous versions of TLS
  - HATE
  - **CRIME**
  - FAIL
  - SAIL
- True or False: The upgrade header is the most common way HTTP/2 is initiated
  - True
  - **False**