from django.shortcuts import render
from .models import *
# Create your views here.
def dashboard(request):
    projects = Project.objects.all()
    boxes = Box.objects.all()
    return render(request, 'dashboard.html', context={'projects': projects, 'boxes': boxes})