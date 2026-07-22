# Praktikum Pengolahan Citra: Ekstraksi dan Pencocokan Fitur

### PraktikumCitra_12 

Repositori ini berisi kumpulan skrip Python untuk memvisualisasikan fitur yang diekstraksi dari sebuah citra dan melakukan pencocokan fitur antar citra menggunakan library OpenCV dan scikit-image.

## Daftar Tugas

### 1. Visualisasi Fitur yang Diekstraksi
Berfokus pada representasi visual fitur dari gambar untuk memahami sifat gambar dan kemanjuran teknik ekstraksi. Terdiri dari 3 teknik:
*   **Deteksi Tepi (Canny Edge):** Memvisualisasikan batas dan bentuk objek dengan melapisi peta tepi pada gambar asli.
*   **Tekstur (Local Binary Pattern / LBP):** Memvisualisasikan pola tekstur yang direkam dalam gambar (digunakan pada gambar pola kain batik).
*   **Titik Kunci (SIFT):** Memvisualisasikan lokasi utama (keypoints) pada gambar menggunakan algoritma SIFT (digunakan pada gambar becak).

### 2. Pencocokan Fitur (Feature Matching) dengan ORB
Menerapkan algoritma ORB (Oriented FAST and Rotated BRIEF) untuk menemukan dan membandingkan titik serupa antar dua gambar (Motor Hijau vs Motor Hitam). 
Algoritma ini dipilih karena cepat, efisien, rotasi invarian (kebal terhadap rotasi gambar), dan merupakan alternatif bebas lisensi dari SIFT/SURF.

## Persyaratan (Dependencies)
Pastikan Anda telah menginstal library berikut sebelum menjalankan skrip:
```bash
pip install opencv-python matplotlib numpy scikit-image

```
***Cara Menjalankan Clone repositori ini***

Pastikan file gambar (becak.jpeg, batik.jpg, motor hijau.jpg, motor hitam.jpg) berada di dalam direktori yang sama dengan skrip.

Jalankan masing-masing skrip Python melalui terminal VS Code.

### Hasil Praktek 

Hasil Pencocokan 

***Hasil Fitur ORB***
![foto](https://github.com/apriliaputri2005-ops/praktikum12_citra/blob/9dcbf6672eeac96a0a788ad9f5269aa467c0bb29/praktikum_12/motor%20hijau%20vs%20motor%20hitam.png)

***Hasil Sift***
![foto](https://github.com/apriliaputri2005-ops/praktikum12_citra/blob/9dcbf6672eeac96a0a788ad9f5269aa467c0bb29/praktikum_12/sensor%20becak.png)

***Canny Edge Detection***
![foto](https://github.com/apriliaputri2005-ops/praktikum12_citra/blob/9dcbf6672eeac96a0a788ad9f5269aa467c0bb29/praktikum_12/Hasil%20Photo%20batik.png)

***Canny Edges Detection***
![foto](https://github.com/apriliaputri2005-ops/praktikum12_citra/blob/9dcbf6672eeac96a0a788ad9f5269aa467c0bb29/praktikum_12/becak.png)

***LBP texture***
![foto](https://github.com/apriliaputri2005-ops/praktikum12_citra/blob/e58ff7aea286a71a7ad1e4ebff4c99d33b36e141/praktikum_12/LBP%20teksture.png)
