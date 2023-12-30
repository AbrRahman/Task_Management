from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel
def add_task(request):
    if request.method=='POST':
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form=TaskForm()
    return render(request,"add_task_form.html",{'form':task_form})

def show_task(request):
    data=TaskModel.objects.all()
    return render(request,"show_task.html",{"data":data})

def edit_task(request,id):
    data=TaskModel.objects.get(pk=id)
    task_form=TaskForm(instance=data)
    if request.method=='POST':
        task_form=TaskForm(request.POST,instance=data)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request,"add_task_form.html",{'form':task_form})
def delete_task(request,id):
    data=TaskModel.objects.get(pk=id)
    data.delete()
    return redirect('show_task')