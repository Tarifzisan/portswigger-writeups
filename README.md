# 📌 Authentication Basics

Authentication is something we use every single day, often without even thinking about it. Every time you log into your email, unlock your smartphone, access your university portal, or sign in to GitHub, an authentication process is working behind the scenes to verify your identity.

This repository is a beginner-friendly introduction to authentication. It explains the core concepts, common authentication methods, popular attacks, and best security practices in a simple and easy-to-understand way.

---

## 📖 What is Authentication?

Authentication is the process of verifying that a user is who they claim to be before allowing access to a system or application.

For example, when you enter your username and password on a website, the server checks whether those credentials match the stored records. If they do, you're granted access. Otherwise, access is denied.

Think of authentication as showing your student ID before entering an examination hall. The ID confirms your identity, allowing you to enter.

---

## 🤔 Authentication vs Authorization

These two terms are often confused, but they have different purposes.

| Authentication             | Authorization                             |
| -------------------------- | ----------------------------------------- |
| Confirms your identity     | Determines what you are allowed to access |
| Happens first              | Happens after authentication              |
| Answers **"Who are you?"** | Answers **"What can you do?"**            |

For instance, logging into your university portal is authentication. Viewing only your own grades after logging in is authorization.

---

## 🔑 Authentication Factors

Authentication methods are generally based on one or more of these factors.

### Something You Know

This includes information that only you should know.

Examples:

* Password
* PIN
* Security questions

---

### Something You Have

This refers to something you physically possess.

Examples:

* Mobile phone
* Hardware security key
* Smart card
* One-Time Password (OTP) device

---

### Something You Are

These methods use your unique biological characteristics.

Examples:

* Fingerprint
* Face recognition
* Iris scan
* Voice recognition

---

## 🔐 Common Authentication Methods

### Password-Based Authentication

This is the most common authentication method. Users provide a username and password to access a system.

Although simple and widely used, passwords can be weak, reused across multiple websites, or stolen through phishing attacks.

---

### Multi-Factor Authentication (MFA)

Multi-Factor Authentication adds an extra layer of security by requiring two or more verification methods.

For example:

* Password
* OTP sent to your mobile phone

Even if someone discovers your password, they still cannot log in without the second verification step.

---

### Biometric Authentication

Biometric authentication verifies identity using physical characteristics such as fingerprints or facial recognition.

Many smartphones and modern laptops use this method because it is both convenient and secure.

---

### Passwordless Authentication

Instead of relying on passwords, users can authenticate using technologies such as:

* Passkeys
* Hardware security keys
* Biometrics
* Magic login links

Passwordless authentication is becoming increasingly popular because it helps reduce password-related attacks.

---

## ⚠️ Common Authentication Attacks

Attackers often try to exploit weak authentication systems. Some common attacks include:

### Brute Force Attack

Trying many password combinations until the correct one is found.

### Credential Stuffing

Using usernames and passwords leaked from previous data breaches to access other accounts.

### Password Spraying

Trying a few common passwords against many different user accounts.

### Phishing

Creating fake websites or emails that trick users into revealing their login credentials.

### Username Enumeration

Identifying valid usernames by analysing differences in login responses, error messages, or account lock behaviour.

---

## 🔄 Basic Authentication Flow

```text
User
   │
   │  Username & Password
   ▼
Authentication Server
   │
   │  Verify Credentials
   ▼
Is the information correct?
   │
 ┌─┴──────────┐
 │            │
Yes          No
 │            │
 ▼            ▼
Access      Access
Granted     Denied
```

---

## ✅ Best Practices

A secure authentication system should follow these practices:

* Use strong and unique passwords.
* Enable Multi-Factor Authentication (MFA) whenever possible.
* Never reuse passwords across multiple websites.
* Use a trusted password manager.
* Protect login pages with HTTPS.
* Monitor suspicious login attempts.
* Apply account lockout carefully to avoid information leakage.
* Keep authentication mechanisms updated.

---

## 🌍 Where Do We Use Authentication?

Authentication is used almost everywhere online, including:

* Email services
* Social media platforms
* GitHub
* Online banking
* E-commerce websites
* University portals
* Cloud services

If you've ever logged into a website or unlocked your phone, you've already used authentication.

---

## 📌 Conclusion

Authentication is one of the most important building blocks of cybersecurity. It helps ensure that only legitimate users can access protected systems and data.

As technology evolves, authentication methods are also improving. While passwords are still widely used, modern approaches like Multi-Factor Authentication, biometrics, and passkeys provide stronger security and a better user experience.

Whether you're just starting your cybersecurity journey or simply curious about how login systems work, understanding authentication is a valuable first step.

---

## 📚 References

* OWASP Authentication Cheat Sheet
* NIST Digital Identity Guidelines
* PortSwigger Web Security Academy
* Microsoft Security Documentation

---

## 📄 Disclaimer

This repository is created for educational purposes only. Its goal is to help beginners understand the fundamentals of authentication and encourage secure authentication practices.

