# Filter Tebak Logo

Anggota Kelompok
NAMA                             | NIM             | ID Github
:------------------------------: | :-------------: | :---------------:
[Joanne Polama Putri Sembiring]  | [121140128]     | joanneps
[Muhammad Taqy Abdullah]         | [121140166]     | 166Taqy
[Dea Lisriani Safitri Waruwu]    | [121140208]     | Deawaruwu04


## Deskripsi:
Filter Tebak Logo adalah program sederhana berbasis kamera memanfaatkan teknologi deteksi wa-
jah untuk memprediksi arah wajah pengguna (kiri atau kanan) sebagai input jawaban yang dibuat
menggunakan Python. Program ini dirancang untuk memilih logo yang benar antara dua opsi. Dalam
filter ini pengguna akan menebak logo berdasarkan gambar yang ditampilkan di atas kepala pengguna.
Filter ini akan mendeteksi arah gerakan kepala pengguna apakah ke kiri atau ke kanan. Pengguna
diberi batas waktu untuk menebak logo, jika waktu habis sebelum permainan selesai maka skor akan
langsung ditampilkan. Filter akan memberikan notifikasi atau tanda apakah tebakannya benar atau
salah dan akan menampilkan skor di akhir permainan. Program ini dibuat untuk menghibur sekaligus
memberikan pengalaman unik kepada pengguna dengan melibatkan interaksi langsung melalui gerakan
wajah. Teknologi utama yang digunakan dalam progam ini adalah OpenCV dan dlib

## Instruksi Instalasi:
1. Pastikan library berikut sudah terinstall di pyhton anda :
   - OpenCV (`pip install opencv-python dlib`)
2. Siapkan gambar logo yang akan digunakan dalam filter. Buat folder assets di dalam direktori lalu tambahkan gambar logo dengan nama file berikut:
     - filabenar.JPG
     - filasalah.JPG
     - instagrambenar.JPG
     - instagramsalah.JPG
     - kfcbenar.JPG
     - kfcsalah.JPG
     - mercedesbenar.JPG
     - mercedessalah.JPG
     - oreobenar.JPG
     - oreosalah.JPG
3. Jalankan script dengan perintah berikut:
   `python script.py`

## Cara Bermain
1. Saat permainan dimulai, dua logo akan muncul di layar (satu benar satu salah) pada posisi atas kiri kanan
2. Lihat ke kamera dan arahkan wajah/kepala anda ke kiri atau ke kanan untuk memilih logo
3. Filter akan memberi tahu jika jawaban anda benar atau salah
4. Permainan berlangsung selama 30 detik dan skor akan ditampilkan di akhir permainan



## Logbook
MINGGU KE-                         | KEGIATAN            
:------------------------------:   | :-------------: 
Minggu ke-1 (24-30 November 2024)  | Mencari berbagai referensi filter di TikTok    
Minggu ke-2 (1-7 Desember 2024)    | Diskusi terkait judul final project + mengajukan judul (acc)     
Minggu ke-3 (8-14 Desember 2024)   | Mengerjakan code program + mencari 'assets' yang diperlukan untuk filter
Minggu ke-4 (15-21 Desember 2024)  | Mengerjakan code program + mencicil laporan
Minggu ke-5 (22-24 Desember 2024)  | Melakukan cross ceck program dan laporan + submit final project ke gform pengumpulan
