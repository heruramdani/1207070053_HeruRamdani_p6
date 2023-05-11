#import library
import numpy as np
import imageio
import cv2
import matplotlib.pyplot as plt
#membaca gambar
img = cv2.imread('Bandung.png')
img_height =img.shape[0]# Mengambil ukuran tinggi gambar dan memasukkannya ke dalam variabel img_height.
img_width = img.shape[1]#Mengambil ukuran lebar gambar dan memasukkannya ke dalam variabel img_width.
img_channel = img.shape[2]#Mengambil jumlah channel gambar dan memasukkannya ke dalam variabel img_channel.

#Merubah gambar menjadi Grayscale
img_grayscale = np.zeros(img.shape, dtype=np.uint8) # membuat array kosong dengan dimensi yang sama seperti gambar dengan tipe data uint8

for y in range(0, img_height): # looping untuk setiap pixel pada sumbu Y dari gambar
    for x in range(0, img_width): # looping untuk setiap pixel pada sumbu X dari gambar
        red = img[y][x][0] # mengambil nilai red (R) pada pixel tertentu
        green = img[y][x][1] # mengambil nilai green (G) pada pixel tertentu
        blue = img[y][x][2] # mengambil nilai blue (B) pada pixel tertentu
        gray = (int(red) + int(green) + int(blue)) / 3 # menghitung nilai grayscale dari pixel tertentu
        img_grayscale[y][x] = (gray, gray, gray) # mengisi array kosong dengan nilai grayscale pada pixel tertentu



plt.imshow(img_grayscale)#Menampilkan hasil pemrosesan gambar dengan menggunakan fungsi "plt.imshow" dari pustaka Matplotlib
plt.title("Grayscale")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".

#Menampilkan Histogram Gambar Grayscale
#Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256))
#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hg[x] = 0
#Menghitung nilai dari gambar
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray] += 1
#menampilkan histogram
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".
#Menampilkan Histogram Gambar RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256))#Membuat empat array dengan ukuran 256 dan 768 elemen berturut-turut, diinisialisasi dengan nilai 0.
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))
#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0#Mengisi setiap nilai dalam array hgr, hgg, hgb dengan 0.

for x in range(0, 768):
    hgrgb[x] = 0# Mengisi setiap nilai dalam array hgrgb dengan 0.
#Menghitung nilai dari gambar
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0#Mengisi setiap nilai dalam array hgr, hgg, hgb dengan 0.

for x in range(0, 768):
    hgrgb[x] = 0#Mengisi setiap nilai dalam array hgrgb dengan 0.

# th = int(256/64)
temp = [0]# Membuat variabel temp dengan list kosong.
for y in range(0, img.shape[0]):#Melakukan iterasi pada setiap piksel dalam gambar,
    for x in range(0, img.shape[1]):
        red = int(img[y][x][0])
        green = int(img[y][x][1])
        blue = int(img[y][x][2])
        green = green + 256#mengambil nilai R, G, B dari setiap piksel, menambahkan 256 pada nilai G
        blue = blue + 512# 512 pada nilai B, dan kemudian menambahkan 1 pada setiap array hgrgb sesuai dengan nilai R, G, dan B tersebut.
        #         temp.append(green)
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1

binsrgb = np.linspace(0, 768, 100)#Membuat 100 elemen array yang berisi 0 hingga 768.
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#Menampilkan histogram dengan menggunakan fungsi plt.hist dengan nilai array hgrgb dan binsrgb sebagai parameter, dengan warna hitam dan opacity sebesar 0.5.
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".
#menampilkan histogram
for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

bins = np.linspace(0, 256, 100)
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Red")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".

plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Green")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".

plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Blue")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".
#Menampilkan Histogram Kumulatif
hgk = np.zeros((256))
c = np.zeros((256))#dengan ukuran 256 dan diisi dengan 0 menggunakan fungsi np.zeros().

for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0#Melakukan perulangan untuk mengisi setiap nilai dalam array hgk dan c dengan 0.

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1#Melakukan perulangan pada setiap piksel gambar untuk menghitung histogram citra grayscale pada array hgk.

c[0] = hgk[0]
for x in range(1, 256):
    c[x] = c[x - 1] + hgk[x]#Menghitung nilai komulatif dari array hgk pada array c.

hmaxk = c[255]#Menghitung nilai maksimum pada array c untuk normalisasi histogram.

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk#Menghitung nilai normalisasi pada setiap elemen array c.

plt.hist(c, bins, color="black", alpha=0.5)#Menampilkan histogram citra menggunakan fungsi plt.hist() dengan variabel bins yang belum didefinisikan.
plt.title("Histogram Grayscale Kumulatif")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".
#Menampilkan histogram hequalisasi
hgh = np.zeros((256))#Menginisialisasi array dengan nilai 0 untuk menyimpan nilai histogram
h = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256):#Looping sebanyak 256 kali untuk menginisialisasi nilai histogram dan komulatif histogram
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height):#Looping sebanyak ukuran lebar dan tinggi gambar untuk menghitung histogram
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1

h[0] = hgh[0]#Menghitung nilai komulatif histogram
for x in range(1, 256):
    h[x] = h[x - 1] + hgh[x]

for x in range(0, 256):#Normalisasi histogram
    h[x] = h[x] / img_height / img_width

for x in range(0, 256):#Mereset nilai histogram lagi untuk menghitung hasil transformasi
    hgh[x] = 0

for y in range(0, img_height):#Looping sebanyak ukuran lebar dan tinggi gambar untuk menghitung nilai transformasi
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0]#Menghitung nilai komulatif histogram hasil transformasi
for x in range(1, 256):
    c[x] = c[x - 1] + hgh[x]

hmaxk = c[255]#Normalisasi kembali hasil transformasi

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")#Kode ini juga menambahkan judul pada masing-masing gambar menggunakan fungsi "plt.title"
plt.show()#menampilkan gambar dengan fungsi "plt.show".