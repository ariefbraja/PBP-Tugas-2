# Tugas 4
# Kegunaan {% csrf_token %} pada elemen <form>. Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} diimplementasikan untuk menghindari malicious attacks yang di mana menghasilkan token di server-side saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, maka permintaan tersebut tidak akan dieksekusi.

# Apakah kita dapat membuat elemen <form> secara manual?
Iya, kita dapat membuat secara manual.

# Cara membuat <form> secara manual
Tiap label di models.py dicetak secara satu per satu. Misalkan title kita buat `<label for="title">Title:</label>` dan atribut lainnya bisa kita gunakan juga type dan name.
  
#  Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Saat user menekan tombol submit, sistem akan membuat request ke views.py untuk disimpan ke database. Setelah itu, akan dibuat form yang akan di jalankan terlebih dahulu is_valid() agar menjadi cleaned_data agar form tersebut bisa di jalankan method save(). Fungsi di views.py yang memakai form akan memanggil redirect untuk menampilkan data yang sudah diinput. Fungsi di views.py akan menjalankan render yang akan menuju ke HTML yang di mana akan memunculkan data-data yang diinput user.

#  Mengimplementasikan checklist
1. Menjalankan `python manage.py startapp todolist`
2. Menambahkan path di urls.py dengan perintah `path('', show_todolist, name='show_todolist')` , di project_django urls.py dengan perintah `path('todolist/', include('todolist.urls')),` dan project_django urls.py di INSTALLED_APPS menambahkan 'todolist'
3. Membuat class di models.py bernama Task yang berisi user, date, title, description, is_finished
4. Menjalakan perintah `python manage.py makemigrations` dan `python manage.py migrate`
5. Membuat fungsi register dengan kode
```py
 def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)
  ```
 6. Membuat register.html yang berisi
```py
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
 ```
 
7. Menambahkan path ke urls.py yaitu `path('register/', register, name='register')`
8. Hampir sama seperti register, selanjutnya membuat fungsi login_user, logout_user, create_task dengan potongan kode
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    form = TodolistForm()

    if request.method == "POST":
        form = TodolistForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user=User.objects.get(username=request.user.username)
            saving.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create-task.html', context)
  ```
  9. Memasukkan path login, logout, create-task ke urls.py dengan kode
  ```py
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),
  path('create-task/', create_task, name='create_task'),
  ```
  10. Membuat HTML login dengan potongan kode
  ```py
  {% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="submit" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
 ```
 11. Membuat create-task.html dengan potongan kode
 ```py
{% extends 'base.html' %}

{% block meta %}
<title>Tambah Task Baru</title>
{% endblock meta %}

{% block content %}  

<div class = "create_task">
    
    <h1>Tambah Task Baru</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>
                <tr>
                    {{ form }}
    
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Tambah Task"/></td>  
                </tr>
            </table>
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
12. Melakukan push dan commit ke Github dan deploy ke Heroku
13. Membuat akun dummy
  
# Tugas 5
# Perbedaan dari Inline, Internal, dan External CSS
 1. Inline CSS : kode diletakkan di dalam tag HTML tertentu.
 2. Internal CSS : kode CSS internal diletakkan di dalam bagian <head> pada halaman.
 3. External CSS : menghubungkan ke file .CSS eksternal. Perubahan apapun yang dibuat pada file CSS akan tampil pada website.
  
# Kelebihan Inline, Internal, dan External CSS
 Kelebihan Inline CSS : 
  - Permintaan HTTP yang lebih kecil
  
 Kelebihan Internal CSS :
  - Perubahan hanya terjadi pada 1 halaman
  - Hanya menggunakan satu file yaitu html
  
 Kelebihan External CSS : 
  - Ukuran file html menjadi lebih kecil
  - File html menjadi lebih rapih
  - File CSS yang sama bisa digunakan di banyak halaman
  
 # Kekurangan Inline, Internal, dan External CSS
 Kekurangan Inline CSS :
  - Harus diterapkan pada setiap elemen
  - File html terlihat kurang rapih
  
 Kekurangan Internal CSS :
  - Perubahan hanya terjadi pada 1 halaman dan bisa menjadi tidak efisien
  
 Kekurangan External CSS :
  - Halaman belum tampil secara lengkap sebelum file CSS selesai dipanggil
 
# Tag HTML5
  1. <a> = Menentukan anchor
  2. <br> = Memasukkan single line break
  3. <button> = Menentukan button
  4. <div> = Menentukan section
  5. <input> = Menentukan input field
  
# Tipe-tipe CSS selector
  1. Type selector : Selector memilih elemen berdasarkan nama tag
  2. Class selector : Selektor memilih elemen berdasarkan nama class yang diberikan
  3. ID selector : hampir sama dengan class selector, tetapi ID bersifat unik dan hanya boleh digunakan oleh satu elemen saja
  4. Attribute selector : selector yang memilih elemen berdasarkan atribut
  5. Universal selector : menyeleksi semua elemen pada jangkauan tertentu
  
# Cara mengimplementasikan checklist.
  1. Membuat navigation bar dengan bootstrap
  2. Mengubah style pada setiap tag yang diperlukan
  3. Memasukkan kode ke file css 
  4. Mengubah table menjadi cards pada todolist.html
  

# Link Heroku
`https://tugas2ariefbraja.herokuapp.com/todolist/login/`
`https://tugas2ariefbraja.herokuapp.com/todolist/`
`https://tugas2ariefbraja.herokuapp.com/todolist/register/`
`https://tugas2ariefbraja.herokuapp.com/todolist/create-task/`

  
  
