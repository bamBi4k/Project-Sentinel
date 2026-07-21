"""
Project Sentinel

Main Demo

Phase 1:
Authority

Phase 2:
Credential issuance

Phase 3:
Wallet import

"""


import os
import glob



from crypto_utils import (
    generate_keypair
)


from issuer import (
    create_credential
)


from wallet import (
    import_credential,
    show_wallet
)



ISSUER = "SentinelAuthority"



print(
    "\n=============================="
)

print(
    "       PROJECT SENTINEL"
)

print(
    "=============================="
)



# -------------------------
# Phase 1
# -------------------------


private_key = (
    f"keys/{ISSUER}_private.key"
)



if not os.path.exists(
    private_key
):

    print(
        "\nCreating authority..."
    )

    generate_keypair(
        ISSUER
    )


else:

    print(
        "\nAuthority already exists."
    )



# -------------------------
# Phase 2
# -------------------------


credentials = glob.glob(
    "credentials/*.json"
)



if len(credentials) == 0:


    print(
        "\nCreating credential..."
    )


    create_credential(

        True,

        2000

    )


    credentials = glob.glob(
        "credentials/*.json"
    )


else:


    print(
        "\nExisting credential found."
    )



credential_file = credentials[0]



print(
    "\nCredential:"
)

print(
    credential_file
)



# -------------------------
# Phase 3
# -------------------------


if not os.path.exists(
    "wallet_storage/my_credential.json"
):


    print(
        "\nImporting credential into wallet..."
    )


    import_credential(
        credential_file
    )


else:


    print(
        "\nWallet already contains credential."
    )



show_wallet()



print(
    "\n=============================="
)

print(
    "PHASE 3 COMPLETE"
)

print(
    "=============================="
)