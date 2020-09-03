from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<slug:activation_key>/', views.activate_account),
    
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile_view'),

]