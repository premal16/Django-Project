from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register_and_login, name='register'),
    path('profile/', views.profilePage, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
     path('change-password/', views.change_password, name='change_password')
]
