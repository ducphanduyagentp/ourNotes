# Browser Defenses

## Introduction to Client Side

- Old days: HTML, FTP, Gopher
- Threats:
  - Malicious clients => servers
  - Malicious servers => clients
  - Malicious users => other users
  - Malicious users => website maintainers
  - Malicious clients => intermediate servers: cache poisoning

### Quiz (60/100)

- We talked about multiple parsers on the client side, which wasnt one?
  - **DOM Parser**
  - CSS Parser
  - JS Parser
  - HTML Parser
- Who did we say was, at least partially, responsible for lack of browser security?
  - Government
  - NSA
  - **Browser Developers**
  - Developers
- Which of the following attacks did we say browsers can attempt to mitigate?
  - SQL Injection
  - **Clickjacking**
  - Log Injection
  - Remote Code Execution
- True or False: All web server side langugues must integrate with web servers?
  - True
  - **False**
- How do some browsers try and help prevent malware distrubtion?
  - Artifical Inteligence
  - **Blacklists**
  - Javascript Injection
  - anual Review

## The DOM

### Browser isolation

- Generally webapps run in isolated sandboxes
- In many webapps, there are mix of trusted and untrusted contents
- Trust boundary
- User experience

## The document

- Maintains by W3C
- Represented in a tree with the document is the root
- A standard now, but browsers still may have minor differences

### Quiz (80/100)

- The DOM is conceptually what type of data structure
  - List
  - Set
  - **Tree**
  - Array
- Which organization maintains the DOM standard
  - Mozilla
  - **W3C**
  - IETF
  - RFC
- What is the root of the DOM
  - **Document**
  - Root
  - Page
  - $
- True or False: Standardization means all browsers use the same DOM modeling?
  - **True**
  - False
- True or False: The DOM was originally designed to manage Javescript interaction?
  - **True**
  - False

## Manipulating the DOM

- Accessed and manipulated by JavaScript.
- Accessing via:
  - Walking the tree
  - By ID
  - XPath
- AJAX (Asynchronous JavaScript and XML)
  - XMLHttpRequest: GET or POST
  - Using jQuery `$.get`
- Security issues
  - DOM-based XSS
  - Prevent by Same Origin Policy

### Quiz

- Objects in the DOM can be referenced by all of the following except?
  - Exact path
  - Numerical position
  - Their relationship to nodes
  - **Alphabetical order**
- When you assign an Element to a variable what base type does it have?
  - String
  - **Object**
  - Reference
  - Array
- AJAX is based on which underlying JavaScript function?
  - $.get
  - **XMLHttpRequest**
  - MakeRequest
  - HTTPRequest
- XPath is a method for ______
  - Experimental mapping between locations
  - Validating the URL that was used in the DOM
  - Exploiting DOM security weaknesses
  - **Addressing objects in the DOM**
- True or False: Loading Javascript from a remote site has security ramifications?
  - **True**
  - False

## Same Origin Policy

- From Netscape, same time as JavaScript, to prevent access across domains
- May not access any origin outside your own
- Origin by RFC 6454
  - Scheme: HTTP, HTTPS, FTP, etc.
  - Host: domain, www.x.com != x.com
  - Port
- Allowed to make the requests but not reading the content
- A good idea is to store each person on a separate sub-domain or domain
- Exceptions:
  - Reading: NO
  - Writing: Generally allowed, links, forms
  - Embedding: Embedded from google, etc.

### Quiz (80/100)

- Same Origin Policy was introducted by?
  - Mozilla
  - Microsoft
  - Google
  - **Netscape**
- Which of the following doesnt violate SOP for http://cnn.com
  - http://cnn.com:8080
  - http://www.cnn.com
  - **http://cnn.com:80/test/info.php**
  - https://cnn.com
- True or False: Cross origin writing is generally allowed?
  - **True**
  - False
- third party image tags are considered what?
  - Reading
  - Writing
  - **Embedding**
  - Scripting
