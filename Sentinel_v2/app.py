# app.py
from flask import Flask, render_template, jsonify, request, session
import json
import secrets
from datetime import datetime
import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from authority.issuer import Issuer
from wallet.wallet import Wallet
from verifier.verifier import Verifier
from verifier.policy_engine import PolicyEngine

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Initialize components
issuer = Issuer()
wallet = Wallet()
verifier = Verifier()

# Set authority public key in verifier
verifier.set_authority_public_key(issuer.get_public_key())

# Initialize policy engine
policy_engine = PolicyEngine()
policy_engine.add_policy("AGE_OVER_18", True)

# Store challenges (in production, use Redis or similar)
stored_challenges = {}

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/success')
def success_page():
    """18+ content page"""
    return render_template('success.html')

@app.route('/access_denied')
def access_denied():
    """Access denied page"""
    return render_template('access_denied.html')

@app.route('/authority/public_key')
def get_authority_public_key():
    """Get authority public key"""
    return jsonify({
        'public_key': issuer.get_public_key()
    })

@app.route('/issuer/issue', methods=['POST'])
def issue_credential():
    """Issue a credential"""
    data = request.json
    user_id = data.get('user_id', 'demo_user')
    birth_year = data.get('birth_year', 2000)
    
    credential = issuer.issue_credential(user_id, birth_year)
    wallet.store_credential(credential)
    
    return jsonify({
        'status': 'success',
        'credential': credential.to_dict()
    })

@app.route('/wallet/credential')
def get_wallet_credential():
    """Get stored credential (for demo)"""
    credential = wallet.load_credential()
    if credential:
        return jsonify(credential.to_dict())
    return jsonify({'status': 'no_credential'}), 404

@app.route('/verifier/challenge', methods=['POST'])
def create_challenge():
    """Create a verification challenge"""
    challenge = secrets.token_hex(32)
    session_id = secrets.token_hex(16)
    stored_challenges[session_id] = {
        'challenge': challenge,
        'timestamp': datetime.now().isoformat()
    }
    
    return jsonify({
        'session_id': session_id,
        'challenge': challenge
    })

@app.route('/verifier/verify', methods=['POST'])
def verify():
    """Verify a proof"""
    data = request.json
    session_id = data.get('session_id')
    proof_data = data.get('proof')
    
    # Check session
    if session_id not in stored_challenges:
        return jsonify({
            'status': 'error',
            'message': 'Invalid session'
        }), 400
    
    session_data = stored_challenges[session_id]
    # Remove session to prevent replay
    del stored_challenges[session_id]
    
    # Verify proof
    proof_valid = verifier.verify_proof(proof_data)
    
    if not proof_valid:
        return jsonify({
            'status': 'error',
            'message': 'Invalid proof signature'
        }), 400
    
    # Check policy
    claim_type = proof_data.get('claim_type')
    value = proof_data.get('value')
    
    if policy_engine.check_policy(claim_type, value):
        return jsonify({
            'status': 'success',
            'message': 'Identity verified successfully!'
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Policy requirement not met'
        }), 403

@app.route('/verify_and_redirect', methods=['POST'])
def verify_and_redirect():
    """Verify and redirect to 18+ page"""
    data = request.json
    session_id = data.get('session_id')
    proof_data = data.get('proof')
    
    # Check session
    if session_id not in stored_challenges:
        return jsonify({
            'status': 'error',
            'message': 'Invalid session'
        }), 400
    
    # Remove session to prevent replay
    del stored_challenges[session_id]
    
    # Verify proof
    proof_valid = verifier.verify_proof(proof_data)
    
    if not proof_valid:
        return jsonify({
            'status': 'error',
            'message': 'Invalid proof signature'
        }), 400
    
    # Check policy
    claim_type = proof_data.get('claim_type')
    value = proof_data.get('value')
    
    if policy_engine.check_policy(claim_type, value):
        # User is 18+ - grant access
        return jsonify({
            'status': 'success',
            'message': 'Access granted - 18+ content unlocked',
            'redirect': '/success'
        })
    else:
        # User is NOT 18+
        return jsonify({
            'status': 'error',
            'message': 'Age verification failed - You must be 18+',
            'redirect': '/access_denied'
        }), 403

@app.route('/demo/setup', methods=['POST'])
def demo_setup():
    """Quick setup for demo"""
    data = request.json
    user_id = data.get('user_id', 'demo_user')
    birth_year = data.get('birth_year', 2000)
    
    # Issue credential
    credential = issuer.issue_credential(user_id, birth_year)
    wallet.store_credential(credential)
    
    return jsonify({
        'status': 'success',
        'message': 'Credential issued and stored',
        'credential': credential.to_dict()
    })

@app.route('/demo/proof', methods=['POST'])
def demo_proof():
    """Generate a proof for demo"""
    data = request.json
    challenge = data.get('challenge')
    claim_type = data.get('claim_type', 'AGE_OVER_18')
    
    if not challenge:
        return jsonify({'error': 'Challenge required'}), 400
    
    proof = wallet.generate_proof(claim_type, challenge)
    if proof:
        return jsonify({
            'status': 'success',
            'proof': proof.to_dict()
        })
    return jsonify({
        'status': 'error',
        'message': 'Could not generate proof'
    }), 400

@app.route('/reset', methods=['POST'])
def reset():
    """Reset the system"""
    import shutil
    
    # Reset wallet
    wallet_dir = 'storage/wallet'
    if os.path.exists(wallet_dir):
        shutil.rmtree(wallet_dir)
    
    # Reinitialize components
    global wallet, issuer
    issuer = Issuer()
    wallet = Wallet()
    verifier.set_authority_public_key(issuer.get_public_key())
    
    return jsonify({'status': 'success', 'message': 'System reset'})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("PROJECT SENTINEL v2 - Identity Handshake System")
    print("="*60)
    print("\nComponents:")
    print("  Authority: Issuer ready")
    print("  Wallet: Ready")
    print("  Verifier: Ready")
    print("\nDemo Setup:")
    print("  POST /demo/setup - Issue a demo credential")
    print("  GET / - Web interface")
    print("\n" + "="*60)
    print("Starting server at http://127.0.0.1:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)