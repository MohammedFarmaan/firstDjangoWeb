from django.urls import path
from . import views

urlpatterns = [
    path('', views.Print, name='Print'),
    path('user', views.GetUser, name='GetUser')
]
