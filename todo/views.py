from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . models import Todo



def home(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {"todo_items":todo_items})
    
@csrf_exempt
def add(request):
    current_date =timezone.now()
    content=request.POST["content"]
    
    created_obj=Todo.objects.create(added_date= current_date,text=content)
    print(created_obj.id)
    
    return HttpResponseRedirect(reverse('todo:home'))
    
@csrf_exempt
def delete_item(request, todo_id ):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todo:home'))