from django.shortcuts import render, redirect
from mainpage.models import StaffWorker
from django.template.context_processors import csrf

def searchingpage(request):

    if request.user.is_authenticated():

        context = {'username': request.user.username }

        return render(request,'searching_form.html', context)

    else:

        return redirect('/authpage/')


def search(request):

    if request.user.is_authenticated():

        args = {}
        args.update(csrf(request))

        WorkerName = request.POST.get('worker_name','')
        WorkerSecondName = request.POST.get('worker_secondname','')
        WorkerEmail = request.POST.get('worker_email','')
        WorkerMobile = request.POST.get('worker_mobile','')
        WorkerPost = request.POST.get('worker_post','')

        worker_list = {}
        kwargs = {}

        if WorkerName != '':

           kwargs['WorkerName__icontains'] = WorkerName

        if WorkerSecondName != '':

           kwargs['WorkerSecondName__icontains'] = WorkerSecondName

        if WorkerEmail != '':

           kwargs['WorkerEmail__icontains'] = WorkerEmail

        if WorkerMobile != '':

           kwargs['WorkerMobile__icontains'] = WorkerMobile

        if WorkerPost != '':

           kwargs['WorkerPost__icontains'] = WorkerPost

        worker_list = StaffWorker.objects.filter(**kwargs)

        context = {'worker_list':worker_list, 'username': request.user.username }

        return render(request, 'result.html', context)

    else:

        return redirect('/authpage/')
