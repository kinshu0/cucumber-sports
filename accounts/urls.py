from django.urls import path, re_path
from . import views
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home', permanent=True)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<str:activation_key>/', views.activate_account),
    
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/', views.profile, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile')

]