Project Sentinel
A decentralized identity handshake system - proving who you are without revealing yourself

What is Project Sentinel?
Project Sentinel is a privacy-first digital identity prototype that allows users to prove facts about themselves (like "I am over 18") without revealing personal information like their name, birth date, or ID number.

Think of it as a digital ID card that only shows what's absolutely necessary - nothing more.

System Architecture
https://github.com/bamBi4k/Project-Sentinel/blob/main/Data%2520Flow%2520Diagram.png?raw=true

Figure 1: Complete identity verification flow from issuance to access

The Flow Explained:
Sentinel Authority generates cryptographic keys and issues signed credentials

User Wallet stores credentials securely on the user's device

Website requests verification and sends a cryptographic challenge

Wallet signs the challenge using the credential (without revealing the actual data)

Website verifies the signature and grants access

Features
Status	Feature	Description
✅	Trusted Issuer	Authority that signs and issues verifiable credentials
✅	User-Controlled Wallet	Credentials stored locally - user is in full control
✅	Cryptographic Signatures	Ed25519 signing and verification for tamper-proof credentials
✅	Credential Verification	Verify authenticity without exposing underlying data
✅	Challenge-Response Auth	Prevents replay attacks with unique challenges per session
✅	Replay Protection	Each verification uses a unique nonce
✅	No Database	Zero data storage - no user profiles or tracking
✅	No User Accounts	No registration, no passwords, no login system
What It Is Today (Prototype)
This is a functional prototype that demonstrates:

Complete identity handshake flow from issuer to website

Cryptographic verification without sharing personal data

A working foundation for decentralized identity systems

This is the basic skeleton behind industry standards like:

Verifiable Credentials (VC)

OpenID4VC

eIDAS 2.0 Wallets (EU Digital Identity Framework)

Future Vision (What It Will Become)
Phase 4.5: Privacy Hardening (In Progress)
Remove birth year and user identifier leakage

Website receives only "age_over_18": true and cryptographic proof

Phase 5: Selective Disclosure
Users choose exactly what attributes to reveal

Prove "I am over 18" without revealing birth year

Prove "I am a citizen" without revealing name or passport number

Phase 6: Zero-Knowledge Proofs (ZKP)
Replace signature verification with zero-knowledge proofs

Prove facts mathematically without revealing ANY underlying data

Using Groth16, PLONK, or Bulletproofs

Production Vision
Full decentralized identity wallet for mobile and browser

Web3 integration with blockchain-based verification

Enterprise-grade privacy compliant with GDPR and data protection laws

Cross-platform support (mobile, desktop, browser extension)

How to Use (Current Prototype)
Prerequisites
Python 3.8 or higher

Git

Quick Setup
bash
# 1. Clone the repository
git clone https://github.com/bamBi4k/Project-Sentinel.git
cd Project-Sentinel

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the system (3 terminals needed)
# Terminal 1 - Start the issuer
python issuer.py

# Terminal 2 - Start the website
python website.py

# Terminal 3 - Run the wallet
python wallet.py
Testing the Flow
Open your browser to http://127.0.0.1:5000

Click "Verify Identity" on the website

Wallet generates a proof using your credential

Website verifies the proof

Access granted - you're verified!

Project Structure
text
Project-Sentinel/
├── issuer.py          # Authority that signs credentials
├── wallet.py          # User wallet storing credentials
├── website.py         # Demo website requesting verification
├── verifier.py        # Cryptographic verification logic
├── crypto_utils.py    # Key generation and crypto helpers
├── main.py            # Combined demo script
├── requirements.txt   # Python dependencies
└── templates/         # Web interface templates
    ├── index.html     # Main verification page
    └── success.html   # Access granted page
Privacy Guarantees
Your data stays on your device:

✅ Private keys are never transmitted

✅ Credentials are stored locally

✅ Proofs are generated on-device

✅ Websites receive only what's necessary

✅ No central database = no data breaches

Current Status
Phase	Status
Phase 1: Basic Structure	✅ Complete
Phase 2: Identity Issuance	✅ Complete
Phase 3: Wallet Implementation	✅ Complete
Phase 4: Verification Flow	✅ Complete
Phase 4.5: Privacy Hardening	🔄 In Progress
Phase 5: Selective Disclosure	📋 Planned
Phase 6: Zero-Knowledge Proofs	📋 Planned
Contributing
This is an open-source project focused on privacy-preserving digital identity. Contributions welcome!

Areas needing help:

Mobile wallet development

QR code / NFC integration

Zero-knowledge proof implementation

UI/UX improvements

Browser extension development

License
MIT License - Free to use, modify, and distribute.

Questions?
Open an issue on GitHub

Star the repository to follow development

Watch for new releases and features

Project Sentinel - Because your identity should belong to you.

Quick Start Commands
bash
# If you want to try it right now:

# 1. Start the website
python website.py

# 2. In another terminal, run the demo
python main.py

# 3. Open browser to http://127.0.0.1:5000
This response is AI-generated, for reference only.
