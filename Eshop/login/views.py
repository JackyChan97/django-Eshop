from django.shortcuts import render,redirect

from login.models import User # 要不然下面不行
# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "It can not be empty"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = User.objects.get(name=username)

                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "password is wrong"
            except:
                message = "User is not exist"
        return render(request, 'login/login.html',{"message":message})
    return render(request, 'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return redirect('/index/')