from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
from todo.models import Todolist
from django.shortcuts import HttpResponseRedirect, get_object_or_404


def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')    # 获取表单input内容中name为‘action’的那一条,获取其value
        if action == 'add':
            content = request.POST.get('content')
            Todolist.objects.create(content = content)
            # 如果获取到的表单

    todo_list = Todolist.objects.all()

    return render(request, 'index.html', locals())

def complete(request, pk):
    todo_item = get_object_or_404(Todolist, id=pk)
    todo_item.is_completed = True
    todo_item.save()
    return HttpResponseRedirect('/')

def delete(request, pk):
    todo_item = get_object_or_404(Todolist, id=pk)
    todo_item.delete()
    return HttpResponseRedirect('/')








