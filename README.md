# ChatScraper

ChatScraper adalah aplikasi web yang memungkinkan pengguna untuk mengelola dan menyimpan percakapan ChatGPT. Aplikasi ini menyediakan fitur untuk melakukan scraping data percakapan dari link ChatGPT, memproses teks percakapan, dan menampilkan riwayat percakapan yang telah disimpan.

## Fitur

- **Registrasi dan Login**: Pengguna dapat mendaftar dan masuk ke aplikasi.
- **Submit Link ChatGPT**: Pengguna dapat memasukkan link percakapan ChatGPT untuk disimpan.
- **Scraping Data**: Aplikasi akan melakukan scraping data dari link yang diberikan.
- **Preprocessing Teks**: Teks percakapan akan diproses untuk menghapus tanda baca, angka, dan spasi berlebih.
- **Riwayat Percakapan**: Pengguna dapat melihat riwayat percakapan yang telah disimpan.
- **Detail Percakapan**: Pengguna dapat melihat detail percakapan yang telah diproses.

## Instalasi

1. Clone repositori ini:

    ```sh
    git clone https://github.com/JasonSlav/scrape-gpt.git
    cd scrape-gpt
    ```

2. Buat virtual environment dan aktifkan:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Untuk pengguna Unix/macOS
    venv\Scripts\activate  # Untuk pengguna Windows
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Buat file `.env` berdasarkan `.env.example` dan isi dengan konfigurasi yang sesuai:

    ```sh
    cp .env.example .env
    ```

5. Jalankan migrasi database:

    ```sh
    flask db upgrade
    ```

6. Jalankan aplikasi:

    ```sh
    flask run
    ```

## Struktur Proyek

```
.
├── .env
├── .env.example
├── .gitignore
├── app.py
├── config.py
├── index.html
├── models/
│   ├── __init__.py
│   ├── conversation.py
│   ├── user.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── scrape.py
├── scraper/
│   ├── preprocess.py
│   ├── scraper.py
├── static/
│   ├── flash.css
│   ├── index.js
│   ├── navbar.js
│   ├── script.js
│   ├── style.css
├── templates/
│   ├── chat.html
│   ├── history.html
│   ├── home.html
│   ├── index.html
│   ├── navbar.html
│   ├── preprocess.html
└── requirements.txt
```

## Penggunaan

1. Buka browser dan akses `http://localhost:5000`.
2. Daftar akun baru atau login dengan akun yang sudah ada.
3. Masukkan link percakapan ChatGPT pada halaman utama dan klik "Submit Link".
4. Klik "Nama Deskripsi Chat" di sebelah kiri untuk melihat detail percakapan yang telah diproses.
5. Lihat riwayat dan detail preprocessed text pada halaman "Riwayat".

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan buat pull request dengan perubahan yang Anda usulkan.

