"""
Project Sentinel
Cryptographic Foundation

Phase 1:
- Generate identity key pairs
- Sign messages
- Verify signatures

Uses:
Ed25519 public key cryptography

No identity data is stored here.
No databases.
No networking.
"""


from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder
import os


KEY_FOLDER = "keys"


def create_key_folder():
    """
    Creates the key storage directory.
    """

    if not os.path.exists(KEY_FOLDER):
        os.makedirs(KEY_FOLDER)



def generate_keypair(identity_name):
    """
    Generates a new Ed25519 key pair.

    Private key:
        Used to create signatures.
        MUST remain secret.

    Public key:
        Shared with verifiers.
        Used to verify signatures.
    """

    create_key_folder()

    signing_key = SigningKey.generate()

    verify_key = signing_key.verify_key


    private_key_path = (
        f"{KEY_FOLDER}/{identity_name}_private.key"
    )

    public_key_path = (
        f"{KEY_FOLDER}/{identity_name}_public.key"
    )


    with open(private_key_path, "wb") as file:
        file.write(
            signing_key.encode()
        )


    with open(public_key_path, "wb") as file:
        file.write(
            verify_key.encode()
        )


    print("[+] Keypair generated")
    print(f"Private key: {private_key_path}")
    print(f"Public key : {public_key_path}")



def load_private_key(identity_name):
    """
    Loads a private signing key.
    """

    path = (
        f"{KEY_FOLDER}/{identity_name}_private.key"
    )


    with open(path, "rb") as file:
        key_data = file.read()


    return SigningKey(key_data)



def load_public_key(identity_name):
    """
    Loads a public verification key.
    """

    path = (
        f"{KEY_FOLDER}/{identity_name}_public.key"
    )


    with open(path, "rb") as file:
        key_data = file.read()


    return VerifyKey(key_data)



def sign_message(identity_name, message):
    """
    Creates a cryptographic signature.

    Example:

    message:
        "Age verified"

    output:
        signature
    """

    private_key = load_private_key(identity_name)


    signed = private_key.sign(
        message.encode()
    )


    return signed.signature.hex()



def verify_message(identity_name, message, signature):
    """
    Checks whether:

    1. Message was signed
    2. Signature is valid
    3. Public key matches

    Returns True or False.
    """

    public_key = load_public_key(identity_name)


    try:

        public_key.verify(
            message.encode(),
            bytes.fromhex(signature)
        )


        return True


    except Exception:

        return False