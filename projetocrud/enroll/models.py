from django.db import models

# Create your models here.
class Usuario(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False, blank=False)
    nome = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    senha = models.CharField(max_length=80, null=False, blank=False)
    curso = models.CharField(max_length=90, null=False, blank=False)
