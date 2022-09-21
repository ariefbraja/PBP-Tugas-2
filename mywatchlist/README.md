# Perbedaan JSON, XML, dan HTML
1. JSON : self-describing, lebih simple
2. XML : self-descriptive, dirancang untuk membawa data, bukan untuk menampilkan data
3. HTML : digunakan untuk menampilkan suatu hal dalam halaman World Wide Web

# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery merupakan elemen yang penting dalam penukaran data yang di mana data tersebut akan diolah dan diproses. Nantinya, user akan memerlukan data-data tersebut. HTML, XML, dan JSON diperlukan dalam sebuah platform agar user dapat membaca dan menerima data-data yang sudah tersedia.

# Langkah-Langkah Implementasi Checklist
1. Menambahkan aplikasi mywatchlist pada repo lab 2 
2. Menambahkan path mywatchlist 
3. Menambahkan 'mywatchlist' pada settings.py di project_django
4. Membuat model MyWatchList dengan atribut watched, title, rating, release date, review
5. Menjalankan python manage.py makemigrations dan python manage.py migrate
6. Membuat folder fixtures di dalam folder mywatchlist yang berisi file initial_mywatchlist_data.json yang berisikan film-film yang ingin dimasukkan 
7. Menjalankan python manage.py loaddata initial_mywatchlist_data.json
8. Membuat file mywatchlist.html pada folder templates di dalam folder mywatchlist
9. Membuat fungsi show_mywatchlist, show_json, dan show_xml
10. Import fungsi-fungsi tersebut pada urls_py
11. Membuat file urls.py di mywatchlist dan menambahkan path('html/', show_mywatchlist, name='show_mywatchlist'), path('xml/', show_xml, name='show_xml'), dan path('json/', show_json, name='show_json') ke dalam urlpatterns
12. Menambahkan path('mywatchlist/', include('mywatchlist.urls')) ke dalam urls.py di project_django
13. Melakukan Deployment ke Heroku dengan menambahkan kode release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json pada Procfile

# Link Akses
1. https://tugas2ariefbraja.herokuapp.com/mywatchlist/html/
2. https://tugas2ariefbraja.herokuapp.com/mywatchlist/json/
3. https://tugas2ariefbraja.herokuapp.com/mywatchlist/xml/

# Mengakses URL dengan Postman

![html tugas 3](https://user-images.githubusercontent.com/112464917/191564686-c8e979c7-6d37-4a97-958c-92ea5137b965.png)

![json tugas 3](https://user-images.githubusercontent.com/112464917/191564741-a629b093-0a21-4428-b5e7-1a0b9ffe2523.png)

![xml tugas 3](https://user-images.githubusercontent.com/112464917/191564769-c77620e9-5888-427f-9d1d-51d6b09065fc.png)

# Menambahkan Unit test pada tests.py
Menambahkan class ContohAppTest(TestCase) yang berisikan kode:

    def test_mywatchlist_html(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_json(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml(self):
        response = Client().get('https://tugas2ariefbraja.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

# Bonus
Menambahkan kode 

    countWatched = 0
    for film in data_film_mywatchlist:
        if(film.watched == "Yes"):
            countWatched+= 1
    if(countWatched > 10 - countWatched):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
        
pada views.py yang nantinya message akan ditampilkan pada paling bawah web
