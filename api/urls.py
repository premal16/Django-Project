from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', RegisterUSer.as_view()),
    # path('login/', Login.as_view(), name='login'),
    # path('profile/', UserProfileCreationAPIView.as_view()),
    # path('user/profile/<int:pk>/', UserProfileRetrieveAPIView.as_view()),
    path('',views.homePage, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register_and_login, name='register'),
    path('profile/', views.profilePage, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name = 'edit_profile')

]
