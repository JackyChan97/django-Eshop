from django.shortcuts import render,redirect

from login.models import User # 要不然下面不行

from . import  models
from login.forms import UserForm
# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "It cannot be empty!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "Password is wrong!"
            except:
                message = "User is not exist"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return redirect('/index/')