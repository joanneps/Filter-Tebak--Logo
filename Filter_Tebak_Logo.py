import cv2
import dlib
import time
import random

# Inisialisasi detektor wajah
detector = dlib.get_frontal_face_detector()

# Fungsi untuk menampilkan teks di layar
def show_text(frame, text, position, font_scale=1, color=(0, 255, 0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = max(0, position[0] - text_size[0] // 2)
    text_y = position[1] + text_size[1] // 2
    if text_x + text_size[0] > frame.shape[1]:
        text_x = frame.shape[1] - text_size[0]
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness)

# Fungsi untuk menambahkan gambar ke frame
def overlay_image(frame, image, position):
    x, y = position
    h, w, _ = image.shape
    if y + h > frame.shape[0] or x + w > frame.shape[1]:
        return  # Jangan menggambar jika posisi keluar dari frame
    frame[y:y+h, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 0.5, image, 0.5, 0)

# Fungsi untuk menampilkan jeda sebelum pertanyaan berikutnya
def pause_with_message(frame, message, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        frame_copy = frame.copy()
        show_text(frame_copy, message, (frame_copy.shape[1] // 2, frame_copy.shape[0] // 2), font_scale=1.5, color=(0, 255, 255))
        cv2.imshow("Tebak Logo", frame_copy)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Buka kamera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Tidak dapat mengakses kamera.")
    exit()

# Load daftar gambar benar dan salah
logo_pairs = [
    ("assets/filabenar.JPG", "assets/filasalah.JPG"),
    ("assets/instagrambenar.JPG", "assets/instagramsalah.JPG"),
    ("assets/kfcbenar.JPG", "assets/kfcsalah.JPG"),
    ("assets/mercedesbenar.JPG", "assets/mercedessalah.JPG"),
    ("assets/oreobenar.JPG", "assets/oreosalah.JPG")
]

# Validasi dan resize gambar
for i, (benar_path, salah_path) in enumerate(logo_pairs):
    benar = cv2.imread(benar_path)
    salah = cv2.imread(salah_path)
    if benar is None or salah is None:
        print(f"Gambar pada pasangan {i+1} tidak ditemukan: {benar_path}, {salah_path}")
        exit()
    logo_pairs[i] = (cv2.resize(benar, (150, 150)), cv2.resize(salah, (150, 150)))

# Variabel permainan
score = 0
start_time = time.time()
game_duration = 30  # Batas waktu dalam detik

# Indeks pasangan logo yang belum digunakan
unused_indices = list(range(len(logo_pairs)))

# Permainan dimulai
current_pair = None
current_answer = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat membaca frame.")
        break

    # Balikkan frame agar tidak mirror
    frame = cv2.flip(frame, 1)

    # Konversi frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = detector(gray)

    # Pilih pasangan baru jika tidak ada pasangan aktif
    if current_pair is None:
        if unused_indices:  # Jika masih ada gambar yang tersisa
            index = random.choice(unused_indices)
            unused_indices.remove(index)
            current_pair = logo_pairs[index]
            current_answer = "Kiri" if random.choice([True, False]) else "Kanan"
        else:
            # Jika semua gambar habis
            pause_with_message(frame, f"Skor Akhir Kamu: {score}", 5)
            break

    # Tentukan posisi gambar berdasarkan jawaban
    if current_answer == "Kiri":
        benar_pos = (50, 50)
        salah_pos = (frame.shape[1] - 200, 50)
    else:
        benar_pos = (frame.shape[1] - 200, 50)
        salah_pos = (50, 50)

    # Tambahkan gambar ke frame
    overlay_image(frame, current_pair[0], benar_pos)
    overlay_image(frame, current_pair[1], salah_pos)

    # Tampilkan jawaban yang diminta
    show_text(frame, f"Tebak logo!", (frame.shape[1] // 2, 30), font_scale=1, color=(0, 255, 255))

    # Cek jika ada wajah yang terdeteksi
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        face_center = x + w // 2
        frame_width = frame.shape[1]

        # Tentukan arah wajah
        if face_center < frame_width // 3:
            direction = "Kiri"
        elif face_center > frame_width * 2 // 3:
            direction = "Kanan"
        else:
            direction = "Tengah"

        show_text(frame, f"Posisi: {direction}", (frame.shape[1] // 2, frame.shape[0] - 50), font_scale=1, color=(255, 0, 0))

        if direction in ["Kiri", "Kanan"]:
            if direction == current_answer:
                score += 1
                pause_with_message(frame, "Benar! kembali ke tengah.", 2)
            else:
                pause_with_message(frame, "Salah! kembali ke tengah.", 2)
            current_pair = None  # Hapus pasangan aktif

    # Hitung waktu tersisa
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - int(elapsed_time))
    show_text(frame, f"Waktu: {remaining_time}s", (frame.shape[1] - 100, 30), font_scale=1, color=(255, 255, 255))

    # Tampilkan skor
    show_text(frame, f"Skor: {score}", (100, 30), font_scale=1, color=(255, 255, 255))

    # Tampilkan hasil frame
    cv2.imshow("Tebak Logo", frame)

    # Akhiri jika waktu habis
    if remaining_time == 0:
        pause_with_message(frame, f"Skor Akhir Kamu: {score}", 5)
        break

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()

print(f"Skor Akhir Kamu: {score}")