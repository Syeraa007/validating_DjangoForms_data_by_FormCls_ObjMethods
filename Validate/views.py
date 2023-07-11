from django.shortcuts import render
from django.http import HttpResponse
from Validate.forms import *
from Validate.models import *
# Create your views here.

def objMethod(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            print(str(SFD.cleaned_data))
            Student.objects.get_or_create(name=SFD.cleaned_data['name'],age=SFD.cleaned_data['age'],loc=SFD.cleaned_data['loc'],email=SFD.cleaned_data['email'],remail=SFD.cleaned_data['remail'],url=SFD.cleaned_data['url'])[0].save()
            return HttpResponse('Data recieved successfully ')
        else:
            return HttpResponse('Invalid data entered')
    return render(request,'objMethod.html',d)

def show_objMethod(request):
    SDA=Student.objects.all()
    d={'SDA':SDA}
    return render(request,'show_objMethod.html',d)

