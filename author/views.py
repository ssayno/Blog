from django.shortcuts import render
from .models import Author
# Create your views here.


def author_registor(request):
    if request.method == "GET":
        return render(request, 'register.html', {})
    elif request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        realname = request.POST.get('realname')
        nickname = request.POST.get('nickname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')
        # print(status)
        author = Author.objects.filter(username=username)
        if len(author) > 0:
            return render(request, 'register.html', {
                'msg_code': 0,
                'msg_info': "帐号已经存在"
            })
        author = Author(username=username, password=password, realname=realname,
                        nickname=nickname, gender=sex, age=age, email=email, phone=phone,
                        status=status)
        author.save()
        return render(request, 'login.html', {
            'msg_code': 0,
            'msg_info': "帐号注册成功",
            'msg_account': username,
            'msg_title': "确认输入账户密码"
        })


def author_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {
            'msg_title': "请输入账户和密码"
        })
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            author = Author.objects.get(username=username, password=password)
            print(type(author))
            request.session['author'] = author
            return render(request, 'index.html', {
                'msg_code': 0,
                'msg_info': "登陆成功",
            })
        except:
            return render(request, 'login.html', {
                'msg_code': -1,
                'msg_info': "帐号或者密码出现问题，请重新登陆"
            })


def main(request):
    return render(request, 'main.html')