from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('activate', views.activate_account, name='activate'),
    path('activate/<slug:activation_key>/', views.activate_account)
    # path('login', views.login_view, name='login'),
    # path('register', views.register, name='register')

]