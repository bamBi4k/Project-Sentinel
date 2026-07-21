"""
Project Sentinel

Local Verification Website
"""


from flask import Flask, render_template


from verifier import (
    create_challenge,
    verify_response
)


from wallet import (
    setup_wallet,
    create_proof
)



app = Flask(__name__)



@app.route("/")
def index():


    return render_template(
        "index.html"
    )



@app.route("/verify")
def verify():


    request = create_challenge()


    response = create_proof(

        request["challenge"]

    )



    result = verify_response(

        request,

        response

    )



    if result:


        return render_template(
            "success.html"
        )


    else:


        return "Verification failed"



if __name__ == "__main__":


    setup_wallet()


    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )