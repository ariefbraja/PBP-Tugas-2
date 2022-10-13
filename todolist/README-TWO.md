# Perbedaan antara asynchronous programming dengan synchronous programming
Synchronus :  
- Menggunakan metode full page refresh
- akan memblokir klien sampai operasi yang dijalankan selesai
- model pada browser sangat tidak responsif

Asynchronus : 
- tidak perlu adanya refresh lagi dari user
- halaman website secara langsung akan diupdate secara langsung tanpa refresh full page

# Event-Driven Programming
Event-driven programming adalah sebuah paradigma yang di mana entitas berkomunikasi secara indirectly dengan mengirimkan pesan dari satu ke yang lainnya menggunakan intermediary.

# Penerapan Asynchronous Programming

# Implementasi Checklist
1. Membuat file todolist-ajax.html
2. Memasukkan kode modal ke dalam todolist-ajax.html
```html
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Add Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="formtask">
          {% csrf_token %}
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="field_title" name="title">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Description:</label>
            <textarea class="form-control" id="field_desc" name="description"></textarea>
          </div>
        </form>
      </div>
        <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Confirm</button>
      </div>
    </div>
  </div>
</div>
```

3. Memasukkan script dan async function ke dalam todolist-ajax.html seperti solusi lab 5
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script>
  async function getTodolist(){
    return fetch("{% url 'todolist:show_json' %}").then((res) => res.json())
  }

  async function refreshTodolist(){
    document.getElementById("ajax-cards").innerHTML = ""
    const todolist = await getTodolist()
    let htmlString = ``
    todolist.forEach(item=> {
      htmlString+=`\n
      <div class = "cards" >
        <p>
        <span class="nowrap"><b>Date : </b></span>
        <span class="nowrap">${item.fields.date}</span>
        </p>
        <p>
        <span class="nowrap"><b>Title : </b></span>
        <span class="nowrap">${item.fields.title}</span>
        </p>
        <p>
        <span class="nowrap"><b>Description : </b></span>
        <span class="nowrap">${item.fields.description}</span>
        </p>
        <p>
        <span class="nowrap"><b>Status : </b></span>
        <span class="nowrap">
        ${item.fields.is_finished ?  "Selesai" : "Belum Selesai"}
        <span>
        </p>

        <div class = "buttonwrapper">
        <form method="POST" action="{% url 'todolist:change_status' %}">
          {% csrf_token %}
          <input type="hidden" name="id" value="${item.fields.id}"/>
          <td><button type="submit" class="btn btn-warning" >Change Status</button></td>
        </form>
        <form method="POST" action="{% url 'todolist:delete_task' %}">
          {% csrf_token %}
          <input type="hidden" name="id" value="${item.fields.id}"/>
          <td><button type="submit" class="btn btn-danger" >Delete</button></td>
        </form>
        </div>

      </div>
      `
    });
    document.getElementById("ajax-cards").innerHTML = htmlString
  }
  
  async function addTask() {
    fetch("{% url 'todolist:add_task_ajax' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#formtask'))
      }).then(refreshTodolist)
    return false
  }

  document.getElementById("addtaskbutton").onclick = addTask

  refreshTodolist()

</script>
```

4. Dalam views.py membuat fungsi show_json
```py
def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist))
```
5. Dalam views.py membuat fungsi add_task_ajax
```py
def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todolist = Task(title=title, description=description, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

6. Dalam views.py membuat fungsi views_ajax
```py
def views_ajax(request):
    return render(request, "todolist-ajax.html")
```

7. Dalam urls.py menambahkan path 
```py
    path('json/', show_json, name='show_json'),
    path('ajax/', views_ajax, name='views_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax'),
```
