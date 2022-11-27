from django.contrib import admin
from django.urls import path
from miniblog import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.loginuser,name='login'),
   path('logout/',views.logoutuser,name='logout'),
   path('addpost/',views.addpost,name='addpost'),
   path('updatepost/<int:id>',views.updatepost,name='updatepost'),
   path('deletepost/<int:id>',views.deletepost,name='deletepost'),
]
