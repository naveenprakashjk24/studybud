from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('room/<str:pk>', views.room, name='room' ),
    path('create-room/', views.createroom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    path('user-profile/<str:pk>', views.userProfile, name='user-profile'),
    path('update-message/', views.updateUser, name='update-user'),
    path('topics-list/', views.topicsPage, name='topics-list'),

]