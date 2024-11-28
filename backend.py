from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests


def encrypt(plaintext, key):
    # Generate a random IV for each encryption
    iv = os.urandom(16)

    # Add padding to plaintext
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Perform AES encryption with the random IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and ciphertext (IV is needed for decryption)
    encrypted_data = iv + ciphertext
    return base64.b64encode(encrypted_data).decode()  # Encode as Base64 for easier transport


def decrypt(ciphertext, key):
    # Decode the Base64 encoded ciphertext
    encrypted_data = base64.b64decode(ciphertext)

    # Extract the IV (first 16 bytes) and the actual ciphertext
    iv = encrypted_data[:16]
    actual_ciphertext = encrypted_data[16:]

    # Perform AES decryption with the extracted IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Remove padding from the decrypted plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()


# Serve the frontend
@app.route('/')
def serve_frontend():
    return render_template('index.html')  # Renders index.html from a 'templates' folder


@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.json
    plaintext = data.get('plaintext', '')
    key = data.get('key', '')

    if len(key) != 16:
        return jsonify({'error': 'Key must be 16 characters long!'}), 400

    try:
        encrypted_text = encrypt(plaintext, key.encode())  # Convert key to bytes
        return jsonify({'encrypted': encrypted_text})
    except Exception as e:
        return jsonify({'error': 'Encryption failed!', 'details': str(e)}), 400


@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.json
    ciphertext = data.get('ciphertext', '')
    key = data.get('key', '')

    if len(key) != 16:
        return jsonify({'error': 'Key must be 16 characters long!'}), 400

    try:
        decrypted_text = decrypt(ciphertext, key.encode())  # Convert key to bytes
        return jsonify({'decrypted': decrypted_text})
    except Exception as e:
        return jsonify({'error': 'Decryption failed!', 'details': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
