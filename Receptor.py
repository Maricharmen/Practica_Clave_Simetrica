import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PORT = 5000
KEY = b'12345678901234567890123456789012'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', PORT))
    s.listen(1)

    print("Esperando configuración...")

    conn, addr = s.accept()

    with conn:
        data = conn.recv(1024)

        nonce = data[:12]
        cifrado = data[12:]

        aesgcm = AESGCM(KEY)

        mensaje = aesgcm.decrypt(nonce, cifrado, None)

        print(f"Mensaje seguro recibido: {mensaje.decode()}")