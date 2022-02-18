from django.db import models
from uuid import uuid4

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    lido = models.CharField(max_length=1)
    emprestado = models.CharField(max_length=1)