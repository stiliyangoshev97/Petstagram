from django.urls import path

app_name = "accounts"
from accounts import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),


]