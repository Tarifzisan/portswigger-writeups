# Username Enumeration via Response Timing

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Category:** Authentication
- **Lab:** Username Enumeration via Response Timing
- **Lab Link:** https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing

---

## Objective

The purpose of this lab is to:

1. Find a valid username by analyzing the response time.
2. Brute-force the password of the valid user.

---

## Solution

### Step 1: Access the Lab

1. Click **Access the Lab**.
2. Open **Burp Suite**.
3. Go to **Proxy** and launch **Burp's Chromium Browser**.
4. Open the lab URL in the browser.

---

### Step 2: Capture the Login Request

1. Click **My Account** to open the login page.
2. Enter any username and password.
3. Turn **Intercept** ON in Burp Suite before logging in.
4. Submit the login request.

**Example Credentials**

```text
Username: test
Password: test
```

---

### Step 3: Send the Request to Repeater

1. Open **HTTP History**.
2. Find the request with:

```text
Method: POST
URL: /login
```

3. Right-click the request and send it to **Repeater**.
4. Add the following header:

```http
X-Forwarded-For: 503
```

5. Set the credentials as:

```text
Username: wiener
Password: peter
```

6. Click **Send**.

The response confirms that these credentials are valid, but they are **not** the target account.

---

### Step 4: Test Response Timing

Replace the password with a very long string (approximately 100 characters).

Example:

```text
peterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeter
```

Click **Send** and observe the response time.

---

### Step 5: Configure Intruder

Send the request to **Intruder**.

#### Payload Position 1

Select the value:

```text
503
```

Configure it as:

- Payload Type: Number
- Number Range:
  - From: 1
  - To: 100
  - Step: 1
- Number Format: Decimal

#### Payload Position 2

Select the username (`wiener`) and configure:

- Payload Type: Simple List
- Paste the provided username list into the payload.

Set the **Attack Type** to **Pitchfork**.

Start the attack.

---

### Step 6: Identify the Valid Username

Compare the following columns:

- Response Received
- Response Complete

The username with the **longest response time** is the valid username.

---

### Step 7: Brute-force the Password

1. Replace the username payload with the valid username.
2. Highlight the password field.
3. Remove the username payload list.
4. Paste the provided password list.
5. Start the attack.

The request that returns **HTTP Status Code 302** indicates the correct password.

---

## Result

- Valid Username: **[Found during enumeration]**
- Correct Password: **[Found during brute force]**

Use the discovered credentials to log in and successfully solve the lab.

---

## Tools Used

- Burp Suite
- Burp Repeater
- Burp Intruder
- Chromium (Burp Browser)

---

## Key Takeaways

- Response timing can reveal valid usernames.
- Burp Intruder's **Pitchfork** attack is useful for username enumeration.
- A **302 Redirect** indicates a successful login in this lab.
