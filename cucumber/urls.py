"""cucumber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('profile_view')
    return render(request, 'index.html')

def terms(request):
    return render(request, 'terms.html')
def privacy(request):
    return render(request, 'privacy.html')
def about(request):
    return render(request, 'about.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name='home'),
    path('events/', include('events.urls')),
    path('accounts/', include('accounts.urls')),

    path('legal/terms', terms, name='terms'),
    path('legal/privacy', privacy, name='privacy'),

    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)