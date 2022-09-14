# README Tugas 2 Arief Braja

![urls py](https://user-images.githubusercontent.com/112464917/190202188-1e2d7f68-ee18-4ea8-9a9e-22bf34167ac6.png)

Jelaskan kenapa menggunakan virtual environment? 
Secara singkat, virtual environment menyediakan kita sebuah environment independen dari sistem operasi host. Dengan demikian, kita dapat menginstal dan menggunakan software yang diperlukan di folder /bin virtualenv daripada menggunakan software yang diinstal di host.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Iya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Walaupun begitu, penggunaan virtual environment merupakan best practice karena menghilangkan dependencies conflicts. Contohnya saat kita ingin menginstal versi terbaru dari Django. Jika kita diberikan suatu projek django dengan versi yang lebih lama, kita harus terlebih dahulu menginstal versi django lama tersebut.

Cara mengimplementasikan poin 1 sampai dengan 4.M
1. Mengambil semua objek atau data yang ada di models
2. Cocokan semua data pada models dengan html
3. Memanggil fungsi yang dibuat di dalam urls.py dengan menggunakan fungsi path
4. Menjalankan perintah python manage.py makemigrations, python manage.py migrate, dan python manage.py loaddata initial_wishlist_data.json
5. Melakukan deploy di heroku dengan membuat sebuah project baru (Tugas2ariefbraja)
6. Mengambil API Key dan API Name, kemudian memasukkan keduanya di Github
7. Save dan lakukan Re-run

LINK HEROKU
https://tugas2ariefbraja.herokuapp.com/katalog/
