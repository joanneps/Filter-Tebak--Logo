# Roadmap Proyek Filter Tebak Logo

Proyek ini bertujuan untuk bikin filter "Tebak Logo" yang bisa mendeteksi arah wajah (kiri/kanan) untuk memilih logo yang benar. Kita juga bakal nge-track skor berdasarkan jawaban dan waktu yang dipakai. Di bawah ini adalah langkah-langkah yang kita perlu kerjakan bersama.

---

## 1. Desain Tampilan dan Logo

- **Tugas**:
  - Siapin gambar logo yang bakal tampil di layar.
  - Tentuin posisi logo di kiri dan kanan layar.
  - Ukuran logo harus pas, nggak terlalu besar atau kecil (misalnya 200x200 px biar jelas).
  - Tempatin logo di posisi kiri dan kanan, sesuai dengan arah wajah yang terdeteksi.

---

## 2. Pengaturan Waktu Menebak

- **Tugas**:
  - Tentuin batas waktu buat jawab (misalnya 10 detik).
  - Gunakan timer buat nampilinn waktu yang tersisa di layar.
  - Kalo waktu habis, tampilkan hasilnya (jawaban benar atau salah).

---

## 3. Deteksi Wajah dan Arah Kepala

- **Tugas**:
  - Gunakan `dlib` buat deteksi wajah, ambil koordinat wajah (x, y, w, h).
  - Tentuin arah wajah: 
    - Kalo wajahnya ke kiri, tampilkan logo kiri.
    - Kalo wajahnya ke kanan, tampilkan logo kanan.
  - Setelah itu, tentuin apakah jawabannya benar atau salah, sesuai logo yang muncul.

---

## 4. Skor dan Hasil Akhir

- **Tugas**:
  - Hitung skor berdasarkan jawaban yang benar.
  - Tampilinn skor setelah tiap ronde.
  - Setelah beberapa ronde, tampilkan total skor akhir.

---

## 5. Pengujian dan Debugging

- **Tugas**:
  - Tes deteksi wajah, pastiin arah wajah terdeteksi dengan benar.
  - Uji coba tampilan logo, pastiin logo muncul dengan jelas di posisi yang tepat.
  - Tes juga di beberapa perangkat dan kondisi, biar deteksi wajahnya tetep akurat.

---

## 6. Fitur Opsional (Kalau Waktu Masih Ada)

- **Tugas**:
  - **Tingkat Kesulitan**: Bisa tambah opsi tingkat kesulitan, misalnya lebih banyak logo atau logo yang lebih mirip.
  - **Suara**: Tambahin efek suara pas jawabannya benar atau salah (biar lebih seru).
  - **Animasi**: Bisa tambahin animasi atau efek visual, misalnya pas wajah bergerak atau timer hampir habis.

---

## 7. Optimasi Kinerja

- **Tugas**:
  - Pastikan filter nggak nge-lag, terutama pas deteksi wajah dan nampilinn logo.
  - Uji coba di beberapa perangkat, pastiin semuanya berjalan lancar di berbagai kondisi.

---

## Pembagian Tugas

### Anggota Tim:
- **[Nama Anggota 1]**:
- **[Nama Anggota 2]**:
- **[Nama Anggota 3]**:

---

## Langkah-Langkah Proyek:

1. **Siapkan Logo**: Bikin gambar logo dan tentuin tata letak di layar.
2. **Timer**: Tentuin berapa lama waktu yang diberikan buat jawab.
3. **Deteksi Arah Wajah**: Gunakan `dlib` buat deteksi wajah, tentuin arah wajah (kiri/kanan).
4. **Penilaian dan Skor**: Tentuin jawaban benar atau salah dan hitung skor.
5. **Testing**: Tes deteksi wajah, logo, dan pastikan semua berjalan lancar.
6. **Fitur Opsional**: Tambahin tingkat kesulitan, suara, dan animasi.
7. **Optimasi**: Pastikan filter jalan mulus tanpa gangguan.

---

Dengan adanya roadmap ini, diharapkan agar mempermudah pengerjaan proyek secara terstruktur.