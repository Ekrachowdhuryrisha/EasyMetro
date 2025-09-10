from django.contrib import admin 
from django.urls import path
from easymetro_app import views


urlpatterns = [
path('admin/', admin.site.urls),
path('register/', views.register, name='register'),
path('login/', views.login, name='login'),
path('logout/', views.logout, name='logout'),
path('', views.home, name='home'),
path('history/', views.history, name='history'),
]