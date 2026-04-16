# 🐧 Palmer Penguins Species Classifier

Aplikasi web untuk mengklasifikasikan spesies penguin dari dataset **Palmer Penguins** menggunakan algoritma **K-Nearest Neighbors (KNN)** dan framework **Flask**.

---

## 📋 Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Spesies Penguin](#spesies-penguin)
- [Teknologi](#teknologi)
- [Struktur Proyek](#struktur-proyek)
- [Instalasi & Menjalankan](#instalasi--menjalankan)
- [Cara Penggunaan](#cara-penggunaan)
- [Fitur](#fitur)
- [Dataset](#dataset)

---

## 📌 Tentang Proyek

Proyek ini merupakan aplikasi machine learning berbasis web yang mampu memprediksi spesies penguin berdasarkan empat pengukuran fisik:

| Parameter | Satuan | Rentang Umum |
|---|---|---|
| Bill Length (Panjang Paruh) | mm | 32 – 60 mm |
| Bill Depth (Kedalaman Paruh) | mm | 13 – 22 mm |
| Flipper Length (Panjang Sirip) | mm | 170 – 235 mm |
| Body Mass (Berat Badan) | gram | 2700 – 6300 g |

Model KNN dilatih menggunakan dataset Palmer Penguins dan disimpan dalam format **Pickle** untuk dimuat ulang tanpa perlu melatih kembali.

---

## 🐧 Spesies Penguin

| Spesies | Nama Ilmiah | Ciri Khas |
|---|---|---|
| **Adélie** | *Pygoscelis adeliae* | Cincin putih di sekitar mata, paruh pendek |
| **Chinstrap** | *Pygoscelis antarcticus* | Garis hitam tipis di bawah dagu |
| **Gentoo** | *Pygoscelis papua* | Bercak putih di kepala, paruh oranye, terbesar |

---

## 🛠️ Teknologi

**Back End:**
- Python 3.x
- Flask
- scikit-learn (KNN)
- NumPy
- Pickle

**Front End:**
- HTML5 + CSS3
- Vanilla JavaScript
- Jinja2 Templating
- Google Fonts (Inter, JetBrains Mono)

---

## 📁 Struktur Proyek

```
Pwpb/
├── app.py                      # Server Flask & endpoint prediksi
├── model_penguin_knn.pickle    # Model KNN (sudah dilatih)
├── templates/
│   └── index.html              # Halaman utama (UI + Jinja2)
├── env/                        # Virtual environment (opsional)
└── README.md
```

---

## ⚙️ Instalasi & Menjalankan

### 1. Clone / Download Proyek

```bash
git clone <url-repo>
cd Pwpb
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv env
```

Aktifkan:
- **Windows:** `env\Scripts\activate`
- **Mac/Linux:** `source env/bin/activate`

### 3. Install Dependencies

```bash
pip install flask numpy scikit-learn
```

### 4. Jalankan Server

```bash
python app.py
```

### 5. Buka di Browser

```
http://127.0.0.1:5000/
```

---

## 🚀 Cara Penggunaan

1. **Buka aplikasi** di browser `http://127.0.0.1:5000/`
2. **Scroll ke section Prediksi** atau klik menu navbar **"Prediksi"**
3. **Isi parameter** pengukuran fisik penguin pada form, atau
4. **Gunakan tombol "⚡ Coba Data"** di kartu spesies untuk mengisi otomatis
5. **Klik "Prediksi Spesies 🚀"** dan lihat hasilnya

### Contoh Data Per Spesies

| Spesies | Bill Length | Bill Depth | Flipper Length | Body Mass |
|---|---|---|---|---|
| Adélie | 39 mm | 18 mm | 190 mm | 3700 g |
| Chinstrap | 55 mm | 20 mm | 200 mm | 4500 g |
| Gentoo | 48 mm | 15 mm | 217 mm | 5000 g |

---

## ✨ Fitur

- 🎨 **Dark theme modern** dengan efek glassmorphism dan warna nyaman di mata
- 🌨️ **Animasi snowflake** bernuansa Antartika
- 📚 **Informasi lengkap** tiap spesies (habitat, makanan, tinggi, berat, populasi)
- ❄️ **Fakta menarik** tentang penguin Palmer
- ⚡ **Tombol auto-fill** untuk mengisi form dengan data contoh spesies
- 🔮 **Prediksi real-time** menggunakan model KNN
- 📱 **Responsive** untuk desktop, tablet, dan mobile
- 🧭 **Smooth scroll navbar** dengan offset untuk navbar fixed
- 👥 **Section Tim Kelompok** untuk presentasi

---

## 📊 Dataset

Dataset **Palmer Penguins** dikumpulkan oleh **Dr. Kristen Gorman** dari Palmer Station, Antartika sebagai bahan riset dan alternatif modern dari dataset Iris.

- **Jumlah data:** 344 sampel
- **Jumlah spesies:** 3 (Adélie, Chinstrap, Gentoo)
- **Sumber:** [palmerpenguins.github.io](https://allisonhorst.github.io/palmerpenguins/)

---

## 📝 Lisensi

Proyek ini dibuat sebagai tugas presentasi / pembelajaran. Dataset Palmer Penguins dilisensikan di bawah [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
