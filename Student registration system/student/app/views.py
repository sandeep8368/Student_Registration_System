from django.shortcuts import render, redirect
from multiprocessing import context
from .models import Student
from .forms import StudentForm


# Create your views here.
def Home(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        form.save()
        form=StudentForm()

    data=Student.objects.all()


    context={
        'form':form,
        'data':data,
    }
    return render (request,'app/index.html',context)


def Delete_record(request,id):
    a=Student.objects.get(pk=id)
    a.delete()
    return redirect('/')


def Update_record(request,id):
    if request.method=='POST':
        data=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
    
    
        data=Student.objects.get(pk=id)
        form=StudentForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app/update.html',context)