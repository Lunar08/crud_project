from django.shortcuts import render,HttpResponseRedirect
from .forms import StudenRegistration
from .models import User
# Create your views here.

def addandshow(request):
    if request.method=='POST':
        fm=StudenRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudenRegistration()
    else:
        fm=StudenRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

def updatedata(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudenRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudenRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

def deletedata(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    