from todolist.models import relation
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .modelMan import check_user, delete_task,add_task ,save_user,list_of_tasks ,for_checkbox
# Create your views here.

def loginx(request):  # login done 
    if(request.method == 'GET'):
        return render(request, 'todolist/login.html' ,{
                'incorrect_password' : False
            })
    elif(request.method == 'POST'):
        user = request.POST['username']
        pas = request.POST['password']
        user = authenticate(request, username=user, password=pas)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'todolist/index.html')
        else:
            return render(request, 'todolist/login.html' ,{
                'incorrect_password' : True
            })
def signup(request): #done 
    if request.method == 'GET':
        return render(request, 'todolist/signup.html', 
            {'invaliad_username' :False
            })
    elif request.method == 'POST':
        if check_user(request.POST['username']):
            user = User.objects.create_user( request.POST['username'],request.POST['email'], request.POST['password'])
            user.save()
            save_user(request.POST['username'],request.POST['date_of_birth'] ,request.POST['first_name'] 
            ,request.POST['last_name'],request.POST['email'])
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'todolist/index.html')
            return render(request, 'todolist/login.html')
        else :
            return render(request, 'todolist/signup.html', 
            {'invaliad_username' :True
            })

@login_required
def index(request): #not done ---->>
    x = list_of_tasks(request.user.username)
    is_empty = False
    if len(x) == 0:
        is_empty = True
    return render(request, 'todolist/index.html', {
        'data' : x,
        'is_empty' : is_empty
    })

@login_required
def add(request): #notdone
    if request.method == 'GET':
        return render(request, "todolist/add.html")
    elif request.method == 'POST':
        add_task(request.user.username ,request.POST['task'] ,request.POST['time'])
        return render(request, "todolist/add.html")




@login_required
def remove(request):  #done for get not for post ---->>
    x = list_of_tasks(request.user.username)
    list_len = len(x)
    is_empty = False
    if list_len == 0:
        is_empty = True
    list_name = for_checkbox(list_len)
    z_list = zip(x,list_name)
    if request.method == 'GET':
        return render(request, 'todolist/remove.html', {
        'data' : z_list,
        'is_empty':is_empty
    })
    if request.method == 'POST':
        for x ,y  in z_list:
            if request.POST.get(y) != None:
                delete_task(request.user.username , x['task_name'])
        return redirect('/todolist/home')


        # delete_task(request.user.get_username() ,task_name) 







def about(request):
    return render(request, "todolist/about.html")
@login_required
def logoutx(request):  # logout done
    logout(request)
    return render(request, "todolist/login.html")

    
