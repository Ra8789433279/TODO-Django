from django.shortcuts import render, HttpResponse
from home.models import tasks

# Create your views here.

def home(request):
    context = {"success" : False}
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title, desc)
        ins = tasks(tasksTitle=title, tasksDesc=desc)
        ins.save()
        context = {"success" : True}
    return render(request, 'index.html', context)


def tasks_view(request):
    alltasks = tasks.objects.all()
    context = {'tasks' : alltasks} 
    return render(request, 'tasks.html', context )
