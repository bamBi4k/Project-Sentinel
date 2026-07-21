"""
Project Sentinel

Wallet Module

Responsibilities:

Phase 3:
- Import credentials
- Store credentials
- Verify issuer signature

Phase 4:
- Create verification responses
- Sign website challenges

The wallet represents the user's device.
"""


import json
import os


from crypto_utils import (
    verify_message,
    sign_message,
    generate_keypair
)



ISSUER_NAME = "SentinelAuthority"

WALLET_ID = "UserWallet"


WALLET_FOLDER = "wallet_storage"


WALLET_FILE = (
    "wallet_storage/my_credential.json"
)



def create_wallet_folder():

    if not os.path.exists(
        WALLET_FOLDER
    ):

        os.makedirs(
            WALLET_FOLDER
        )



def setup_wallet():

    """
    Creates user wallet keys.
    """

    create_wallet_folder()


    private_key = (
        f"keys/{WALLET_ID}_private.key"
    )


    if not os.path.exists(
        private_key
    ):

        print(
            "[Wallet] Creating wallet keys"
        )

        generate_keypair(
            WALLET_ID
        )



def load_credential_from_issuer(
        credential_path
):

    with open(
        credential_path,
        "r"
    ) as file:

        return json.load(file)



def verify_credential(
        credential
):

    """
    Checks issuer signature.
    """


    signature = credential["signature"]


    unsigned = credential.copy()


    del unsigned["signature"]



    credential_data = json.dumps(
        unsigned,
        sort_keys=True
    )


    return verify_message(

        ISSUER_NAME,

        credential_data,

        signature

    )



def import_credential(
        credential_path
):

    """
    Phase 3:

    Import credential into wallet.
    """


    create_wallet_folder()


    credential = load_credential_from_issuer(
        credential_path
    )


    print(
        "\n[Wallet]"
    )


    print(
        "Checking credential..."
    )



    if not verify_credential(
        credential
    ):

        print(
            "Credential invalid!"
        )

        return False



    print(
        "Credential valid"
    )



    with open(
        WALLET_FILE,
        "w"
    ) as file:


        json.dump(
            credential,
            file,
            indent=4
        )



    print(
        "Credential imported"
    )


    return True



def show_wallet():

    """
    Displays stored credential.
    """


    if not os.path.exists(
        WALLET_FILE
    ):

        print(
            "Wallet empty"
        )

        return



    with open(
        WALLET_FILE,
        "r"
    ) as file:


        credential = json.load(
            file
        )



    print(
        "\nWallet content:"
    )


    print(
        json.dumps(
            credential,
            indent=4
        )
    )



def create_proof(
        challenge
):

    """
    Phase 4:

    Answer website verification request.
    """


    if not os.path.exists(
        WALLET_FILE
    ):

        raise Exception(
            "No credential in wallet"
        )



    with open(
        WALLET_FILE,
        "r"
    ) as file:


        credential = json.load(
            file
        )



    signature = sign_message(

        WALLET_ID,

        challenge

    )



    return {


        "credential":
            credential,


        "wallet_signature":
            signature

    }