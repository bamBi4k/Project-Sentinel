http://127.0.0.1:5000


 Sentinel Authority

                         |
                         |
                 Ed25519 Signature

                         |
                         v

              Signed User Credential

                         |
                         v

                  Sentinel Wallet

                         |
                         |
              Signs Website Challenge

                         |
                         v

                  Sentinel Website

                         |
                         |
                    Verification

                         |
                         v

                  ACCESS GRANTED


Important: 

This is no longer just "a Python script".

You now have a functional prototype of:

A decentralized identity handshake

with:

✅ Trusted issuer
✅ User-controlled wallet
✅ Cryptographic signatures
✅ Credential verification
✅ Challenge-response authentication
✅ Replay protection foundation
✅ No database
✅ No user accounts

This is the basic skeleton behind systems like:

Verifiable Credentials
OpenID4VC
eIDAS 2.0 wallets




Project Sentinel — Phase 1

Goal:

Create the foundation for:

generating cryptographic identities
signing data
verifying signatures

This is the core of the future handshake.

Project-Sentinel/
│
├── main.py
├── crypto_utils.py
├── issuer.py
├── wallet.py
├── verifier.py
│
├── keys/
│
├── credentials/
│
└── requirements.txt


For now only these matter:

main.py
crypto_utils.py
requirements.txt

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What you have now

You have the first real component of Sentinel:

                 Sentinel Authority

                      |
                      |
              signs credential

                      |
                      v

              Digital Signature

You have proven:

✅ A trusted authority can create a cryptographic identity
✅ A message can be signed
✅ Anyone with the public key can verify authenticity
✅ The private key never leaves the issuer