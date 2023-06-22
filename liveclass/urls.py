from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('create_room/',views.create_room,name='create_room'),
    path('join_room/',views.join_room,name='join_room'),
    path('room/',views.room,name='room'),
    path('stud_record/',views.Stud_record,name='stud_record'),

]