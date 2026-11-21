# Skor UTBK Universitas Sultan Ageng Tirtayasa

Repositori ini berisi kumpulan data nilai minimum UTBK–SNBT untuk program studi Universitas Sultan Ageng Tirtayasa (Untirta) pada tahun 2023–2026. Data dikumpulkan dari halaman resmi [PMB Untirta](https://pmb.untirta.ac.id) dan disimpan dalam format CSV untuk memudahkan pencarian, pengolahan, dan analisis.

## Daftar Data per Tahun

| Tahun | Data CSV | Sumber |
| --- | --- | --- |
| 2026 | [utbk-2026.csv](data/2026/utbk-2026.csv) | [PMB Untirta 2026](https://pmb.untirta.ac.id/nilai-minimum-snbt-2026/) |
| 2025 | [utbk-2025.csv](data/2025/utbk-2025.csv) | [PMB Untirta 2025](https://pmb.untirta.ac.id/nilai-minimum-utbk-snbt-2025/) |
| 2024 | [utbk-2024.csv](data/2024/utbk-2024.csv) | [PMB Untirta 2024](https://pmb.untirta.ac.id/nilai-minimum-utbk-2024/) |
| 2023 | [utbk-2023.csv](data/2023/utbk-2023.csv) | [PMB Untirta 2023](https://pmb.untirta.ac.id/nilai-minimum-utbk-snbt-per-prodi-tahun-2023/) |

Seluruh referensi sumber juga tercatat pada [`data/referensi.csv`](data/referensi.csv).

> [!IMPORTANT]
> Format kolom pada setiap berkas CSV dapat berbeda antara tahun, tergantung dari format tabel di halaman PMB Untirta.

> [!IMPORTANT]
> Berkas-berkas CSV dalam repositori ini menggunakan pemisah titik koma (`;`) sebagai pengganti koma (`,`) dikarenakan penggunaan koma sebagai pemisah desimal pada beberapa kolom.

## Penggunaan Skrip Pengambilan Data

Pastikan Python sudah terpasang, lalu instal dependensi:

```bash
python -m pip install -r requirements.txt
```

Jalankan skrip dari direktori `scripts` dengan menyertakan URL sumber dan tahun:

```bash
cd scripts
python main.py "URL_REFERENSI" TAHUN
```

Contoh:

```bash
python main.py "https://pmb.untirta.ac.id/nilai-minimum-snbt-2026/" 2026
```

## Lisensi

- **Kode:** skrip Python di `scripts/` dilisensikan di bawah [MIT License](LICENSE).
- **Data:** berkas dan hasil olahan di `data/` dilisensikan di bawah [CC BY 4.0](LICENSE-DATA).

Data bersumber dari [PMB Untirta](https://pmb.untirta.ac.id/). Situs sumber tidak mencantumkan lisensi yang jelas untuk datanya, sehingga lisensi repositori tidak menjamin hak atas konten asli. Daftar sumber tersedia pada [`data/referensi.csv`](data/referensi.csv).
