<div align="center">

# 🛡️ PortSwigger Web Security Academy — Lab Journey

### `awel@astu:~$` tracking every vulnerability, one lab at a time 

[![Total Labs](https://img.shields.io/badge/Total%20Labs-79%20solved-22d3ee?style=for-the-badge&logo=hackthebox&logoColor=white)](#-solved-labs)
[![Apprentice](https://img.shields.io/badge/Apprentice-34%2F61-3fb950?style=for-the-badge)](#-level-progress)
[![Practitioner](https://img.shields.io/badge/Practitioner-51%2F174-f5a524?style=for-the-badge)](#-level-progress)
[![Expert](https://img.shields.io/badge/Expert-0%2F39-f85149?style=for-the-badge)](#-level-progress)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Aug%208%202026-0891b2?style=for-the-badge)](#-solved-labs)

**[🌐 Portfolio](https://awel-abduljelil.github.io/My-Portfolio/) · [💻 GitHub](https://github.com/Awel-Abduljelil) · [✍️ Writeups on Medium](https://medium.com/@awela1499) · [📡 Telegram](https://t.me/Awexaa)**

</div>

---

## `//` about

This repo documents my hands-on progress through **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — the same curriculum used by working AppSec engineers and pentesters to learn real exploitation techniques, not just theory.

Every lab here was solved manually using **Burp Suite**, browser dev tools, and an HTTP proxy — no walkthroughs copy-pasted, no shortcuts. The goal is to build the same instincts a professional penetration tester relies on: read the app, form a hypothesis, test it, break it.

This journey feeds directly into my [portfolio](https://awel-abduljelil.github.io/My-Portfolio/) and CTF work — think of this repo as the lab notebook behind the "Penetration Tester" title on that site.

---

## `//` level progress

| Rank | Progress | Completion |
|---|---|---|
| 🟢 **Apprentice** | `███████████████░░░░░░░░░░░` | **36 / 61** |
| 🟡 **Practitioner** | `████████░░░░░░░░░░░░░░░░░░░░` | **52 / 174** |
| 🔴 **Expert** | `░░░░░░░░░░░░░░░░░░░░░░░░` | **0 / 39** |

---

## `//` categories covered

| Category | Progress | Status |
|---|---|---|
| Web cache deception | 4 / 4 | ✅ Complete |
| Server-side request forgery (SSRF) | 5 / 5 | ✅ Complete |
| Authentication vulnerabilities | 11 / 11 | ✅ Complete |
| Clickjacking (UI redressing) | 5 / 5 | ✅ Complete |
| File upload vulnerabilities | 6 / 6 | ✅ Complete |
| Path traversal | 6 / 6 | ✅ Complete |
| Information disclosure| 5 / 5 | ✅ Complete |
| SQL injection | 14 / 15 | 🟡 In progress |
| API testing | 4 / 5 | 🟡 In progress |
| Command injection | 3 / 5 | 🟡 In progress |
| Access control | 5 / 13 | 🟡 In progress |
| WebSockets vulnerabilities | 1 / 13 | 🟡 In progress |
| GraphQL API vulnerabilities | 4 / 9 | 🟡 In progress  |
| Cross-site scripting (XSS) | 0 / 0 | ⬜ Not started |
| Server-side template injection (SSTI) | 2 / 15 | ⬜ Not started |
| JWT attacks | 0 / 0 | ⬜ Not started |
| OAuth authentication | 0 / 0 | ⬜ Not started |
| Insecure deserialization | 0 / 0 | ⬜ Not started |
| XXE injection | 0 / 0 | ⬜ Not started |
| NoSQL injection | 0 / 0 | ⬜ Not started |
| Request smuggling | 0 / 0 | ⬜ Not started |

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
| `No` | Sequential lab number |
| `Date` | When the lab was solved |
| `Topic` | Vulnerability category |
| `Lab Title` | Exact PortSwigger lab name |
| `Difficulty` | Apprentice / Practitioner / Expert |
| `Writeup` | Link to a full breakdown, or `N/A` if notes weren't published |

> Full writeups are reserved for labs with a technique or trick worth documenting in depth — the rest are solved and logged, but not all get a dedicated article.


## see tablee bellow
---


| No | Date | Topic | Lab Title | Difficulty | Writeup |
|---|---|---|---|---|---|
| 1 | 2026-06-10 | Web cache deception | Exploiting path mapping for web cache deception | Apprentice | N/A |
| 2 | 2026-06-10 | Web cache deception | Exploiting path delimiters for web cache deception | Practitioner | N/A |
| 3 | 2026-06-10 | Web cache deception | Exploiting origin server normalization for web cache deception | Practitioner | N/A |
| 4 | 2026-06-10 | Web cache deception | Exploiting cache server normalization for web cache deception | Practitioner | N/A |
| 5 | 2026-06-11 |   SSRF | Basic SSRF against the local server | Apprentice | N/A |
| 6 | 2026-06-11 |   SSRF | Basic SSRF against another back-end system | Apprentice | N/A |
| 7 | 2026-06-11 |   SSRF | SSRF with blacklist-based input filter | Practitioner | N/A |
| 8 | 2026-06-11 |   SSRF | SSRF with filter bypass via open redirection vulnerability | Practitioner | N/A |
| 9 | 2026-06-11 |   SSRF | Blind SSRF with out-of-band detection | Practitioner | N/A |
| 10 | 2026-06-12 | Authentication | Username enumeration via different responses | Apprentice | [writeup](https://medium.com/@awela1499/username-enumeration-via-different-responses-portswigger-lab-17dd6255e1bb) |
| 11 | 2026-06-12 | Authentication | Username enumeration via subtly different responses | Practitioner | N/A |
| 12 | 2026-06-12 | Authentication | Username enumeration via response timing | Practitioner | N/A |
| 13 | 2026-06-12 | Authentication | Broken brute-force protection, IP block | Practitioner | N/A |
| 14 | 2026-06-13 | Authentication | 2FA simple bypass | Apprentice | N/A |
| 15 | 2026-06-13 | Authentication | 2FA broken logic | Practitioner | N/A |
| 16 | 2026-06-13 | Authentication | Brute-forcing a stay-logged-in cookie | Practitioner | N/A |
| 17 | 2026-06-13 | Authentication | Offline password cracking | Practitioner | N/A |
| 18 | 2026-06-13 | Authentication | Password reset broken logic | Apprentice | N/A |
| 19 | 2026-06-13 | Authentication | Password reset poisoning via middleware | Practitioner | N/A |
| 20 | 2026-06-13 | Authentication | Password brute-force via password change | Practitioner | N/A |
| 21 | 2026-06-14 |   Clickjacking | Basic clickjacking with CSRF token protection | Apprentice | N/A |
| 22 | 2026-06-14 |   Clickjacking | Clickjacking with form input data prefilled from a URL parameter | Apprentice | N/A |
| 23 | 2026-06-14 |   Clickjacking | Clickjacking with a frame buster script | Apprentice | N/A |
| 24 | 2026-06-14 |   Clickjacking | Exploiting clickjacking to trigger DOM-based XSS | Practitioner | N/A |
| 25 | 2026-06-14 |   Clickjacking | Multistep clickjacking | Practitioner | N/A |
| 26 | 2026-06-16 | SQL injection | SQLi in WHERE clause allowing retrieval of hidden data | Apprentice | N/A |
| 27 | 2026-06-16 | SQL injection | SQLi vulnerability allowing login bypass | Apprentice | N/A |
| 28 | 2026-06-16 | SQL injection | UNION attack — determining the number of columns | Practitioner | N/A |
| 29 | 2026-06-16 | SQL injection | UNION attack — finding a column containing text | Practitioner | N/A |
| 30 | 2026-06-16 | SQL injection | UNION attack — retrieving data from other tables | Practitioner | N/A |
| 31 | 2026-06-16 | SQL injection | UNION attack — retrieving multiple values in a single column | Practitioner | N/A |
| 32 | 2026-06-17 | SQL injection | Querying the database type and version (MySQL/MS-SQL) | Practitioner | N/A |
| 33 | 2026-06-17 | SQL injection | Listing the database contents on non-Oracle databases | Practitioner | N/A |
| 34 | 2026-06-19 | Path traversal | File path traversal, simple case | Apprentice | N/A |
| 35 | 2026-06-19 |   Access control | Unprotected admin functionality | Apprentice | N/A |
| 36 | 2026-06-19 |   Access control | Unprotected admin functionality with unpredictable URL | Apprentice | N/A |
| 37 | 2026-06-19 |   Access control | User role controlled by request parameter | Apprentice | N/A |
| 38 | 2026-06-19 |   Access control | User ID controlled by request parameter, unpredictable IDs | Apprentice | N/A |
| 39 | 2026-06-19 |   Access control | User ID controlled by request parameter with password disclosure | Apprentice | N/A |
| 40 | 2026-06-20 | SQL injection | Blind SQLi with conditional responses | Practitioner | N/A |
| 41 | 2026-06-20 | SQL injection | Blind SQLi with conditional errors | Practitioner | N/A |
| 42 | 2026-06-20 | SQL injection | Visible error-based SQL injection | Practitioner | N/A |
| 43 | 2026-06-21 | SQL injection | Blind SQLi with time delays and information retrieval | Practitioner | N/A |
| 44 | 2026-06-22 | SQL injection | SQLi with filter bypass via XML encoding | Practitioner | N/A |
| 45 | 2026-06-23 |   File upload | Remote code execution via web shell upload | Apprentice | N/A |
| 46 | 2026-06-23 |   File upload | Web shell upload via Content-Type restriction bypass | Apprentice | N/A |
| 47 | 2026-06-23 |   File upload | Web shell upload via path traversal | Practitioner | N/A |
| 48 | 2026-06-23 |   File upload | Web shell upload via extension blacklist bypass | Practitioner | N/A |
| 49 | 2026-06-24 |   File upload | Web shell upload via obfuscated file extension | Practitioner | N/A |
| 50 | 2026-06-24 |   File upload | Remote code execution via polyglot web shell upload | Practitioner | N/A |
| 51 | 2026-06-24 | Path traversal | Traversal sequences blocked with absolute path bypass | Practitioner | N/A |
| 52 | 2026-06-24 | Path traversal | Traversal sequences stripped non-recursively | Practitioner | N/A |
| 53 | 2026-06-24 | Path traversal | Traversal sequences stripped with superfluous URL-decode | Practitioner | N/A |
| 54 | 2026-06-24 | Path traversal | Validation of start of path | Practitioner | N/A |
| 55 | 2026-06-24 | Path traversal | Validation of file extension with null byte bypass | Practitioner | N/A |
| 56 | 2026-06-25 |   API testing | Exploiting an API endpoint using documentation | Apprentice | N/A |
| 57 | 2026-06-25 |   API testing | Finding and exploiting an unused API endpoint | Practitioner | N/A |
| 58 | 2026-06-26 |   API testing | Exploiting a mass assignment vulnerability | Practitioner | N/A |
| 59 | 2026-06-26 |   API testing | Exploiting server-side parameter pollution in a query string | Practitioner | N/A |
| 60 | 2026-06-27 | Command injection | OS command injection, simple case | Apprentice | N/A |
| 61 | 2026-06-27 | Command injection | Blind OS command injection with time delays | Practitioner | N/A |
| 62 | 2026-06-27 | Command injection | Blind OS command injection with output redirection | Practitioner | N/A |
| 63 | 2026-07-01 |   GraphQL API vulnerabilities| Accessing private GraphQL posts | Apprentice | N/A |
| 64 | 2026-07-06 |   GraphQL API vulnerabilities| Accidental exposure of private GraphQL fields | Practitioner | N/A |
| 65 | 2026-08-03 |SQL injection | SQL injection attack, querying the database type and version on Oracle| Practitioner | N/A |
| 66 | 2026-08-03 |  Information disclosure | Information disclosure vulnerabilities| Apprentice | N/A |
| 67 | 2026-08-03 |  Information disclosure | Source code disclosure via backup files| Apprentice | N/A |
| 68 | 2026-08-03 |  Information disclosure | Information disclosure on debug page| Apprentice | N/A |
| 69 | 2026-08-03 |  Information disclosure | Authentication bypass via information disclosure| Apprentice | N/A |
| 70 | 2026-08-03 |  Information disclosure | information disclosure in version control history | Practitioner | N/A |
| 71 | 2026-08-04 | CSRF |  CSRF vulnerability with no defenses | Practitioner | N/A |
| 72 | 2026-08-04 | CSRF |  CSRF where token validation depends on request method | Practitioner | N/A |
| 73 | 2026-08-04 | CSRF | CSRF where token validation depends on token being present  | Practitioner | N/A |
| 74 | 2026-08-05 | CSRF | CSRF where token is not tied to user session PRACTITIONER | Practitioner | N/A |
| 75 | 2026-08-06 |   WebSockets vulnerabilities |Manipulating WebSocket messages to exploit vulnerabilities| APPRENTICE  | N/A |
| 76 | 2026-08-07 |   GraphQL API vulnerabilities |Accessing private GraphQL posts | APPRENTICE  | N/A |
| 77 | 2026-08-07 |   GraphQL API vulnerabilities |Accidental exposure of private GraphQL fields | PRACTITIONER  | N/A |
| 78 | 2026-08-08 |   GraphQL API vulnerabilities |Finding a hidden GraphQL endpoint| PRACTITIONER  | N/A |
| 79 | 2026-08-08 |   GraphQL API vulnerabilities |Bypassing GraphQL brute force protections  | PRACTITIONER  | N/A |




## `//` what's next

- [ ] Finish remaining **Access control** labs (8 left)
- [ ] Start **Cross-site scripting (XSS)** track
- [ ] Start **JWT attacks** track
- [ ] Push toward first **Expert**-level lab

---

## `//` connect

<div align="left">

[![Portfolio](https://img.shields.io/badge/Portfolio-0891b2?style=for-the-badge&logo=firefox&logoColor=white)](https://awel-abduljelil.github.io/My-Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Awel-Abduljelil)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Awexaa)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://www.x.com/Aweljelil49555)

</div>

<div align="center">
<sub>Built lab by lab. No shortcuts, no copy-paste writeups — just hands-on practice.</sub>
</div>
