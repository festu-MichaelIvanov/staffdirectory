from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StaffWorker

@login_required(login_url='/authpage/')

def index(request):

    worker_list = StaffWorker.objects.all()[:5]
    context = {'worker_list':worker_list, 'username':request.user.username}
    return render(request, 'index.html', context)


