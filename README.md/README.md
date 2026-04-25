# 🛡️ ShadowVault: Advanced End-to-End Encrypted Password Manager

ShadowVault is a high-security local password management system built using Python and Flask. It focuses on absolute data privacy by ensuring that plain-text passwords never touch the database.

---

## 🎯 Project Objectives (Uddeshya)

Is project ko banane ke peeche main 4 bade objectives hain:

1. **Cryptographic Integrity:** User ke sensitive data (passwords) ko standard AES-256 bit encryption se secure karna taaki data breach ke waqt bhi information unreadable rahe.
2. **Privacy-First Architecture:** Ek aisa system design karna jahan "Server" ya "Admin" ko bhi user ke passwords ka pata na chale (jisey technical term mein End-to-End Encryption kehte hain).
3. **Local Key Sovereignty:** User ki encryption key (`master.key`) uske apne local machine par rahegi. Iska matlab hai ki user ke paas apne data ka 100% control hai.
4. **Interactive Security UX:** Ek aisa modern interface provide karna jo cybersecurity tools ko ek premium aur futuristic look de (Cyber Rain & Neon Aesthetics).

---

## 🛠️ Technical Architecture & Security Flow

Project kaise kaam karta hai:
- **Plaintext Input:** User apna password enter karta hai.
- **Encryption Engine:** Python ki `cryptography` library ka use karke password ko AES-256 algorithm se process kiya jata hai.
- **Master Key Generation:** Ek unique `master.key` file generate hoti hai jo sirf user ke computer par hoti hai.
- **Ciphertext Storage:** Database mein sirf ek lamba "Scrambled Code" (Ciphertext) save hota hai. Bina master key ke ise decrypt karna mathematically impossible hai.

---

## 🚀 Key Features

- **End-to-End Encryption:** Data is encrypted before storage.
- **Multicolour Cyber Rain UI:** Futuristic ambient background for better UX.
- **Glassmorphism Design:** Modern transparent cards with interactive zoom effects.
- **Secure SQLite Backend:** Robust and lightweight local database.

---

## 💻 Tech Stack
- **Backend:** Python, Flask
- **Security:** Fernet (AES-256), Cryptography Library
- **Database:** SQLite, SQLAlchemy
- **Frontend:** HTML5, CSS3 (Neon-Animations), Bootstrap 5

---

## 👨‍💻 Developed By
**Krishna Shivare** *B.Tech Student & Cybersecurity Enthusiast*