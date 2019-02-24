from django.shortcuts import render,redirect
from . import  models
from shopping.forms import AddForm
from login.models import User
import login.views
import os
import time
# Create your views here.


def add(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！

        if request.method == "POST":
            add_form = AddForm(request.POST)
            message = "It cannot be empty!"
            if add_form.is_valid():  # 获取数据
                name = add_form.cleaned_data['name']
                price = add_form.cleaned_data['price']

                userName = request.session.get("user_name",False)
                user = User.objects.get(name = userName)
                introduction = add_form.cleaned_data['introduction']

                kind = add_form.cleaned_data['kind']
                myFile = request.FILES.get("myfile", None)

                if myFile:
                    da = time.strftime("%y_%m_%d_%H_%M_%S-")
                    path = os.path.join("upload", da+myFile.name)
                    destination = open(path, 'wb+')  # 打开特定的文件进行二进制的写操作
                    for chunk in myFile.chunks():  # 分块写入文件
                        destination.write(chunk)
                    destination.close()

                    new_goods = models.Goods.objects.create()
                    new_goods.name = name
                    new_goods.price = price
                    new_goods.userName = user
                    new_goods.introduction = introduction
                    new_goods.imagePath = path
                    new_goods.kind = kind
    
                    new_goods.save()
                    return redirect('/index/')
        add_form = AddForm()
        return render(request, 'shopping/add.html', locals())
    else:
        return redirect("/index/")


def modify (request):
    pass
    return render(request,'shopping/modify.html')