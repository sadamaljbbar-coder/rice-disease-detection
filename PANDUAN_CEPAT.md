# 🚀 Panduan Cepat - Sistem Deteksi Penyakit Padi

## Persyaratan Sistem

1. **Python 3.8+** - Download dari [python.org](https://www.python.org/downloads/)
2. **Akun Roboflow** - Daftar gratis di [roboflow.com](https://roboflow.com)
3. **Model Roboflow** - Gunakan model yang sudah dilatih (rice-deases-ofyxk/5)

---

## Langkah-Langkah Setup

### Langkah 1: Download Project

```bash
# Clone atau download project ini
# Letakkan di folder yang mudah diakses
```

### Langkah 2: Dapatkan API Key Roboflow

1. Login ke [app.roboflow.com](https://app.roboflow.com)
2. Klik nama Anda di pojok kanan atas
3. Pilih "Settings"
4. Copy "API Key" Anda

### Langkah 3: Konfigurasi Environment

```bash
# Masuk ke folder project
cd rice_disease_project

# Copy file konfigurasi
cp .env.example .env

# Edit file .env
# Ganti 'your_api_key_here' dengan API Key Roboflow Anda
```

Contoh isi file `.env`:
```
ROBOFLOW_API_KEY=abc123xyz456
ROBOFLOW_MODEL_ID=rice-deases-ofyxk/5
```

### Langkah 4: Install Dependencies

```bash
# Windows
pip install -r requirements.txt

# Linux/Mac
pip3 install -r requirements.txt
```

### Langkah 5: Jalankan Server

```bash
# Masuk ke folder backend
cd backend

# Jalankan server
python app.py
```

Jika berhasil, Anda akan melihat:
```
============================================================
🌾 Rice Disease Detection System
============================================================
📡 Starting server on http://0.0.0.0:5000
🔧 Debug mode: True
🤖 Roboflow Model: rice-deases-ofyxk/5
============================================================
```

### Langkah 6: Buka Aplikasi

1. Buka browser (Chrome, Firefox, Edge)
2. Akses `http://localhost:5000`
3. Upload gambar daun padi
4. Lihat hasil deteksi dan rekomendasi!

---

## Troubleshooting

### Error: "ROBOFLOW_API_KEY not set"
- Pastikan file `.env` ada dan berisi API key yang benar
- Restart server setelah mengubah `.env`

### Error: "Module not found"
```bash
pip install flask flask-cors requests python-dotenv Pillow
```

### Error: "Address already in use"
- Port 5000 sudah digunakan
- Edit `config.py` dan ganti PORT ke angka lain (misal 5001)

### Error: "API Error: 401"
- API Key salah atau expired
- Dapatkan API Key baru dari Roboflow

### Gambar tidak terdeteksi dengan benar
- Pastikan gambar jelas dan fokus pada daun
- Hindari gambar yang blur atau gelap
- Ukuran file maksimal 10MB

---

## Tips Penggunaan

### Untuk Hasil Terbaik:
1. 📸 Ambil foto daun dari jarak 30-50 cm
2. ☀️ Pastikan pencahayaan cukup (tidak terlalu gelap/terang)
3. 🎯 Fokuskan pada area yang menunjukkan gejala
4. 📱 Gunakan kamera dengan resolusi minimal 5MP

### Interpretasi Hasil:
- **Confidence > 90%**: Hasil sangat yakin
- **Confidence 70-90%**: Hasil cukup yakin
- **Confidence < 70%**: Perlu verifikasi ulang

---

## Struktur Project

```
rice_disease_project/
├── backend/
│   ├── app.py              # Server Flask
│   ├── config.py           # Konfigurasi
│   ├── roboflow_client.py  # Koneksi ke Roboflow
│   └── dss/
│       ├── knowledge_base.py  # Database penyakit
│       └── recommender.py     # Engine rekomendasi
├── frontend/
│   ├── index.html          # Halaman utama
│   ├── css/style.css       # Styling
│   └── js/app.js           # Logic frontend
├── docs/
│   └── API_DOCUMENTATION.md
├── .env                    # Konfigurasi (buat manual)
├── .env.example            # Contoh konfigurasi
├── requirements.txt        # Dependencies Python
└── README.md
```

---

## Kontak & Bantuan

Jika mengalami kendala:
1. Baca dokumentasi API di `docs/API_DOCUMENTATION.md`
2. Periksa log error di terminal
3. Pastikan semua langkah sudah diikuti dengan benar

---

**Selamat menggunakan! 🌾**
