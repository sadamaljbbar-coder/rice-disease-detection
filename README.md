# 🌾 Sistem Deteksi Penyakit Daun Padi Berbasis Vision Transformer

## Dengan Integrasi Web IoT dan Decision Support System

---

## 📋 Daftar Isi

1. [Arsitektur Sistem](#arsitektur-sistem)
2. [Persyaratan](#persyaratan)
3. [Langkah Implementasi](#langkah-implementasi)
4. [Struktur Folder](#struktur-folder)
5. [Cara Menjalankan](#cara-menjalankan)
6. [Setup untuk macOS](#setup-untuk-macos)

---

## 🏗️ Arsitektur Sistem

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │   Frontend Web  │────▶│  Backend API    │────▶│  Roboflow API   │
│   User Device   │────▶│   (HTML/JS/CSS) │     │  (Python Flask) │     │  (ViT Model)    │
│                 │     │                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └────────┬────────┘     └─────────────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │   Decision      │
                                                │   Support       │
                                                │   System        │
                                                │   (Knowledge DB)│
                                                └─────────────────┘
```

---

## 📦 Persyaratan

### Software
- Python 3.8+
- Node.js (opsional, untuk development)
- Web Browser modern

### Python Libraries
```
flask==3.0.0
flask-cors==4.0.0
requests==2.31.0
python-dotenv==1.0.0
Pillow==12.1.0
gunicorn==21.2.0
inference-sdk==0.9.0
numpy==2.0.0
```

---

## 🚀 Setup untuk macOS

### Langkah 1: Install Miniconda (jika belum ada)
```bash
# Download dan install Miniconda untuk macOS
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh  # untuk Apple Silicon
# atau
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh  # untuk Intel

bash Miniconda3-latest-MacOSX-*.sh
```

### Langkah 2: Setup Environment
```bash
# Buka terminal dan navigasi ke folder project
cd path/to/rice_disease_project

# Buat environment baru
conda create -n rice-env python=3.10 -y

# Aktifkan environment
conda activate rice-env

# Install dependencies
pip install -r requirements.txt
```

### Langkah 3: Setup Environment Variables
Pastikan file `.env` ada di root folder dengan isi:
```
ROBOFLOW_API_KEY=your_api_key_here
ROBOFLOW_MODEL_ID=rice-deases-ofyxk/5
```

### Langkah 4: Jalankan Aplikasi
```bash
# Dari folder root project
./run.sh
```

Atau manual:
```bash
cd backend
python app.py
```

### Langkah 5: Akses Aplikasi
Buka browser ke: `http://localhost:5000`

---

## 💻 Cara Menjalankan (Windows/Linux)
python-dotenv
Pillow
```

### Akun & API
- Akun Roboflow (sudah ada model ViT dengan akurasi 98.1%)
- Roboflow API Key

---

## 🚀 Langkah Implementasi

### Langkah 1: Setup Roboflow API
1. Login ke Roboflow
2. Buka project "Rice Diseases 5"
3. Copy API Key dari Settings

### Langkah 2: Setup Backend
1. Install dependencies: `pip install -r requirements.txt`
2. Buat file `.env` dengan API key
3. Jalankan server: `python app.py`

### Langkah 3: Setup Frontend
1. Buka folder `frontend`
2. Buka `index.html` di browser

### Langkah 4: Testing
1. Upload gambar daun padi
2. Lihat hasil deteksi dan rekomendasi

---

## 📁 Struktur Folder

```
rice_disease_project/
├── README.md
├── requirements.txt
├── .env.example
├── backend/
│   ├── app.py                 # Flask server utama
│   ├── config.py              # Konfigurasi
│   ├── roboflow_client.py     # Roboflow API client
│   └── dss/
│       ├── __init__.py
│       ├── knowledge_base.py  # Database pengetahuan penyakit
│       └── recommender.py     # Engine rekomendasi
├── frontend/
│   ├── index.html             # Halaman utama
│   ├── css/
│   │   └── style.css          # Styling
│   └── js/
│       └── app.js             # Logic frontend
└── docs/
    └── API_DOCUMENTATION.md   # Dokumentasi API
```

---

## ▶️ Cara Menjalankan

### Development Mode
```bash
# 1. Clone/download project
# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env
# Edit .env dengan API key Anda

# 4. Jalankan backend
cd backend
python app.py

# 5. Buka frontend di browser
# Buka file frontend/index.html
```

### Production Mode
Gunakan Gunicorn atau deploy ke cloud platform seperti:
- Heroku
- Railway
- Google Cloud Run
- AWS Lambda

---

## 📞 Kontak

M. SADAM - Universitas Pendidikan Indonesia

---

## 📄 Lisensi

MIT License - Bebas digunakan untuk keperluan akademik dan penelitian.