- SOP policy is needed because _____
  - HTTP has protocol flaws
  - Browsers store state
  - **Javascript is insecure**
  - Applications are poorly designed

## Same Origin Policy Exception

### Bypassing SOP

- JSONP: Embed JSON data and parse it
- Document.Domain: Modifying the origin domain, top level domains are not allowed. Set the same superdomain on both hosts.
- CORS (Cross Origin Resource Sharing)
  - AJAX sends out an OPTIOIN request with headers
    - Origin
    - Access-Control-Allow-Methods
    - Access-Control-Allow-Credetials
    - Access-Control-Allow-Headers
  - Server response headers
    - Access-Control-Allow-Origin
  - If credentials are sent, * is not allowed
  - W3C recommended by 2014
- PostMessage environment: newest
  - HTML5
  - Sending text messages across domains
  - Stars are bad
- Others:
  - Flash: crossdomain.xml for swf files
  - Acrobat
- Cookies have their own SOP

### Quiz

- Which of the following is the W3C reccomendation?
  - PostMessage
  - Document.domain
  - **CORS**
  - JSONP
- True or False: PostMessages are secure by default
  - True
  - **False**
- CORS causes each cross-site request to send a ______ header.
  - From
  - **Origin**
  - CORS
  - Destination
- Document.domain is configured how?
  - HTML Metatag
  - **JavaScript**
  - Request Headers
  - Response
- The Flash filename we mentioned for configuring SOP expansion was ______
  - Sameorigin.xml
  - Crossorigin.xml
  - **Crossdomain.xml**
  - Samedomain.xml

## Cookie Security

- SOP for Cookies
  - Domain
  - Path
  - Force https
- Implied options: If domain and path are unset, they default to the URL that set them
- Scopes
  - Set bob.rit.edu => rit.edu won't see
  - Set rit.edu => bob.rit.edu will see
  - rit.edu can set rit.edu
  - rit.edu can't set bob.rit.edu
  - bob.rit.edu can set bob.rit.edu
- Cookies Uniqueness
  - Same name, different values
  - Cookie shadowing, a valid attack
  - Both are stored
- Public Suffix list
  - TLDs are not just 1 after the root. `.co.uk` is a TLD
  - eTLD: effective TLD
  - This list contains domains that are **treated** as TLDs
- Security related Cookie options
  - Secure: Sent over SSL
  - HTTPOnly: Client-side scripts can't access cookies
  - SameSite: Prevent cookies from being sent across domains, by Google
    - Strict
    - Lax: Only prevent in POST
- Additional issues
  - Path separation: SOP doesn't care about path
  - HTTP can set cookie for HTTPS sessions
  - Port: cnn.com:8000 will be given on cnn.com
  - Tampering: on client side. To secure, use encryption or integrity controls
- GPC: Get-Post Cookie
  - Server side
  - ASP, PHP receive params in the cookie

### Quiz

- Which aspect of cookies origin is unique compared to SOP
  - Host
  - Port
  - **Path**
  - Scheme
- True or False: Any part of the super domain is allowed in the domain option?
  - True
  - **False**
- The e in eTLD stands for?
  - Encapsulated
  - Enquire
  - Essential
  - **Effective**
- True or False: The public suffix list contains things beyond TLDs?
  - **True**
  - False
- The HTTPOnly cookie option means?
  - Cookies can only be accessed over TLS
  - **Cookes cant be accessed via Javascript**
  - Cookies will only be sent if you came from the same domain
  - Cookies will not be sent on AJAX requests
- Aspects
  - Policy Delivery
  - Policy Directives
  - Violation reports
- If multiple policies are provided, use the one with least privilege
- Directives in CSP 1.0
  - default-src
  - script-src
  - object-src
  - img-src
  - media-src
  - style-src
  - font-src
  - xhr-src
  - frame-ancestors
  - report-uri

## Intro to Content Security Policy

