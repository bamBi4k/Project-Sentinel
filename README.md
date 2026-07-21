# Project Sentinel

**Prove who you are, without revealing who you are.**

Project Sentinel is a privacy-first identity system that lets you prove simple facts about yourself, like **“I am over 18”**, without sharing sensitive details such as your name, birth date, or ID number.

---

## What is Project Sentinel?

Project Sentinel is a digital identity prototype built around privacy.

Instead of showing everything about you, it only shares the minimum information needed for access.  
Think of it like a digital ID card that hides everything except the one fact a website actually needs.

---

## Why it matters

Today, many websites ask for more personal data than they really need.

Project Sentinel is designed to change that by helping people:

- Keep personal details private.
- Control their own identity data.
- Verify information without exposing the underlying data.
- Avoid accounts, passwords, and unnecessary tracking.

---

## How it works

![System Architecture](https://github.com/bamBi4k/Project-Sentinel/blob/ed7d9a86ced18bfbc2c07a605a908ed51555154b/Data%20Flow%20Diagram.png)

**Figure 1:** Complete identity verification flow from issuance to access.

### Simple flow

1. **Sentinel Authority** creates cryptographic keys and issues a signed credential.
2. **Your wallet** stores the credential securely on your device.
3. **A website** asks you to verify something.
4. **Your wallet** signs a challenge without revealing personal data.
5. **The website** checks the proof and grants access.

---

## Key features

| Feature | What it means |
|---|---|
| Trusted issuer | An authority signs and issues verifiable credentials. |
| User-controlled wallet | Credentials stay on your device, not on a company server. |
| Cryptographic signatures | Helps protect credentials from tampering. |
| Credential verification | Confirms facts without exposing private details. |
| Challenge-response login | Uses a fresh challenge each time to prevent replay attacks. |
| Replay protection | Each verification is unique and cannot be reused. |
| No database | No central storage of user profiles or personal records. |
| No user accounts | No sign-up forms, passwords, or traditional login system. |

---

## What it is today

This is a working prototype that demonstrates:

- A complete identity handshake from issuer to website.
- Privacy-preserving verification.
- A foundation for decentralized identity systems.

It is inspired by the same general ideas behind:

- Verifiable Credentials.
- OpenID4VC.
- eIDAS 2.0 digital wallet concepts.

---

## What comes next

### Phase 4.5: Privacy hardening
- Reduce leakage of birth year and user identifiers.
- Make the website receive only the exact proof it needs.

### Phase 5: Selective disclosure
- Choose exactly what to reveal.
- Example: prove “I am over 18” without showing your birth year.
- Example: prove “I am a citizen” without revealing your passport number.

### Phase 6: Zero-knowledge proofs
- Replace signature checks with zero-knowledge proofs.
- Prove facts mathematically without revealing the underlying data.
- Possible technologies: Groth16, PLONK, or Bulletproofs.

---

## Current status

| Phase | Status |
|---|---|
| Phase 1: Basic structure | Complete |
| Phase 2: Identity issuance | Complete |
| Phase 3: Wallet implementation | Complete |
| Phase 4: Verification flow | Complete |
| Phase 4.5: Privacy hardening | In progress |
| Phase 5: Selective disclosure | Planned |
| Phase 6: Zero-knowledge proofs | Planned |

---

## How to try it

### Requirements
- Python 3.8 or higher
- Git

### Setup

```bash
git clone https://github.com/bamBi4k/Project-Sentinel.git
cd Project-Sentinel
pip install -r requirements.txt
```

### Run the prototype

Open **3 terminals** and run:

```bash
# Terminal 1
python issuer.py
```

```bash
# Terminal 2
python website.py
```

```bash
# Terminal 3
python wallet.py
```

### Test the flow

1. Open your browser to http://127.0.0.1:5000
2. Click **Verify Identity**
3. Let the wallet generate a proof
4. The website verifies it
5. Access is granted

---

## Project structure

```text
Project-Sentinel/
├── issuer.py          # Issues signed credentials
├── wallet.py          # Stores credentials locally
├── website.py         # Demo website asking for verification
├── verifier.py        # Verification logic
├── crypto_utils.py    # Key generation and crypto helpers
├── main.py            # Combined demo script
├── requirements.txt   # Python dependencies
└── templates/
    ├── index.html     # Main verification page
    └── success.html   # Access granted page
```

---

## Privacy promises

Your data stays on your device:

- Private keys are never sent anywhere.
- Credentials are stored locally.
- Proofs are generated on-device.
- Websites receive only the information they need.
- There is no central database to breach.

---

## Contributing

This is an open-source project focused on privacy-preserving digital identity.

Help is especially welcome in these areas:

- Mobile wallet development.
- QR code and NFC integration.
- Zero-knowledge proof implementation.
- UI/UX improvements.
- Browser extension development.

---

## License

MIT License — free to use, modify, and distribute.

---

## Questions?

- Open an issue on GitHub.
- Star the repository to follow progress.
- Watch for new releases and features.

**Project Sentinel — because your identity should belong to you.**
