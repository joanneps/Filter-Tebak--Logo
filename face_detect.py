import cv2
import dlib

# Inisialisasi detektor wajah
detector = dlib.get_frontal_face_detector()

# Fungsi untuk menampilkan teks di layar
def show_text(frame, text, position, font_scale=1, color=(0, 255, 0)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    cv2.putText(frame, text, position, font, font_scale, color, thickness)

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat mengakses kamera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat membaca frame.")
        break
    
    # Konversi frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah
    faces = detector(gray)
    
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