

from django.urls import path

from . import views

#Config URL
urlpatterns =[
    path('', views.index, name='home'),
]