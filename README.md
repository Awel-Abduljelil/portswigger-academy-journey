<div align="center">

# 🛡️ PortSwigger Web Security Academy — Lab Journey

### `awel@astu:~$` tracking every vulnerability, one lab at a time 

[![Total Labs](https://img.shields.io/badge/Total%20Labs-240%20tracked-22d3ee?style=for-the-badge&logo=hackthebox&logoColor=white)](#-solved-labs)
[![Apprentice](https://img.shields.io/badge/Apprentice-50%2F61-3fb950?style=for-the-badge)](#-level-progress)
[![Practitioner](https://img.shields.io/badge/Practitioner-97%2F174-f5a524?style=for-the-badge)](#-level-progress)
[![Expert](https://img.shields.io/badge/Expert-9%2F39-f85149?style=for-the-badge)](#-level-progress)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Oct%2028%202026-0891b2?style=for-the-badge)](#-solved-labs)

**[🌐 Portfolio](https://awel-abduljelil.netlify.app/) · [💻 GitHub](https://github.com/Awel-Abduljelil) · [✍️ Writeups on Medium](https://medium.com/@awela1499) · [📡 Telegram](https://t.me/Awexaa)**

</div>

---

## `//` about

This repo documents my hands-on progress through **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — the same curriculum used by working AppSec engineers and pentesters to sharpen real-world exploitation skills.

Every lab here was solved manually using **Burp Suite**, browser dev tools, and an HTTP proxy — no walkthroughs copy-pasted, no shortcuts. The goal is to build the same instincts a professional penetration tester uses during assessments.

This journey feeds directly into my [portfolio](https://awel-abduljelil.netlify.app/) and CTF work — think of this repo as the lab notebook behind the "Penetration Tester" title on that profile.

---

## `//` level progress

| Rank | Progress | Completion |
|---|---|---|
| 🟢 **Apprentice** | `████████████████████░░░░░` | **50 / 61** |
| 🟡 **Practitioner** | `██████████████████░░░░░░░` | **97 / 174** |
| 🔴 **Expert** | `██████░░░░░░░░░░░░░░░░░░` | **9 / 39** |

---

## `//` categories covered

| Category | Solved / Total | Status |
|---|---:|---|
| SQL injection | 18 / 18 | ✅ Complete |
| Cross-site scripting (XSS) | 18 / 18 | ✅ Complete |
| Cross-site request forgery (CSRF) | 11 / 11 | ✅ Complete |
| Clickjacking | 5 / 5 | ✅ Complete |
| DOM-based vulnerabilities | 7 / 7 | ✅ Complete |
| Cross-origin resource sharing (CORS) | 3 / 3 | ✅ Complete |
| OS command injection | 5 / 5 | ✅ Complete |
| Path traversal | 6 / 6 | ✅ Complete |
| Access control vulnerabilities | 11 / 13 | 🟡 In progress |
| Authentication | 12 / 13 | 🟡 In progress |
| WebSockets | 3 / 3 | ✅ Complete |
| Information disclosure | 5 / 5 | ✅ Complete |
| Race conditions | 5 / 5 | ✅ Complete |
| GraphQL API vulnerabilities | 5 / 5 | ✅ Complete |
| Server-side request forgery (SSRF) | 3 / 5 | 🟡 In progress |
| XML external entity (XXE) injection | 0 / 9 | 🟡 In progress |
| HTTP request smuggling | 0 / 22 | 🟡 In progress |
| Server-side template injection | 0 / 6 | 🟡 In progress |
| Web cache poisoning | 0 / 13 | 🟡 In progress |
| Insecure deserialization | 0 / 10 | 🟡 In progress |
| Business logic vulnerabilities | 0 / 10 | 🟡 In progress |
| HTTP Host header attacks | 0 / 6 | 🟡 In progress |
| OAuth authentication | 0 / 6 | 🟡 In progress |
| File upload vulnerabilities | 0 / 1 | 🟡 In progress |
| JWT | 0 / 6 | 🟡 In progress |
| Prototype pollution | 0 / 10 | 🟡 In progress |
| NoSQL injection | 0 / 4 | 🟡 In progress |
| API testing | 0 / 1 | 🟡 In progress |
| Web LLM attacks | 0 / 8 | 🟡 In progress |
| Web cache deception | 0 / 1 | 🟡 In progress |
| Web cache poisoning | 0 / 13 | 🟡 In progress |

> Status legend: ✅ Complete = all labs for that category are solved. 🟡 In progress = some labs are solved or remaining. ⬜ Not started = no labs started yet.

---

## `//` tools of the trade

<div align="left">

![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white)
![DevTools](https://img.shields.io/badge/Browser%20DevTools-4285F4?style=flat-square&logo=googlechrome&logoColor=white)
![HTTP Proxy](https://img.shields.io/badge/HTTP%20Proxy-22d3ee?style=flat-square)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</div>

---

## `//` how to read this table

| Field | Meaning |
|---|---|
| `Solved / Total` | Number of labs solved out of the category total |
| `Status` | `✅ Complete`, `🟡 In progress`, or `⬜ Not started` |

> This table reflects the latest status based on the current lab tracker, and keeps the category-level progress synced with the latest solved labs.

---

## see table below

| No | Date | Topic | Lab Title | Difficulty | Writeup |
|---|---|---|---|---|---|
| 100 | 2026-10-28 | Access control | User role can be modified in user profile | Apprentice | N/A |
| 101 | 2026-10-28 | Access control | User ID controlled by request parameter with data leakage in redirect | Apprentice | N/A |
| 102 | 2026-10-28 | Access control | Insecure direct object references | Apprentice | N/A |
| 103 | 2026-10-28 | Access control | URL-based access control can be circumvented | Practitioner | N/A |
| 104 | 2026-10-28 | Access control | Method-based access control can be circumvented | Practitioner | N/A |
| 105 | 2026-10-28 | Authentication | Username enumeration via account lock | Practitioner | N/A |
| 106 | 2026-10-28 | Authentication | Broken brute-force protection, multiple credentials per request | Expert | N/A |
| 107 | 2026-10-28 | HTTP Host header attacks | Basic password reset poisoning | Apprentice | N/A |
| 108 | 2026-10-28 | Business logic vulnerabilities | Excessive trust in client-side controls | Apprentice | N/A |
| 109 | 2026-10-28 | Business logic vulnerabilities | High-level logic vulnerability | Apprentice | N/A |
| 110 | 2026-10-28 | Server-side template injection | Basic server-side template injection | Practitioner | N/A |
| 111 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages | Practitioner | N/A |
| 112 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages and a JavaScript URL | Practitioner | N/A |
| 113 | 2026-10-28 | DOM-based vulnerabilities | DOM XSS using web messages and JSON.parse | Practitioner | N/A |
| 114 | 2026-10-28 | DOM-based vulnerabilities | DOM-based open redirection | Practitioner | N/A |
| 115 | 2026-10-28 | DOM-based vulnerabilities | DOM-based cookie manipulation | Practitioner | N/A |
| 116 | 2026-10-28 | DOM-based vulnerabilities | Exploiting DOM clobbering to enable XSS | Expert | N/A |
| 117 | 2026-10-28 | DOM-based vulnerabilities | Clobbering DOM attributes to bypass HTML filters | Expert | N/A |
| 118 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with nothing encoded | Apprentice | N/A |
| 119 | 2026-10-28 | Cross-site scripting | Stored XSS into HTML context with nothing encoded | Apprentice | N/A |
| 120 | 2026-10-28 | Cross-site scripting | DOM XSS in document.write sink using source location.search | Apprentice | N/A |
| 121 | 2026-10-28 | Cross-site scripting | DOM XSS in innerHTML sink using source location.search | Apprentice | N/A |
| 122 | 2026-10-28 | Cross-site scripting | DOM XSS in jQuery anchor href attribute sink using location.search source | Apprentice | N/A |
| 123 | 2026-10-28 | Cross-site scripting | DOM XSS in jQuery selector sink using a hashchange event | Apprentice | N/A |
| 124 | 2026-10-28 | Cross-site scripting | Reflected XSS into attribute with angle brackets HTML-encoded | Apprentice | N/A |
| 125 | 2026-10-28 | Cross-site scripting | Stored XSS into anchor href attribute with double quotes HTML-encoded | Apprentice | N/A |
| 126 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with angle brackets HTML encoded | Apprentice | N/A |
| 127 | 2026-10-28 | Cross-site scripting | DOM XSS in document.write sink using source location.search inside a select element | Practitioner | N/A |
| 128 | 2026-10-28 | Cross-site scripting | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | Practitioner | N/A |
| 129 | 2026-10-28 | Cross-site scripting | Reflected DOM XSS | Practitioner | N/A |
| 130 | 2026-10-28 | Cross-site scripting | Stored DOM XSS | Practitioner | N/A |
| 131 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with most tags and attributes blocked | Practitioner | N/A |
| 132 | 2026-10-28 | Cross-site scripting | Reflected XSS into HTML context with all tags blocked except custom ones | Practitioner | N/A |
| 133 | 2026-10-28 | Cross-site scripting | Reflected XSS with some SVG markup allowed | Practitioner | N/A |
| 134 | 2026-10-28 | Cross-site scripting | Reflected XSS in canonical link tag | Practitioner | N/A |
| 135 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with single quote and backslash escaped | Practitioner | N/A |
| 136 | 2026-10-28 | Cross-site scripting | Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped | Practitioner | N/A |
| 137 | 2026-10-28 | Cross-site scripting | Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped | Practitioner | N/A |
| 138 | 2026-10-28 | Cross-site scripting | Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped | Practitioner | N/A |
| 139 | 2026-10-28 | Cross-site scripting | Exploiting cross-site scripting to steal cookies | Practitioner | N/A |
| 140 | 2026-10-28 | Cross-site scripting | Exploiting cross-site scripting to capture passwords | Practitioner | N/A |
| 141 | 2026-10-28 | Cross-site scripting | Exploiting XSS to bypass CSRF defenses | Practitioner | N/A |
| 142 | 2026-10-28 | Cross-site scripting | Reflected XSS with AngularJS sandbox escape without strings | Expert | N/A |
| 143 | 2026-10-28 | Cross-site scripting | Reflected XSS with AngularJS sandbox escape and CSP | Expert | N/A |
| 144 | 2026-10-28 | Cross-site scripting | Reflected XSS with event handlers and href attributes blocked | Expert | N/A |
| 145 | 2026-10-28 | Cross-site scripting | Reflected XSS in a JavaScript URL with some characters blocked | Expert | N/A |
| 146 | 2026-10-28 | Cross-site scripting | Reflected XSS protected by very strict CSP, with dangling markup attack | Practitioner | N/A |
| 147 | 2026-10-28 | Cross-site scripting | Reflected XSS protected by CSP, with CSP bypass | Expert | N/A |
| 150 | 2026-10-28 | JWT | JWT authentication bypass via unverified signature | Apprentice | N/A |
| 151 | 2026-10-28 | JWT | JWT authentication bypass via flawed signature verification | Apprentice | N/A |
| 152 | 2026-10-28 | GraphQL API vulnerabilities | Performing CSRF exploits over GraphQL | Practitioner | N/A |

---

## `//` what's next

- [ ] Finish remaining **SSRF** labs (2 left)
- [ ] Finish remaining **XXE** labs (9 left)
- [ ] Finish remaining **HTTP request smuggling** labs (22 left)
- [ ] Finish remaining **SSTI** labs (6 left)
- [ ] Finish remaining **Authentication** labs (1 left)
- [ ] Finish remaining **Web cache poisoning** labs (13 left)
- [ ] Finish remaining **Business logic** labs (10 left)
- [ ] Finish remaining **JWT** labs (6 left)
- [ ] Finish the **Prototype pollution** track (10 left)
- [ ] Finish **NoSQL injection** labs (4 left)
- [ ] Finish **API testing** labs (1 left)
- [ ] Finish **Web LLM** labs (8 left)
- [ ] Finish **Web cache deception** labs (1 left)

---

## `//` connect

<div align="left">

[![Portfolio](https://img.shields.io/badge/Portfolio-0891b2?style=for-the-badge&logo=firefox&logoColor=white)](https://awel-abduljelil.netlify.app/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Awel-Abduljelil)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Awexaa)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://www.x.com/Aweljelil49555)

</div>

<div align="center">
<sub>Built lab by lab. No shortcuts, no copy-paste writeups — just hands-on practice.</sub>
</div>
