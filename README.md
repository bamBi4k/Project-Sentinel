# Project Sentinel

Project Sentinel is a privacy-focused identity prototype that lets users prove specific facts about themselves without exposing unnecessary personal data.

## Overview

The project demonstrates a minimal identity verification flow built around privacy and user control. A user can prove something like “I am over 18” without sharing their name, ID number, or full date of birth.

## Version 2

Version 2 is the current implementation of Project Sentinel. It uses a modular structure and focuses on privacy hardening, so the website receives only the minimum information needed for verification.

### Version 2 features

- Modular architecture with separated components.
- Privacy hardening with no `user_id` or `birth_year` sent to the website.
- 18+ demo flow with success and access denied pages.
- `.gitignore` configured to protect keys and credentials.
- Storage directories ignored while preserving the project structure.

### Version 2 project structure

```text
Sentinel_v2/
├── app.py                  # Main application
├── authority/              # Issuer and key management
│   ├── issuer.py
│   └── authority_keys.py
├── wallet/                 # Wallet and proof engine
│   ├── wallet.py
│   ├── wallet_keys.py
│   └── proof_engine.py
├── verifier/               # Verification and policy engine
│   ├── verifier.py
│   └── policy_engine.py
├── crypto/                 # Cryptographic functions
│   ├── signatures.py
│   ├── hashing.py
│   └── challenges.py
├── models/                 # Data models
│   ├── credential.py
│   └── proof.py
├── storage/                # Ignored keys and credentials
├── templates/              # HTML templates
│   ├── index.html
│   ├── success.html
│   └── access_denied.html
└── requirements.txt        # Dependencies
```

## Version 1

Version 1 is the original stable prototype. It demonstrates the full issuer-wallet-website handshake and remains a simpler reference implementation.

### Version 1 features

- Trusted issuer with cryptographic signatures.
- User-controlled wallet for credential storage.
- Challenge-response authentication.
- Replay protection.
- No database and no user accounts.

### Version 1 project structure

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

## How it works

![System Architecture](https://github.com/bamBi4k/Project-Sentinel/blob/ed7d9a86ced18bfbc2c07a605a908ed51555154b/Data%20Flow%20Diagram.png)

Figure 1: Complete identity verification flow from issuance to access.

### Simple flow

1. Sentinel Authority creates cryptographic keys and issues a signed credential.
2. Your wallet stores the credential securely on your device.
3. A website asks you to verify something.
4. Your wallet signs a challenge without revealing personal data.
5. The website checks the proof and grants access.

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

## What it is today

This is a working prototype that demonstrates:

- A complete identity handshake from issuer to website.
- Privacy-preserving verification.
- A foundation for decentralized identity systems.

It is inspired by the same general ideas behind:

- Verifiable Credentials.
- OpenID4VC.
- eIDAS 2.0 digital wallet concepts.

## What comes next

### Phase 5: Selective disclosure

- Choose exactly what to reveal.
- Example: prove “I am over 18” without showing your birth year.
- Example: prove “I am a citizen” without revealing your passport number.

### Phase 6: Zero-knowledge proofs

- Replace signature checks with zero-knowledge proofs.
- Prove facts mathematically without revealing the underlying data.
- Possible technologies: Groth16, PLONK, or Bulletproofs.

## Current status

| Phase | Version 2 | Version 1 |
|---|---|---|
| Basic structure | Complete | Complete |
| Identity issuance | Complete | Complete |
| Wallet implementation | Complete | Complete |
| Verification flow | Complete | Complete |
| Privacy hardening | Complete | Not implemented |
| Selective disclosure | Planned | Planned |
| Zero-knowledge proofs | Planned | Planned |

## How to try it

### Requirements

- Python 3.8 or higher.
- Git.

### Setup

```bash
git clone https://github.com/bamBi4k/Project-Sentinel.git
cd Project-Sentinel
pip install -r requirements.txt
```

### Run Version 2

Open a terminal in Sentinel_v2\ and run:

```bash
python app.py
```

### Test the flow

1. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Click **Setup Demo**.
3. Enter your birth year.
4. Click **Verify Identity**.
5. Wait for the redirect if the proof shows you are 18+.

## Privacy promises

Your data stays on your device:

- Private keys are never sent anywhere.
- Credentials are stored locally.
- Proofs are generated on-device.
- Websites receive only the information they need.
- There is no central database to breach.

## Contributing

This is an open-source project focused on privacy-preserving digital identity.

Help is especially welcome in these areas:

- Mobile wallet development.
- QR code and NFC integration.
- Zero-knowledge proof implementation.
- UI/UX improvements.
- Browser extension development.

## License

MIT License — free to use, modify, and distribute.

## Questions?

- Open an issue on GitHub.
- Star the repository to follow progress.
- Watch for new releases and features.

Project Sentinel — because your identity should belong to you.
