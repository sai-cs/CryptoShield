# CryptoShield

CryptoShield is a simple, web-based encryption and decryption platform that demonstrates the use of AES (Advanced Encryption Standard). The platform allows users to securely encrypt and decrypt text using a user-defined 16-character key. This project is perfect for showcasing cryptography and web development skills.

## Features
- **AES Encryption**: Utilizes the industry-standard encryption algorithm for secure data handling.
- **Dynamic IVs**: Each encryption generates a unique Initialization Vector (IV) for added security.
- **User-Friendly Interface**: A clean, cyber-themed design for easy usability.
- **Flask-Powered Backend**: A Python-based backend ensures reliability and scalability.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Cryptography**: Python's `cryptography` library

## How It Works
1. **Encryption**:
   - Enter a 16-character key and the plaintext you want to encrypt.
   - The system generates a unique IV and encrypts the text.
   - The encrypted result is displayed as a Base64-encoded string.

2. **Decryption**:
   - Enter the same 16-character key and the ciphertext.
   - The system decrypts the text and displays the original plaintext.

## Installation
To run CryptoShield locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cryptoshield.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cryptoshield
   ```

3. Install the required dependencies:
   ```bash
   pip install flask cryptography flask-cors
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Use Cases
- Learning and demonstrating cryptography concepts.
- Showcasing web development skills using Flask.
- A lightweight example of secure data handling.

## Disclaimer
CryptoShield is an educational project created to showcase cryptography and web development skills. It is not intended for production use or to handle sensitive information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore, use, and modify CryptoShield for your learning and personal projects!
