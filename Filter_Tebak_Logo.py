import cv2
import dlib

# Inisialisasi detektor wajah
detector = dlib.get_frontal_face_detector()

# Fungsi untuk menampilkan teks di layar
def show_text(frame, text, position, font_scale=1, color=(0, 255, 0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = max(0, min(position[0], frame.shape[1] - text_size[0]))
    text_y = max(text_size[1], min(position[1], frame.shape[0]))
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness)

# Fungsi untuk menambahkan gambar ke frame
def overlay_image(frame, image, position):
    x, y = position
    h, w, _ = image.shape
    if y + h > frame.shape[0] or x + w > frame.shape[1]:
        return  # Jangan menggambar jika posisi keluar dari frame
    frame[y:y+h, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 0.5, image, 0.5, 0)

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat mengakses kamera.")
    exit()

# Load gambar
img_benar = cv2.imread("assets/benar1.jpg")
img_salah = cv2.imread("assets/salah1.jpg")

# Validasi gambar berhasil di-load
if img_benar is None or img_salah is None:
    print("Gambar tidak ditemukan. Periksa kembali path file.")
    exit()

# Resize gambar agar sesuai dengan layar
img_benar = cv2.resize(img_benar, (150, 150))
img_salah = cv2.resize(img_salah, (150, 150))

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

    # Koordinat gambar benar dan salah
    benar_pos = (50, 50)
    salah_pos = (frame.shape[1] - 200, 50)
    
    # Tambahkan gambar ke frame
    overlay_image(frame, img_benar, benar_pos)
    overlay_image(frame, img_salah, salah_pos)
    
    # Cek jika ada wajah yang terdeteksi
    for face in faces:
        # Dapatkan koordinat wajah
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Tentukan posisi tengah wajah (x + w // 2)
        face_center = x + w // 2
        
        # Tentukan lebar frame
        frame_width = frame.shape[1]
        
        # Tentukan apakah wajah mengarah ke kiri atau kanan
        if face_center < frame_width // 3:
            direction = "Kiri"
        elif face_center > frame_width * 2 // 3:
            direction = "Kanan"
        else:
            direction = "Tengah"
        
        # Tampilkan teks di tengah layar
        text_position = (frame_width // 2, frame.shape[0] // 2)
        show_text(frame, f"Arah: {direction}", text_position, font_scale=1.5, color=(255, 0, 0))
    
    # Tampilkan hasil frame dengan tulisan
    cv2.imshow("Deteksi Arah Wajah", frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()
