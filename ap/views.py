from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import appointments,departments,doctable,logintb
from django.contrib.sessions.models import Session

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
    import random
    s=0
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
        else:
            obj.save()
        
        deplist=departments.objects.values_list('depname').all()
        for i in deplist:
           data=appointments.objects.filter(departments=i[0])
           
           if len(data)>20:
             context['key']='todays appointment is full'
                  
             return render(request,'submit.html',context)

           else:
              s=random.randrange(1,21,1)
              context['key']=s
                   
              return render(request,'submit.html',context)

              
            
              
           

# admin

def admin(request):
    if request.POST:
     dic={}
     username=request.POST.get('username')
     password=request.POST.get('password')
     data=logintb.objects.get(username=username,password=password)
     if data.utype=='admin':
         request.session['admin']=data.username
         return render(request,'administrator/index.html')
         

    return render(request,'guest/login.html')

def adminedit(request):
    if request.session['admin']:
       return render(request,'administrator/adminedit.html')

def appointmentapprovals(request):
    if request.session['admin']:
     data=appointments.objects.all()
     return render(request,'administrator/appointmentapprovals.html',{'k':data})

def doctorlist(request):
    if request.session['admin']:
     data=doctable.objects.all()
     return render(request,'administrator/doctorlist.html',{'k':data})

def adddoctor(request):
    if request.session['admin']:
   
     data=departments.objects.all()
     return render(request,'administrator/adddoctor.html',{'k':data})

def adddepartments(request):
    if request.session['admin']:
      deplist=departments.objects.values_list('depname').all()
      for i in deplist:
         data=doctable.objects.filter(departments=i[0])
         count=len(data)
    
         departments.objects.filter(depname=i[0]).update(ndoctors=count)
        

    data=departments.objects.all()
    return render(request,'administrator/adddepartments.html',{'k':data})

def plus(request):
    if request.POST:
        dep=departments()
        dep.depname=request.POST.get('depname')
        dep.ndoctors=0
        dep.save()
    return HttpResponseRedirect('adddepartments') 

def plusdoctor(request):
    if request.POST:
        docobj=doctable()
        docobj.name=request.POST.get('name')
        docobj.age=request.POST.get('age')
        docobj.departments=request.POST.get('departments')
        docobj.save()
        return HttpResponseRedirect('adddoctor')
    
def logout(request):
   if request.session['admin']:
      Session.objects.all().delete()
      return HttpResponseRedirect('adminIndex')
   
       
        
        
          
        

        


            



