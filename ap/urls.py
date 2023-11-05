from django.urls import path
from ap import views

urlpatterns=[
    path('',views.home),
    path('about',views.about),
    path('appointment',views.appointment),
    path('blog',views.blog),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('service',views.service),
    path('singleblog',views.singleblog),
    path('team',views.team),
    path('validation',views.validation),
    path('adminIndex',views.admin),
    path('adminedit',views.adminedit),
    path('appointmentapprovals',views.appointmentapprovals),
    path('doctorlist',views.doctorlist),
    path('adddoctor',views.adddoctor),
    path('adddepartments',views.adddepartments),
    path('plus',views.plus),
    path('adddoc',views.plusdoctor),
    path('logout',views.logout)

]