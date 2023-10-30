from django.shortcuts import render
from django.http import HttpResponse
from . models import appointments

# Create your views here.
# base

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    return render(request,'appointment.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')


def gallery(request):
    return render(request,'gallery.html')


def service(request):
    return render(request,'service.html')


def singleblog(request):
    return render(request,'singleblog.html')

def team(request):
    return render(request,'team.html')

def validation(request):
    if request.POST:
        context={}
        obj=appointments()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.date=request.POST.get('date')
        obj.docter=request.POST.get('docsubject')
        obj.departments=request.POST.get('depsubject')
        obj.message=request.POST.get('formmessage')
        if len(obj.message)==0 or obj.message.isspace():
            context['msg']='empty message'
            return render(request,'submit.html',context)
        obj.save()
        context['msg']='sucessfull'
        return render(request,'submit.html',context)


# admin

def admin(request):
    return render(request,'administrator/index.html')

def adminedit(request):
    return render(request,'administrator/adminedit.html')

def appointmentapprovals(request):
    return render(request,'administrator/appointmentapprovals.html')

def doctorlist(request):
    return render(request,'administrator/doctorlist.html')

def adddoctor(request):
    return render(request,'administrator/adddoctor.html')

def adddepartments(request):
    return render(request,'administrator/adddepartments.html')
        


            



