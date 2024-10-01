from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('gallery',views.gallery,name='gallery'),
    path('contactus',views.contactus,name='contactus'),
    path('managedept',views.managedept,name='managedept'),
    path('manageemp',views.manageemp,name='manageemp'),
    path('managereg',views.managereg,name='managereg'),
    path('managelogin',views.managelogin,name='managelogin'),
    path('managelogout',views.managelogout,name='managelogout')

]