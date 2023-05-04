


from django.shortcuts import render, HttpResponse

from .models import Project


def profile(request):
  
    projects = Project.objects.all()

    print(projects) 
    
    return render(request, 'profile.html', {'projects':projects})

# {'projects':projects} : es un diccionario que tiene como clave projects