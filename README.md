## Specifications

- Description
  Data Scraping untuk men-download File Images berupa manga untuk Manga yang di-inginkan dengan chapter yang diharapkan

- Specification (optional)

- How to use

  1. Program dijalankan pada directory Seleksi-2019-Tugas-1
  2. Untuk menghapus data terlebih dahulu run

  ```
    python3 src/cleaner.py
  ```

  3. Untuk melakukan Scraping run

  ```
    python3 src/scraper.y
  ```

  Pada Program ini, akan diminta input dari nama Manga yang ingin di-unduh dan Chapter berapa dari Manga tersebut

- Ideas and innovations in utilizing the data
  Idea untuk program ini adalah untuk mempermudah membaca manga sehingga tidak perlu mencari-cari website untuk membaca. Digunakan juga untuk mengkoleksi manga yang ada

- JSON Structure
  {
  Name : 'Nama Manga',
  Chapter : 'Chapter Manga',
  Time Downloaded : 'Waktu dimana Program atau Manga di-download',
  Images Downloaded : 'Foto-foto Page Manga yang didownload'
  }

- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)

- Reference (Library used, etc)
  1. bs4
  2. requests
  3. wget
  4. datetime
  5. json
  6. os
  7. glob
