# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.db import models
from django.utils.text import slugify
import os

# Create your models here.

class Usuario(models.Model):
	data_cadastro = models.DateField('Cadastro',default=datetime.now())
	nome = models.CharField("Nome",max_length = 300, default="")
	email = models.CharField("Nome",max_length = 300, default="")
	link = models.CharField("Nome",max_length = 300, default="")
	telefone = models.CharField("Nome",max_length = 300, default="")
	senha = models.CharField("Nome",max_length = 300, default="")
