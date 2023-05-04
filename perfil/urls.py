

from django.urls import path

from . import views

#Config URL
urlpatterns =[
    path('', views.profile, name='profile'),
]