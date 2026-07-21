"""
Project Sentinel

Phase 4

Verifier

Represents:

Website
Government service
Third party

Responsibilities:

- Create verification requests
- Validate wallet responses
"""


import json
import time
import secrets


from crypto_utils import verify_message



ISSUER_NAME = "SentinelAuthority"



def create_challenge():

    """
    Creates a random challenge.

    Prevents replay attacks.

    Every verification attempt
    gets a new number.
    """

    challenge = secrets.token_hex(32)


    return {

        "challenge": challenge,

        "timestamp": time.time(),

        "requirement":
            "age_over_18"

    }



def verify_response(
        request,
        response
):

    """
    Checks wallet response.

    """



    credential = (
        response["credential"]
    )


    wallet_signature = (
        response["wallet_signature"]
    )


    challenge = (
        request["challenge"]
    )



    # -------------------------
    # Check credential issuer
    # -------------------------


    credential_copy = (
        credential.copy()
    )


    issuer_signature = (
        credential_copy["signature"]
    )


    del credential_copy["signature"]



    credential_data = json.dumps(
        credential_copy,
        sort_keys=True
    )



    issuer_valid = verify_message(

        ISSUER_NAME,

        credential_data,

        issuer_signature

    )



    if not issuer_valid:

        return False



    # -------------------------
    # Check requirement
    # -------------------------


    if credential["age_over_18"] != True:

        return False



    # -------------------------
    # Verify wallet signed challenge
    # -------------------------


    wallet_valid = verify_message(

        "UserWallet",

        challenge,

        wallet_signature

    )



    return wallet_valid