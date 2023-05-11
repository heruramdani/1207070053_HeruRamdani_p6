import numpy as np
import imageio
import cv2
import matplotlib.pyplot as plt

#Membaca gambar
img = cv2.imread('Bandung.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Mendapatkan resolusi dan type dari gambar
img_height =img.shape[0]# Mengambil ukuran tinggi gambar dan memasukkannya ke dalam variabel img_height.
img_width = img.shape[1]#Mengambil ukuran lebar gambar dan memasukkannya ke dalam variabel img_width.
img_channel = img.shape[2]#Mengambil jumlah channel gambar dan memasukkannya ke dalam variabel img_channel.

img_type = img.dtype#Mendapatkan tipe data gambar dan disimpan pada variabel "img_type".
#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type)#Membuat dua array nol, yaitu "img_flip_horizontal" dan "img_flip_vertical", dengan ukuran yang sama dengan gambar "img" dan tipe data yang sama seperti "img_type".
img_flip_vertical = np.zeros(img.shape, img_type)# Kedua array nol tersebut akan digunakan untuk menyimpan gambar hasil pemrosesan.
#Membalik gambar secara horizontal
for y in range(0, img_height):#Membalikkan gambar secara horizontal dengan melakukan iterasi pada setiap piksel gambar menggunakan nested loop.
    for x in range(0, img_width):#Proses pemrosesan dilakukan dengan mengambil nilai piksel pada posisi yang berlawanan pada sumbu x.
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]#Hasil pemrosesan disimpan pada array "img_flip_horizontal".
#Membalik gambar secara vertical
for y in range(0, img_height):#Membalikkan gambar secara vertikal dengan melakukan iterasi pada setiap piksel gambar menggunakan nested loop.
    for x in range(0, img_width):#Proses pemrosesan dilakukan dengan mengambil nilai piksel pada posisi yang berlawanan pada sumbu y.
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]#Hasil pemrosesan disimpan pada array "img_flip_vertical".
#Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal)#Menampilkan hasil pemrosesan gambar dengan menggunakan fungsi "plt.imshow" dari pustaka Matplotlib.
plt.title("Flip Horizontal")# Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()# menampilkan gambar dengan fungsi "plt.show".
plt.imshow(img_flip_vertical)#Menampilkan hasil pemrosesan gambar dengan menggunakan fungsi "plt.imshow" dari pustaka Matplotlib.
plt.title("Flip Vertical")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".