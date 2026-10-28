1| <div align="center">
2| 
3| # 🛡️ PortSwigger Web Security Academy — Lab Journey
4| 
5| ### `awel@astu:~$` tracking every vulnerability, one lab at a time 
6| 
7| [![Total Labs](https://img.shields.io/badge/Total%20Labs-240%20tracked-22d3ee?style=for-the-badge&logo=hackthebox&logoColor=white)](#-solved-labs)
8| [![Apprentice](https://img.shields.io/badge/Apprentice-50%2F61-3fb950?style=for-the-badge)](#-level-progress)
9| [![Practitioner](https://img.shields.io/badge/Practitioner-97%2F174-f5a524?style=for-the-badge)](#-level-progress)
10| [![Expert](https://img.shields.io/badge/Expert-9%2F39-f85149?style=for-the-badge)](#-level-progress)
11| [![Last Updated](https://img.shields.io/badge/Last%20Updated-Oct%2028%202026-0891b2?style=for-the-badge)](#-solved-labs)
12| 
13| **[🌐 Portfolio](https://awel-abduljelil.netlify.app/) · [💻 GitHub](https://github.com/Awel-Abduljelil) · [✍️ Writeups on Medium](https://medium.com/@awela1499) · [📡 Telegram](https://t.me/Awexaa)**
14| 
15| </div>
16| 
17| ---
18| 
19| ## `//` about
20| 
21| This repo documents my hands-on progress through **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — the same curriculum used by working AppSec engineers and pentesters to sharpen real-world exploitation skills.
22| 
23| Every lab here was solved manually using **Burp Suite**, browser dev tools, and an HTTP proxy — no walkthroughs copy-pasted, no shortcuts. The goal is to build the same instincts a professional penetration tester uses during assessments.
24| 
25| This journey feeds directly into my [portfolio](https://awel-abduljelil.netlify.app/) and CTF work — think of this repo as the lab notebook behind the "Penetration Tester" title on that profile.
26| 
27| ---
28| 
29| ## `//` level progress
30| 
31| | Rank | Progress | Completion |
32| |---|---|---|
33| | 🟢 **Apprentice** | `████████████████████░░░░░` | **50 / 61** |
34| | 🟡 **Practitioner** | `██████████████████░░░░░░░` | **97 / 174** |
35| | 🔴 **Expert** | `██████░░░░░░░░░░░░░░░░░░` | **9 / 39** |
36| 
37| ---
38| 
39| ## `//` categories covered
40| 
41| | Category | Solved / Total | Status |
42| |---|---:|---|
43| | SQL injection | 18 / 18 | ✅ Complete |
44| | Cross-site scripting (XSS) | 30 / 30 | ✅ Complete |
45| | Cross-site request forgery (CSRF) | 11 / 11 | ✅ Complete |
46| | Clickjacking | 5 / 5 | ✅ Complete |
47| | DOM-based vulnerabilities | 7 / 7 | ✅ Complete |
48| | Cross-origin resource sharing (CORS) | 3 / 3 | ✅ Complete |
49| | XML external entity (XXE) injection | 0 / 9 | ⬜ Not started |
50| | Server-side request forgery (SSRF) | 5 / 7 | 🟡 In progress |
51| | HTTP request smuggling | 0 / 22 | ⬜ Not started |
52| | OS command injection | 5 / 5 | ✅ Complete |
53| | Server-side template injection | 0 / 6 | ⬜ Not started |
54| | Path traversal | 6 / 6 | ✅ Complete |
55| | Access control vulnerabilities | 5 / 7 | 🟡 In progress |
56| | Authentication | 12 / 13 | 🟡 In progress |
57| | WebSockets | 3 / 3 | ✅ Complete |
58| | Web cache poisoning | 0 / 13 | ⬜ Not started |
59| | Insecure deserialization | 0 / 10 | ⬜ Not started |
60| | Information disclosure | 5 / 5 | ✅ Complete |
61| | Business logic vulnerabilities | 0 / 10 | ⬜ Not started |
62| | HTTP Host header attacks | 0 / 6 | ⬜ Not started |
63| | OAuth authentication | 0 / 6 | ⬜ Not started |
64| | File upload vulnerabilities | 6 / 7 | 🟡 In progress |
65| | JWT | 2 / 8 | 🟡 In progress |
66| | Prototype pollution | 0 / 10 | ⬜ Not started |
67| | GraphQL API vulnerabilities | 5 / 5 | ✅ Complete |
68| | Race conditions | 5 / 5 | ✅ Complete |
69| | NoSQL injection | 0 / 4 | ⬜ Not started |
70| | API testing | 4 / 5 | 🟡 In progress |
71| | Web LLM attacks | 0 / 8 | ⬜ Not started |
72| | Web cache deception | 4 / 5 | 🟡 In progress |
73| 
74| > Status legend: ✅ Complete = all labs in the category are solved. 🟡 In progress = at least one lab is solved but the category is not complete. ⬜ Not started = no labs in the category have been solved yet.
75| 
76| ---
77| 
78| ## `//` tools of the trade
79| 
80| <div align="left">
81| 
82| ![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white)
83| ![DevTools](https://img.shields.io/badge/Browser%20DevTools-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
84| ![HTTP Proxy](https://img.shields.io/badge/HTTP%20Proxy-22d3ee?style=flat-square)
85| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
86| 
87| </div>
88| 
89| ---
90| 
91| ## `//` how to read this table
92| 
93| | Field | Meaning |
94| |---|---|
95| | `Solved / Total` | Number of labs solved in that category out of the total available |
96| | `Status` | `✅ Complete`, `🟡 In progress`, or `⬜ Not started` |
97| 
98| > Categories with no solved labs are shown as `⬜ Not started`, while categories with at least one solved lab are shown as `🟡 In progress` until all labs are complete.
99| 
100| 
101| ## see table below
102| ---
103| 
104| 
105| | No | Date | Topic | Lab Title | Difficulty | Writeup |
106| |---|---|---|---|---|---|
107| | 1 | 2026-06-10 | Web cache deception | Exploiting path mapping for web cache deception | Apprentice | N/A |
108| | 2 | 2026-06-10 | Web cache deception | Exploiting path delimiters for web cache deception | Practitioner | N/A |
109| | 3 | 2026-06-10 | Web cache deception | Exploiting origin server normalization for web cache deception | Practitioner | N/A |
110| | 4 | 2026-06-10 | Web cache deception | Exploiting cache server normalization for web cache deception | Practitioner | N/A |
111| | 5 | 2026-06-11 |   SSRF | Basic SSRF against the local server | Apprentice | N/A |
112| | 6 | 2026-06-11 |   SSRF | Basic SSRF against another back-end system | Apprentice | N/A |
113| | 7 | 2026-06-11 |   SSRF | SSRF with blacklist-based input filter | Practitioner | N/A |
114| | 8 | 2026-06-11 |   SSRF | SSRF with filter bypass via open redirection vulnerability | Practitioner | N/A |
115| | 9 | 2026-06-11 |   SSRF | Blind SSRF with out-of-band detection | Practitioner | N/A |
116| | 10 | 2026-06-12 | Authentication | Username enumeration via different responses | Apprentice | [writeup](https://medium.com/@awela1499/username-enumeration-via-different-responses-portswigger-lab-17f768468f17?source=collection_category---) |
117| | 11 | 2026-06-12 | Authentication | Username enumeration via subtly different responses | Practitioner | N/A |
118| | 12 | 2026-06-12 | Authentication | Username enumeration via response timing | Practitioner | N/A |
119| | 13 | 2026-06-12 | Authentication | Broken brute-force protection, IP block | Practitioner | N/A |
120| | 14 | 2026-06-13 | Authentication | 2FA simple bypass | Apprentice | N/A |
121| | 15 | 2026-06-13 | Authentication | 2FA broken logic | Practitioner | N/A |
122| | 16 | 2026-06-13 | Authentication | Brute-forcing a stay-logged-in cookie | Practitioner | N/A |
123| | 17 | 2026-06-13 | Authentication | Offline password cracking | Practitioner | N/A |
124| | 18 | 2026-06-13 | Authentication | Password reset broken logic | Apprentice | N/A |
125| | 19 | 2026-06-13 | Authentication | Password reset poisoning via middleware | Practitioner | N/A |
126| | 20 | 2026-06-13 | Authentication | Password brute-force via password change | Practitioner | N/A |
127| | 21 | 2026-06-14 |   Clickjacking | Basic clickjacking with CSRF token protection | Apprentice | N/A |
128| | 22 | 2026-06-14 |   Clickjacking | Clickjacking with form input data prefilled from a URL parameter | Apprentice | N/A |
129| | 23 | 2026-06-14 |   Clickjacking | Clickjacking with a frame buster script | Apprentice | N/A |
130| | 24 | 2026-06-14 |   Clickjacking | Exploiting clickjacking to trigger DOM-based XSS | Practitioner | N/A |
131| | 25 | 2026-06-14 |   Clickjacking | Multistep clickjacking | Practitioner | N/A |
132| | 26 | 2026-06-16 | SQL injection | SQLi in WHERE clause allowing retrieval of hidden data | Apprentice | N/A |
133| | 27 | 2026-06-16 | SQL injection | SQLi vulnerability allowing login bypass | Apprentice | N/A |
134| | 28 | 2026-06-16 | SQL injection | UNION attack — determining the number of columns | Practitioner | N/A |
135| | 29 | 2026-06-16 | SQL injection | UNION attack — finding a column containing text | Practitioner | N/A |
136| | 30 | 2026-06-16 | SQL injection | UNION attack — retrieving data from other tables | Practitioner | N/A |
137| | 31 | 2026-06-16 | SQL injection | UNION attack — retrieving multiple values in a single column | Practitioner | N/A |
138| | 32 | 2026-06-17 | SQL injection | Querying the database type and version (MySQL/MS-SQL) | Practitioner | N/A |
139| | 33 | 2026-06-17 | SQL injection | Listing the database contents on non-Oracle databases | Practitioner | N/A |
140| | 34 | 2026-06-19 | Path traversal | File path traversal, simple case | Apprentice | N/A |
141| | 35 | 2026-06-19 |   Access control | Unprotected admin functionality | Apprentice | N/A |
142| | 36 | 2026-06-19 |   Access control | Unprotected admin functionality with unpredictable URL | Apprentice | N/A |
143| | 37 | 2026-06-19 |   Access control | User role controlled by request parameter | Apprentice | N/A |
144| | 38 | 2026-06-19 |   Access control | User ID controlled by request parameter, unpredictable IDs | Apprentice | N/A |
145| | 39 | 2026-06-19 |   Access control | User ID controlled by request parameter with password disclosure | Apprentice | N/A |
146| | 40 | 2026-06-20 | SQL injection | Blind SQLi with conditional responses | Practitioner | N/A |
147| | 41 | 2026-06-20 | SQL injection | Blind SQLi with conditional errors | Practitioner | N/A |
148| | 42 | 2026-06-20 | SQL injection | Visible error-based SQL injection | Practitioner | N/A |
149| | 43 | 2026-06-21 | SQL injection | Blind SQLi with time delays and information retrieval | Practitioner | N/A |
150| | 44 | 2026-06-22 | SQL injection | SQLi with filter bypass via XML encoding | Practitioner | N/A |
151| | 45 | 2026-06-23 |   File upload | Remote code execution via web shell upload | Apprentice | N/A |
152| | 46 | 2026-06-23 |   File upload | Web shell upload via Content-Type restriction bypass | Apprentice | N/A |
153| | 47 | 2026-06-23 |   File upload | Web shell upload via path traversal | Practitioner | N/A |
154| | 48 | 2026-06-23 |   File upload | Web shell upload via extension blacklist bypass | Practitioner | N/A |
155| | 49 | 2026-06-24 |   File upload | Web shell upload via obfuscated file extension | Practitioner | N/A |
156| | 50 | 2026-06-24 |   File upload | Remote code execution via polyglot web shell upload | Practitioner | N/A |
157| | 51 | 2026-06-24 | Path traversal | Traversal sequences blocked with absolute path bypass | Practitioner | N/A |
158| | 52 | 2026-06-24 | Path traversal | Traversal sequences stripped non-recursively | Practitioner | N/A |
159| | 53 | 2026-06-24 | Path traversal | Traversal sequences stripped with superfluous URL-decode | Practitioner | N/A |
160| | 54 | 2026-06-24 | Path traversal | Validation of start of path | Practitioner | N/A |
161| | 55 | 2026-06-24 | Path traversal | Validation of file extension with null byte bypass | Practitioner | N/A |
162| | 56 | 2026-06-25 |   API testing | Exploiting an API endpoint using documentation | Apprentice | N/A |
163| | 57 | 2026-06-25 |   API testing | Finding and exploiting an unused API endpoint | Practitioner | N/A |
164| | 58 | 2026-06-26 |   API testing | Exploiting a mass assignment vulnerability | Practitioner | N/A |
165| | 59 | 2026-06-26 |   API testing | Exploiting server-side parameter pollution in a query string | Practitioner | N/A |
166| | 60 | 2026-06-27 | OS Command injection | OS command injection, simple case | Apprentice | N/A |
167| | 61 | 2026-06-27 | OS Command injection | Blind OS command injection with time delays | Practitioner | N/A |
168| | 62 | 2026-06-27 | OS Command injection | Blind OS command injection with output redirection | Practitioner | N/A |
169| | 63 | 2026-07-01 |   GraphQL API vulnerabilities| Accessing private GraphQL posts | Apprentice | N/A |
170| | 64 | 2026-07-06 |   GraphQL API vulnerabilities| Accidental exposure of private GraphQL fields | Practitioner | N/A |
171| | 65 | 2026-08-03 |SQL injection | SQL injection attack, querying the database type and version on Oracle| Practitioner | N/A |
172| | 66 | 2026-08-03 |  Information disclosure | Information disclosure vulnerabilities| Apprentice | N/A |
173| | 67 | 2026-08-03 |  Information disclosure | Source code disclosure via backup files| Apprentice | N/A |
174| | 68 | 2026-08-03 |  Information disclosure | Information disclosure on debug page| Apprentice | N/A |
175| | 69 | 2026-08-03 |  Information disclosure | Authentication bypass via information disclosure| Apprentice | N/A |
176| | 70 | 2026-08-03 |  Information disclosure | information disclosure in version control history | Practitioner | N/A |
177| | 71 | 2026-08-04 | CSRF |  CSRF vulnerability with no defenses | Apprentice | N/A |
178| | 72 | 2026-08-04 | CSRF |  CSRF where token validation depends on request method | Practitioner | N/A |
179| | 73 | 2026-08-04 | CSRF | CSRF where token validation depends on token being present  | Practitioner | N/A |
180| | 74 | 2026-08-05 | CSRF | CSRF where token is not tied to user session PRACTITIONER | Practitioner | N/A |
181| | 75 | 2026-08-06 |   WebSockets vulnerabilities |Manipulating WebSocket messages to exploit vulnerabilities| APPRENTICE  | N/A |
182| | 80 | 2026-09-10 |   CSRF | CSRF where token is tied to non-session cookie  | PRACTITIONER  | N/A |
183| | 81 | 2026-09-10 |   CSRF | CSRF where token is duplicated in cookie | PRACTITIONER  | N/A |
184| | 82 | 2026-09-13 |   CSRF | SameSite Lax bypass via method override| PRACTITIONER  | N/A |
185| | 83 | 2026-09-13 |   CSRF |SameSite Strict bypass via client-side redirect| PRACTITIONER  | N/A |
186| | 84 | 2026-09-13 | WebSockets vulnerabilities |Manipulating WebSocket messages to exploit vulnerabilities | APPRENTICE  | N/A |
187| | 85 | 2026-09-13 | WebSockets vulnerabilities |Manipulating the WebSocket handshake to exploit vulnerabilities| PRACTITIONER  | N/A |
188| | 86 | 2026-09-13 | WebSockets vulnerabilities | Cross-site WebSocket hijacking | PRACTITIONER  | N/A |
189| | 87 | 2026-09-13 |   CSRF |SameSite Strict bypass via sibling domain| PRACTITIONER  | N/A |
190| | 88 | 2026-09-13 |   CSRF |CSRF where Referer validation depends on header being present | PRACTITIONER  | N/A |
191| | 89 | 2026-09-13 |   CSRF |CSRF with broken Referer validation | PRACTITIONER  | N/A |
192| | 90 | 2026-10-12 | CORS |CORS vulnerability with basic origin reflection | APPRENTICE  | N/A |
193| | 91 | 2026-10-12 | CORS |CORS vulnerability with trusted null origin | APPRENTICE  | N/A |
194| | 92 | 2026-10-12 | CORS |CORS vulnerability with trusted insecure protocols | PRACTITIONER  | N/A |
195| | 93 | 2026-10-24 |   Race Condition |Limit overrun race conditions |  APPRENTICE  | N/A |
196| | 94 | 2026-10-24 |   Race Condition |Bypassing rate limits via race conditions |  PRACTITIONER  | N/A |
197| | 95 | 2026-10-24 |   Race Condition |Multi-endpoint race conditions |  PRACTITIONER  | N/A |
198| | 96 | 2026-10-24 |   Race Condition |Single-endpoint race conditions |  PRACTITIONER  | N/A |
199| | 97 | 2026-10-25 |   Race Condition |Exploiting time-sensitive vulnerabilities |  PRACTITIONER  | N/A |
200| | 98 | 2026-10-25 | OS Command injection |Blind OS command injection with out-of-band interaction | Practitioner | N/A |
201| | 99 | 2026-10-25 | OS Command injection |Blind OS command injection with out-of-band data exfiltration | Practitioner | N/A |
202| | 100 | 2026-10-28 | Access control | User role can be modified in user profile | Apprentice | N/A |
203| | 101 | 2026-10-28 | Access control | User ID controlled by request parameter with data leakage in redirect | Apprentice | N/A |
204| | 102 | 2026-10-28 | Access control | Insecure direct object references | Apprentice | N/A |
205| | 103 | 2026-10-28 | Access control | URL-based access control can be circumvented | Practitioner | N/A |
206| | 104 | 2026-10-28 | Access control | Method-based access control can be circumvented | Practitioner | N/A |
207| | 105 | 2026-10-28 | Authentication | Username enumeration via account lock | Practitioner | N/A |
208| | 106 | 2026-10-28 | Authentication | Broken brute-force protection, multiple credentials per request | Expert | N/A |
209| | 107 | 2026-10-28 | HTTP Host header attacks | Basic password reset poisoning | Apprentice | N/A |
210| | 108 | 2026-10-28 | Business logic vulnerabilities | Excessive trust in client-side controls | Apprentice | N/A |
211| | 109 | 2026-10-28 | Business logic vulnerabilities | High-level logic vulnerability | Apprentice | N/A |
212| | 110 | 2026-10-28 | Server-side template injection | Basic server-side template injection | Practitioner | N/A |
213| | 111 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages | Practitioner | N/A |
214| | 112 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages and a JavaScript URL | Practitioner | N/A |
215| | 113 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages and JSON.parse | Practitioner | N/A |
216| | 114 | 2026-10-28 | DOM-based vulnerabilities | DOM-based open redirection | Practitioner | N/A |
217| | 115 | 2026-10-28 | DOM-based vulnerabilities | DOM-based cookie manipulation | Practitioner | N/A |
218| | 116 | 2026-10-28 | DOM-based vulnerabilities | Exploiting DOM clobbering to enable XSS | Expert | N/A |
219| | 117 | 2026-10-28 | DOM-based vulnerabilities | Clobbering DOM attributes to bypass HTML filters | Expert | N/A |
220| | 118 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with nothing encoded | Apprentice | N/A |
221| | 119 | 2026-10-28 | Cross-site scripting | Stored XSS into HTML context with nothing encoded | Apprentice | N/A |
222| | 120 | 2026-10-28 | Cross-site scripting | DOM XSS in document.write sink using source location.search | Apprentice | N/A |
223| | 121 | 2026-10-28 | Cross-site scripting | DOM XSS in innerHTML sink using source location.search | Apprentice | N/A |
224| | 122 | 2026-10-28 | Cross-site scripting | DOM XSS in jQuery anchor href attribute sink using location.search source | Apprentice | N/A |
225| | 123 | 2026-10-28 | Cross-site scripting | DOM XSS in jQuery selector sink using a hashchange event | Apprentice | N/A |
226| | 124 | 2026-10-28 | Cross-site scripting | Reflected XSS into attribute with angle brackets HTML-encoded | Apprentice | N/A |
227| | 125 | 2026-10-28 | Cross-site scripting | Stored XSS into anchor href attribute with double quotes HTML-encoded | Apprentice | N/A |
228| | 126 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with angle brackets HTML encoded | Apprentice | N/A |
229| | 127 | 2026-10-28 | Cross-site scripting | DOM XSS in document.write sink using source location.search inside a select element | Practitioner | N/A |
230| | 128 | 2026-10-28 | Cross-site scripting | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | Practitioner | N/A |
231| | 129 | 2026-10-28 | Cross-site scripting | Reflected DOM XSS | Practitioner | N/A |
232| | 130 | 2026-10-28 | Cross-site scripting | Stored DOM XSS | Practitioner | N/A |
233| | 131 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with most tags and attributes blocked | Practitioner | N/A |
234| | 132 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with all tags blocked except custom ones | Practitioner | N/A |
235| | 133 | 2026-10-28 | Cross-site scripting | Reflected XSS with some SVG markup allowed | Practitioner | N/A |
236| | 134 | 2026-10-28 | Cross-site scripting | Reflected XSS in canonical link tag | Practitioner | N/A |
237| | 135 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with single quote and backslash escaped | Practitioner | N/A |
238| | 136 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped | Practitioner | N/A |
239| | 137 | 2026-10-28 | Cross-site scripting | Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped | Practitioner | N/A |
240| | 138 | 2026-10-28 | Cross-site scripting | Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped | Practitioner | N/A |
241| | 139 | 2026-10-28 | Cross-site scripting | Exploiting cross-site scripting to steal cookies | Practitioner | N/A |
242| | 140 | 2026-10-28 | Cross-site scripting | Exploiting cross-site scripting to capture passwords | Practitioner | N/A |
243| | 141 | 2026-10-28 | Cross-site scripting | Exploiting XSS to bypass CSRF defenses | Practitioner | N/A |
244| | 142 | 2026-10-28 | Cross-site scripting | Reflected XSS with AngularJS sandbox escape without strings | Expert | N/A |
245| | 143 | 2026-10-28 | Cross-site scripting | Reflected XSS with AngularJS sandbox escape and CSP | Expert | N/A |
246| | 144 | 2026-10-28 | Cross-site scripting | Reflected XSS with event handlers and href attributes blocked | Expert | N/A |
247| | 145 | 2026-10-28 | Cross-site scripting | Reflected XSS in a JavaScript URL with some characters blocked | Expert | N/A |
248| | 146 | 2026-10-28 | Cross-site scripting | Reflected XSS protected by very strict CSP, with dangling markup attack | Practitioner | N/A |
249| | 147 | 2026-10-28 | Cross-site scripting | Reflected XSS protected by CSP, with CSP bypass | Expert | N/A |
250| | 150 | 2026-10-28 | JWT | JWT authentication bypass via unverified signature | Apprentice | N/A |
251| | 151 | 2026-10-28 | JWT | JWT authentication bypass via flawed signature verification | Apprentice | N/A |
252| | 152 | 2026-10-28 | GraphQL API vulnerabilities | Performing CSRF exploits over GraphQL | Practitioner | N/A |
253| 
254| ## `//` what's next
255| 
256| - [ ] Finish remaining **SSRF** labs (2 left)
257| - [ ] Finish remaining **XXE** labs (9 left)
258| - [ ] Finish remaining **HTTP request smuggling** labs (22 left)
259| - [ ] Finish remaining **SSTI** labs (6 left)
260| - [ ] Finish remaining **Authentication** labs (1 left)
261| - [ ] Finish remaining **Web cache poisoning** labs (13 left)
262| - [ ] Finish remaining **Business logic** labs (10 left)
263| - [ ] Finish remaining **JWT** labs (6 left)
264| - [ ] Finish the **Prototype pollution** track (10 left)
265| - [ ] Finish **NoSQL injection** labs (4 left)
266| - [ ] Finish **API testing** labs (1 left)
267| - [ ] Finish **Web LLM** labs (8 left)
268| - [ ] Finish **Web cache deception** labs (1 left)
269| 
270| ---
271| 
272| ## `//` connect
273| 
274| <div align="left">
275| 
276| [![Portfolio](https://img.shields.io/badge/Portfolio-0891b2?style=for-the-badge&logo=firefox&logoColor=white)](https://awel-abduljelil.netlify.app/)
277| [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Awel-Abduljelil)
278| [![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Awexaa)
279| [![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://www.x.com/Aweljelil49555)
280| 
281| </div>
282| 
283| <div align="center">
284| <sub>Built lab by lab. No shortcuts, no copy-paste writeups — just hands-on practice.</sub>
285| </div>
286| 