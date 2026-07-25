# Username Enumeration via Account Lock

A walkthrough of the **PortSwigger Web Security Academy** lab **"Username Enumeration via Account Lock"**.

## 📌 Overview

This lab demonstrates how a flawed account lock mechanism can leak information about valid usernames. By analysing differences in server responses after multiple failed login attempts, an attacker can enumerate existing usernames before attempting a password attack.

## 🎯 Objective

- Enumerate a valid username.
- Brute-force the password for the identified user.
- Log in successfully and solve the lab.

---

# 🛠️ Tools Used

- Burp Suite Professional 
- Burp Intruder
- PortSwigger Web Security Academy
- Candidate username list
- Candidate password list

---

# 🔍 Step 1 – Capture the Login Request

1. Open the lab.
2. Submit any invalid credentials.
3. Intercept the request using Burp Proxy.
4. Send the request to **Intruder**.

Example request:

```http
POST /login HTTP/2

username=test
password=test
```

---

# 🎯 Step 2 – Configure Burp Intruder

Select:

- Attack Type: **Cluster Bomb**

Configure payload positions:

```
username=§invalid-user§
password=test§§
```

The empty payload position at the end generates multiple login attempts for each username.

---

# 📋 Step 3 – Load Payloads

### Payload Set 1

Load the candidate username list.

Example:

```
administrator
carlos
wiener
peter
```

### Payload Set 2

Select:

```
Null Payload
```

Set the number of payloads to **5**.

---

# 🚀 Step 4 – Launch the Attack

Start the Intruder attack.

Most usernames will return:

```
Invalid username or password
```

Most usernames produce the normal authentication error.

However, one username returns a noticeably larger response.

Opening that response reveals a different message:
```
Too many incorrect login attempts
```

This behaviour confirms that the username exists.

---

# ✅ Step 5 – Identify the Valid Username

From the Intruder results, locate the username that triggers the account lock response.

Example:

```
Username: carlos
```

---

# 🔐 Step 6 – Brute Force the Password

Create a new Intruder attack.

Configure:

- Attack Type: **Sniper**

Keep the username fixed.

```
username=carlos
password=§password§
```

Load the candidate password list and start the attack.

---

# 🎉 Step 7 – Find the Correct Password

One response will differ from the others.

Possible indicators include:

- HTTP 302 Redirect
- Different response length
- No warning message
- Account page loads

Example:

```
Username: carlos
Password: mustard
```

---

# 🏁 Step 8 – Login

Use the discovered credentials to log in.

The lab is successfully solved.

---

# 🔒 Security Impact

This vulnerability allows attackers to:

- Enumerate valid usernames
- Perform targeted brute-force attacks
- Increase the success rate of credential stuffing attacks
- Reduce guessing effort significantly

---

# 🛡️ Mitigation

Applications should:

- Return identical error messages
- Keep response timing consistent
- Apply rate limiting
- Implement MFA
- Avoid revealing account lock status
- Monitor authentication logs for abuse

---

# 📚 Skills Learned

- Username Enumeration
- Burp Suite Intruder
- Cluster Bomb Attack
- Sniper Attack
- Authentication Testing
- Account Lock Analysis

---

## Disclaimer

This write-up is intended for educational purposes only. All testing was performed in the PortSwigger Web Security Academy lab environment.
