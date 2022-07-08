from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from rest_framework import generics
from .serializers import DSProject, DSProjectSerializer
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def dashboard(request):
    return render(request, 'index.html')



""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""

class DSProjectList(generics.ListCreateAPIView):
    queryset = DSProject.objects.all()
    serializer_class = DSProjectSerializer

