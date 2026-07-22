import cv2
import matplotlib.pyplot as plt

# Muat gambar (Ganti 'batik.jpg' dengan file gambarmu)
image = cv2.imread('batik.jpg', cv2.IMREAD_GRAYSCALE)

# Terapkan detektor tepi Canny
edges = cv2.Canny(image, 100, 200)

# Tampilkan gambar asli dan tepinya
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Edges')
plt.imshow(edges, cmap='gray')
plt.show()

from skimage import io, feature
import matplotlib.pyplot as plt

# Muat gambar dalam skala abu-abu
image = io.imread('image.jpg', as_gray=True) # Gunakan gambar bertekstur (misal: kain, kayu, atau daun)

# Terapkan Pola Biner Lokal (LBP) dengan parameter P=8 dan R=1
lbp = feature.local_binary_pattern(image, P=8, R=1, method='default')

# Tampilkan visualisasi tekstur LBP
plt.figure(figsize=(10, 5))
plt.title('LBP Texture Features')
plt.imshow(lbp, cmap='gray')
plt.show()