"""
Project Sentinel

Credential Issuer

Responsible for:

- Creating credentials
- Signing credentials
- Saving credentials

The issuer represents a trusted authority.
"""


import json
import os
import hashlib

from crypto_utils import sign_message


ISSUER_NAME = "SentinelAuthority"

CREDENTIAL_FOLDER = "credentials"



def create_credential_folder():

    if not os.path.exists(
        CREDENTIAL_FOLDER
    ):

        os.makedirs(
            CREDENTIAL_FOLDER
        )



def generate_user_identifier():

    """
    Creates anonymous credential ID.

    This is NOT a person's identity.

    It is only a reference
    inside the credential system.
    """


    random_bytes = os.urandom(32)


    return hashlib.sha256(
        random_bytes
    ).hexdigest()



def create_credential(
        age_over_18,
        birth_year
):

    create_credential_folder()


    user_identifier = (
        generate_user_identifier()
    )


    credential = {

        "user_identifier":
            user_identifier,


        "age_over_18":
            age_over_18,


        "birth_year":
            birth_year,


        "issuer":
            ISSUER_NAME

    }


    credential_data = json.dumps(
        credential,
        sort_keys=True
    )


    signature = sign_message(
        ISSUER_NAME,
        credential_data
    )


    credential["signature"] = signature



    filename = (
        f"{CREDENTIAL_FOLDER}/"
        f"{user_identifier}.json"
    )


    with open(
        filename,
        "w"
    ) as file:


        json.dump(
            credential,
            file,
            indent=4
        )


    return credential