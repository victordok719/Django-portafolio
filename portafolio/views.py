from django.shortcuts import render
from .models import Project
# Create your views here.
def font(request):
    projects = Project.objects.all()

    return render(request, "font.html", {'projects':projects})
