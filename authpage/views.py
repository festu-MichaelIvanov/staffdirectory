from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth

def index(request):

    if request.user.is_authenticated():

       context = {'username':request.user.username}

       return render(request,'authenticated.html', context)

    else:

       return render(request,'login.html')

def login(request):

    args = {}
    args.update(csrf(request))

    if request.POST:

        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('/mainpage/')

        else:

            args['login_error'] = "Пользователь не найден"
            redirect('/mainpage/authpage')
            return render(request,'login.html', args)

    else:

        return render(request,'login.html')

def logout(requset):

    auth.logout(requset)
    return redirect('/mainpage/')


