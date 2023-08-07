from django.urls import path
from api.views import RegisterUSer,Login,UserProfileCreationAPIView,UserProfileRetrieveAPIView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUSer.as_view()),
    path('login/', Login.as_view()),
    path('profile/', UserProfileCreationAPIView.as_view()),
    path('user/profile/<int:pk>/', UserProfileRetrieveAPIView.as_view()),

]
