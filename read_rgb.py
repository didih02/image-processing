#kali ini saya akan memberikan cara bagaimana membaca channel warna RGB pada sebuah gambar
#pertama-tama, kita membutuhkan sebuah library dari python yg bernama cv2
import cv2

#setelah itu, kita gunakan fungsi imread yang ada pada cv2 yang bertujuan untuk membaca data gambar. 
#Perlu diketahui, gambar yang sering kita pakai itu terdiri dari kumpulan-kumpulan matriks.
img = cv2.imread('palm.jpg')

#pada ruang warna/channel RGB (Red, Green, Blue) terdiri dari matrik 3 Dimensi. 
#Misalkan (300,350,3) ==> 300 dan 350 adalah ukuran dari gambar yaitu 300 px X 350 px sedangkan angka 3 adalah ruang dimensi RGB
print(img[:, :, 0]) #red
print(img[:, :, 1]) #green
print(img[:, :, 2]) #blue
