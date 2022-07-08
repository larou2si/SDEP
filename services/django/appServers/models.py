from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        db_table = 'box'

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    url = models.URLField(blank=True, null=False)
    port = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    is_product = models.BooleanField(blank=True, null=True, default=False)
    is_sidbar = models.BooleanField(blank=True, null=True, default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'server'

    def __str__(self):
        return self.name

        """
class Credentiels(models.Model):
    username = models.CharField(max_length=255, blank=True, null=False)
    password = models.CharField(gettext_lazy('password'), max_length=128)
    Server = models.ForeignKey(Server, on_delete=models.CASCADE, blank=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)

    class Meta:
        db_table = 'credentials'
        """