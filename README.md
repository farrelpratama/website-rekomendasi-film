# 🎬 Recomovie — Film Recommendation Web App

Recomovie adalah aplikasi web berbasis **Django** yang menyediakan fitur pencarian film, detail film, review & rating, bookmark, serta sistem rekomendasi film berbasis **OMDb API**. Aplikasi ini dirancang sebagai project akademik yang menerapkan praktik pengembangan web modern dan siap untuk dideploy.

---

## ✨ Fitur Utama

* 🔍 **Search Film** menggunakan OMDb API
* 📄 **Detail Film** (poster, genre, durasi, rating IMDb, plot)
* ⭐ **Review & Rating (bintang)** oleh user
* 🔖 **Bookmark Film** (simpan & hapus)
* 👤 **Authentication** (Register, Login, Logout)
* 🧑 **Profile Page** berisi daftar bookmark
* 🎲 **Random Recommendation** di homepage
* ⭐ **Bookmark-Based Recommendation** (personalized)

---

## 🛠️ Teknologi yang Digunakan

* **Backend** : Python 3.12, Django
* **Frontend** : Django Template + Bootstrap
* **API** : OMDb API (Open Movie Database)
* **Database** : SQLite 
* **Deployment** : Render

---

## ⚙️ Instalasi Lokal

### 1️⃣ Clone Repository

```bash
git clone https://github.com/USERNAME/cinescope.git
cd cinescope
```

### 2️⃣ Buat & Aktifkan Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac / Linux
source venv/bin/activate
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Konfigurasi Environment Variable

Buat file `.env` (opsional untuk lokal):

```
SECRET_KEY=your-secret-key
OMDB_API_KEY=your-omdb-api-key
DEBUG=True
```

### 5️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Jalankan Server

```bash
python manage.py runserver
```

Akses aplikasi di:

```
http://127.0.0.1:8000/
```

##

---

## 👨‍💻 Author

* Nama  : *Farrel Edrik Pratama*
* NIM   : *25/559602/SV/26319*
* Prodi : *Teknologi Rekayasa Internet*

##
