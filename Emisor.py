import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Configuración
SERVER_IP = '192.168.254.147'
PORT = 5000

# Clave de 32 bytes para AES-256
KEY = b'12345678901234567890123456789012'

aesgcm = AESGCM(KEY)

# Generar nonce aleatorio
nonce = os.urandom(12)

mensaje = b"Configuracion sensible: DB_PASSWORD=admin123"

# Cifrado
texto_cifrado = aesgcm.encrypt(nonce, mensaje, None)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))

    # Enviar nonce + mensaje cifrado
    s.sendall(nonce + texto_cifrado)

    print("Mensaje cifrado enviado.")