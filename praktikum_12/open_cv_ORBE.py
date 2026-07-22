# Langkah 1: Mengimpor Library
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Langkah 2: Memuat Gambar Utama (Menggunakan nama file fotomu)
query_img = cv2.imread('motor hijau.jpg')
train_img = cv2.imread('motor hitam.jpg')

# Validasi untuk memastikan foto terbaca oleh VS Code
if query_img is None or train_img is None:
    print("Error: Foto tidak ditemukan! Pastikan file 'motor hijau.jpg' dan 'motor hitam.jpg' sudah dipindahkan ke folder praktikum_12.")
    exit()

# Langkah 3: Mengonversi ke Skala Abu-abu (Grayscale)
query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

# Langkah 4: Mendeteksi Titik Kunci dan Menemukan Deskriptor menggunakan ORB
orb = cv2.ORB_create()
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)

# Langkah 5: Mencocokkan Deskriptor menggunakan Brute-Force Matcher
matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors, trainDescriptors)

# Mengurutkan hasil kecocokan berdasarkan jarak fitur terbaik
matches = sorted(matches, key=lambda x: x.distance)

# Langkah 6: Memvisualisasikan Kecocokan (Maksimal 20 garis kecocokan)
final_img = cv2.drawMatches(query_img, queryKeypoints, 
                            train_img, trainKeypoints, 
                            matches[:20], None)

# Mengubah ukuran gambar keluaran agar pas di layar monitor
final_img = cv2.resize(final_img, (1000, 650))

# Menampilkan hasil visualisasi menggunakan Matplotlib
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
plt.title("Feature Matches - Motor Hijau vs Motor Hitam")
plt.axis('off')
plt.show()