# TP1DPBO2024C1

# Saya Raffi Ardhi Naufal NIM 2202495 mengerjakan TP 1 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

Dalam tugas praktikum kali ini, saya memiliki desain seperti ini :

![image](https://github.com/RaffiArdhiN/TP1DPBO2024C1/assets/110318306/8a664fb0-4cdf-4aa3-ab5f-f66813c1b857)

Penjelasan tiap kelas :
-	Pemain merupakan nama si pemain dan karakter yang ia mainkan
-	Karakter merupakan kelas orang tua untuk karakter player, npc dan musuh
-	KarakterPlayer merupakan karakter si pemain, berisi status hp; atk; senjata; role; dan item. KarakterPlayer juga memiliki method untuk menyerang musuh dan mengerjakan misi
-	KarakterNPC merupakan karakter sampingan yang memiliki data lokasi dan method seperti memberi info lokasi
-	KarakterJahat merupakan musuh karakter player, berisi status hp dan atk. Memiliki method attack dan talk
-	Role merupakan kelas yang berisi jenis role dan skillnya
-	Item merupakan kelas yang berisi nama saja
Untuk pewarisan, kelas Karakter akan menurunkan sifat ke kelas KarakterPlayer (Karakter Pemain); KarakterNPC; dan KarakterJahat 
Lalu untuk komposit, bisa dilihat sebagai berikut :
-	Pemain akan memiliki KarakterPlayer
-	KarakterPlayer akan memiliki Role dan Item

Hasil Eksekusi :
