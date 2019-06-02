from django.contrib import admin
from django.urls import path, re_path
from tppo import views
from django.conf.urls import  include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.regist),
    path('', views.avtoriz, name='home'),
    path('theme/', views.first, name='home'),
    path('first.html', views.first),
    path('theme/<int:num>/', views.two),
    path('theme/1/test/', views.vote),
]