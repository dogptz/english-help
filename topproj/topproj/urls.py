"""topproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from tppo import views
from django.conf.urls import  include, url




urlpatterns = [
    path('register/', views.regist),
    path('admin/', admin.site.urls),
    path('', views.avtoriz, name='home'),
    path('theme/', views.first, name='home'),
    path('first.html', views.first),
    path('theme/1/', views.two, {'num': "1"}),
    path('theme/2/', views.two, {'num': "2"}),
    path('theme/3/', views.two, {'num': "3"}),
    re_path(r'^theme/1/test/', views.vote),
]