from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^activate/account/$', views.activate_account, name='activate'),
    # path('login', views.login_view, name='login'),
    # path('register', views.register, name='register')

]