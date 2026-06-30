from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        task = Task(
            title=request.POST['title'],
            due_at=make_aware(parse_datetime(request.POST['due_at']))
        )
        task.save()

    # クエリパラメータを判定して並び替える
    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')          # 締切の早い順
    else:
        tasks = Task.objects.order_by('-posted_at')      # 登録の最新順

    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)