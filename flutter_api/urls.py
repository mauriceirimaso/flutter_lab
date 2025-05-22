from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('adduser/', views.add_user, name='add_user'),
    path('getusers/', views.get_users, name='get_users'),
    path('updateuser/', views.update_user, name='update_user'),
    path('deleteuser/', views.delete_user, name='delete_user'),
    path('getuser/', views.get_user_by_id ,name='getuser'),
]