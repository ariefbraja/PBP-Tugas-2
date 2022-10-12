getTodolist()
addTodolist()


function getTodolist(){
    $.ajax({
        type : "GET",
        url : "/todolist/json/",

        success: function(json){
            console.log(json)
            $('#output').empty()
            var data = ""
            JSON.parse(json).forEach(x => {
                data += `
                  <div class = "cards" >
                    <p>
                    <span class="nowrap"><b>Date : </b></span>
                    <span class="nowrap">${x.fields.date}</span>
                    </p>
                    <p>
                    <span class="nowrap"><b>Title : </b></span>
                    <span class="nowrap">${x.fields.title}</span>
                    </p>
                    <p>
                    <span class="nowrap"><b>Description : </b></span>
                    <span class="nowrap">${x.fields.description}</span>
                    </p>
                    <p>
                    <span class="nowrap">
                    ${x.fields.is_finished ?  "Selesai" : "Belum Selesai"}
                    <span>
                    </p>
            
                    <div class = "buttonwrapper">
                    <form method="POST" action="{% url 'todolist:change_status' %}">
                      {% csrf_token %}
                      <input type="hidden" name="id" value="${x.fields.id}"/>
                      <td><button type="submit" class="btn btn-warning" >Change Status</button></td>
                    </form>
                    <form method="POST" action="{% url 'todolist:delete_task' %}">
                      {% csrf_token %}
                      <input type="hidden" name="id" value="${x.fields.id}"/>
                      <td><button type="submit" class="btn btn-danger" >Delete</button></td>
                    </form>
                    </div>
            
                  </div>`
            });
            $("#output").append(data)
            
        }
    })
}

function addTodolist() {
    fetch("{% url 'create_task' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#form'))
      }).then(getTodolist)
    return false
  }

