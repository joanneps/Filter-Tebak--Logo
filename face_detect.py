import cv2
import dlib

# Inisialisasi detektor wajah
detector = dlib.get_frontal_face_detector()

# Fungsi untuk menampilkan teks di layar
def show_text(frame, text, position, font_scale=1, color=(0, 255, 0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    cv2.putText(frame, text, position, font, font_scale, color, thickness)

# Fungsi untuk menambahkan gambar ke frame
def overlay_image(frame, image, position):
    x, y = position
    h, w, _ = image.shape
    frame[y:y+h, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 0.5, image, 0.5, 0)

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat mengakses kamera.")
    exit()

# Load gambar
img_benar = cv2.imread("data/benar.jpg")
img_salah = cv2.imread("data/salah.jpg")

# Resize gambar agar sesuai dengan layar
img_benar = cv2.resize(img_benar, (150, 150))
img_salah = cv2.resize(img_salah, (150, 150))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat membaca frame.")
        break
    
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
        
        # Tampilkan teks di layar
        show_text(frame, f"Arah: {direction}", (50, 50), font_scale=1, color=(255, 0, 0))
    
    # Tampilkan hasil frame dengan tulisan
    cv2.imshow("Deteksi Arah Wajah", frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()
