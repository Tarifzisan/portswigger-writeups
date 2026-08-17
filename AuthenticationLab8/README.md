# PortSwigger Authentication Lab 8 — 2FA Broken Logic

## Overview

This lab demonstrates a **broken two-factor authentication (2FA) logic** vulnerability. The application trusts a **client-controlled `verify` parameter** instead of validating the second factor against the authenticated server-side session. By abusing this flaw, we can brute-force Carlos's MFA code and access his account.

* **Lab:** Authentication Lab 8
* **Category:** Broken Authentication / 2FA Logic Flaw
* **Difficulty:** Apprentice
* **Platform:** PortSwigger Web Security Academy

---

## Objective

Gain access to **Carlos's account** by exploiting the flawed 2FA verification process.

---

## Lab Credentials

| User     | Password |
| -------- | -------- |
| `wiener` | `peter`  |

**Target User:** `carlos`

---

## Vulnerability

The application sends the following request after a successful login:

```http
GET /login2?verify=wiener
```

Instead of checking the logged-in session, the server relies on the value of the **`verify`** parameter. Since it's user-controlled, we can change it to another username.

**Vulnerable behavior:**

```http
GET /login2?verify=carlos
```

This allows us to generate and verify Carlos's MFA code.

---

## Exploitation Steps

### Step 1 — Login

Log in using the provided credentials.

```text
Username: wiener
Password: peter
```

---

### Step 2 — Intercept the 2FA Request

Capture the request with Burp Suite.

```http
GET /login2?verify=wiener HTTP/1.1
```

Send it to **Repeater**.

---

### Step 3 — Switch to Carlos

Modify the request:

```http
GET /login2?verify=carlos HTTP/1.1
```

Send it to **Intruder**.

---

### Step 4 — Brute Force the MFA Code

Configure Intruder with these payload settings:

| Option        | Value        |
| ------------- | ------------ |
| Attack Type   | Sniper       |
| Payload Type  | Numbers      |
| Character Set | `0123456789` |
| Length        | `4` digits   |

This generates every possible MFA code from **0000 → 9999**.

---

### Step 5 — Identify the Valid Code

Run the attack and monitor the responses.

A successful login returns:

```text
HTTP Status: 302 Found
```

The payload producing **302** is Carlos's valid MFA code.

---

### Step 6 — Access Carlos's Account

Use the discovered code in the browser to complete authentication and gain access to Carlos's account.

---

## Burp Workflow

```text
Login
   │
   ▼
Intercept /login2
   │
   ▼
Change verify=wiener
        │
        ▼
   verify=carlos
        │
        ▼
   Send to Intruder
        │
        ▼
 Brute Force 4-digit MFA
        │
        ▼
 Find HTTP 302
        │
        ▼
 Login as Carlos
```

---

## Root Cause

The application fails to bind the MFA verification to the authenticated user session.

**Insecure design**

```text
Client → verify=carlos → Server accepts
```

**Secure design**

```text
Session User = wiener
Verify Code = wiener only
Ignore client-controlled username
```

---

## Impact

* Account takeover
* Authentication bypass
* Broken access control
* Complete compromise of user accounts

---

## Remediation

* Bind MFA verification to the **server-side session**
* Ignore any client-supplied username during 2FA
* Generate MFA challenges only for the authenticated user
* Rate-limit and lock brute-force attempts
* Log suspicious verification requests

---

## Key Takeaways

* Never trust client-controlled authentication parameters.
* MFA should always be tied to the authenticated session.
* Even strong 2FA becomes ineffective if the verification logic is flawed.

---

## References

* PortSwigger Web Security Academy
* Authentication Vulnerabilities — Broken 2FA Logic
