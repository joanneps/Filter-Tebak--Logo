# Roadmap Proyek Filter Tebak Logo

Proyek ini bertujuan untuk membuat filter "Tebak Logo" yang bisa mendeteksi arah wajah (kiri/kanan) untuk memilih logo yang benar. Kita juga akan nge-track skor berdasarkan jawaban dan waktu yang dipakai. Di bawah ini adalah langkah-langkah yang perlu dikerjakan bersama.

---

## 1. Desain Tampilan dan Logo

- **Tugas**:
  - Siapkan gambar logo yang akan tampil di layar.
  - Tentukan posisi logo di kiri dan kanan layar.
  - Ukuran logo harus pas, tidak terlalu besar atau kecil (misalnya 200x200 px biar jelas).
  - Tempatkan logo di posisi kiri dan kanan, sesuai dengan arah wajah yang terdeteksi.

---

## 2. Pengaturan Waktu Menebak

- **Tugas**:
  - Tentukan batas waktu untuk menebak logo (misalnya 10 detik).
  - Gunakan timer untuk menampilkan waktu yang tersisa di layar.
  - Jika waktu habis, tampilkan hasilnya (jawaban benar atau salah).

---

## 3. Deteksi Wajah dan Arah Kepala

- **Tugas**:
  - Gunakan `dlib` untuk deteksi wajah, ambil koordinat wajah (x, y, w, h).
  - Tentukan arah wajah: 
    - Jika wajahnya ke kiri, tampilkan logo kiri.
    - Jika wajahnya ke kanan, tampilkan logo kanan.
  - Setelah itu, tentukan apakah jawabannya benar atau salah, sesuaikan logo yang muncul.

---

## 4. Skor dan Hasil Akhir

- **Tugas**:
  - Hitung skor berdasarkan jawaban yang benar.
  - Tampilkan skor setelah tiap ronde.
  - Setelah beberapa ronde, tampilkan total skor akhir.

---

## 5. Pengujian dan Debugging

- **Tugas**:
  - Tes deteksi wajah, pastikan arah wajah terdeteksi dengan benar.
  - Uji coba tampilan logo, pastikan logo muncul dengan jelas di posisi yang tepat.
  - Tes juga di beberapa perangkat dan kondisi, agar deteksi wajahnya tetep akurat.

---

## 6. Fitur Opsional (Kalau Waktu Masih Ada)

- **Tugas**:
  - **Tingkat Kesulitan**: Bisa tambah opsi tingkat kesulitan, misalnya lebih banyak logo atau logo yang lebih mirip.
  - **Suara**: Tambahin efek suara ketika jawabannya benar atau salah (agar lebih seru).
  - **Animasi**: Bisa tambahin animasi atau efek visual, misalnya pas wajah bergerak atau timer hampir habis.

---

## 7. Optimasi Kinerja

- **Tugas**:
  - Pastikan filter nggak nge-lag, terutama pas deteksi wajah dan nampilinn logo.
  - Uji coba di beberapa perangkat, pastiin semuanya berjalan lancar di berbagai kondisi.

---

## Pembagian Tugas

### Anggota Tim:
- **[Joanne Polama Putri Sembiring]**:
- **[Muhammad Taqy Abdullah]**:
- **[Dea Lisriani Safitri Waruwu]**:

---

## Langkah-Langkah Proyek:

1. **Siapkan Logo**: Bikin gambar logo dan tentuin tata letak di layar.
2. **Timer**: Tentukan berapa lama waktu yang diberikan buat jawab.
3. **Deteksi Arah Wajah**: Gunakan `dlib` buat deteksi wajah, tentukan arah wajah (kiri/kanan).
4. **Penilaian dan Skor**: Tentukan jawaban benar atau salah dan hitung skor.
5. **Testing**: Tes deteksi wajah, logo, dan pastikan semua berjalan lancar.
6. **Fitur Opsional**: Tambahkan tingkat kesulitan, suara, dan animasi.
7. **Optimasi**: Pastikan filter jalan mulus tanpa gangguan.

---

Dengan adanya roadmap ini, diharapkan agar mempermudah pengerjaan proyek secara terstruktur.