- Trust in the content that are embeded
- CSP: probably whitelisting
  - **Content-Security-Policy** header
  - `<meta http-equiv="Content-Security-Policy>`
- Disabled by default
  - Evaluation of strings in JS
    - Inline `setTimeout` and `setInterval`
    - New functions
    - eval
  - Data URIs, pseudo URLs
  - Inline JS, foreign scripts

### Quiz

- True or False: CSP can be enabled in multiple ways
  - **True**
  - False
- CSP supports all of the following aspects, EXCEPT
  - Policy Delivery
  - **Policy Enforcment**
  - Policy Directives
  - Violation Reporting
- CSP by default disables all of the following EXCEPT
  - Inline Javascript
  - **Javascript inclusion**
  - PsuedoURLs
  - Eval Functions
- The C in CSP stands for _____
  - Complete
  - Call-based
  - Caution
  - **Content**
- Which of the following is NOT a valid CSP directive?
  - **dest-src**
  - img-src
  - xhr-src
  - script-src

## A Deeper Look at CSP

- CSP directives
  - default-src: **Overwrites** all the directive ends with `src`
  - script-src: script.src
  - object-src: object.data, embed.src, applet.code, applet.archive
  - img-src: img.src
  - media-src: media.src, audio.src
  - style-src: `<link rel="stylesheet">.href` (background images, icons, etc.)
  - child-src: iframe.src
  - font-src: @font-face.src
  - connect-src: XHR, WebSockets, EventSource
  - frame-ancestors: specifies domains from which content will be able to utilize iframe, frame, object. Anti-clickjacking as X-Frame-Options
  - report-uri: Where the JSON report goes to
  - Upgrade-insecure-requests: Only use HTTPS instead of HTTP
  - sandbox
  - base-uri
  - plugin-types
  - form-action
- The frame-ancestors, report-uri and sandbox has 2 ways to specify
- HSTS: Strict-Transport-Security header
  - includeSubDomains
  - max-age
  - Chrome also has a preload option, a hardcoded list of sites that must use HTTPS
- Sandbox attribute on iframes:
  - JS isn't executed
  - Unique origin
  - The document cannot create new windows
  - No form submission
  - No plugins

### Using CSP

- Sent on per request basis
- Keyword:
  - none: match nothing
  - self: match the current origin only, not its subdomain
  - unsafe-inline: allow inline JS, CSS
  - unsafe-eval: allow text-to-JS like eval
- Enable inline script
  - Specifying a nonce: a hash of the script
- Reporting
  - document-uri
  - referrer
  - blocked-uri
  - violated-directive
  - original-policy
- Can specify CSP-report only

### Quiz (80/100)

- Which of the following is NOT part of the JSON reporting structure?
  - Document-uri
  - Referrer
  - **Origin**
  - Original-Policy
- True or False: Without using unsafe-inline, it isnt possible tp allow inline JS
  - True
  - **False**
- The HSTS standard requires that when a header is present HTTPS is always used
  - **True**
  - False
- Using CSP sandbox directive will NOT add the following security?
  - Prohibit JavaScript execution
  - Put the site into a unique origin
  - **Links cannot be clicked on**
  - Plugins will not be loaded
- The first S in HSTS stands for _________
  - Security
  - **Strict**
  - Suppliment
  - Standard

## Do Not Track

### Quiz (80/100)

- DNT stands for ____ ____ ____
  - Deny Network Tracking
  - **Do Not Track**
  - Distributed Node Tracking
  - Detailed Number Tracker
- True or False: Multiple browsers enable DNT tokens by default
  - True
  - **False**
- True or False: DNT is enabled on most modern browsers
  - True
  - **False**
- This data was based on a presentation at what conference?
  - Defcon
  - Blackhat
  - **AppSec**
  - Shmoocon
- On most browsers it takes ____ steps to enable DNT
  - 0-4
  - **4-8**
  - 8-12
  - 12-16