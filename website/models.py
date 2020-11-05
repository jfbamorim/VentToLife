from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import date


class Tecnico(models.Model):
    first_name = models.CharField('Nome', max_length=255)
    last_name = models.CharField('Apelido', max_length=255)
    email = models.EmailField('Email', max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?9?\d{9}$',
                                 message="O número de telemóvel é inválido.")
    phone_number = models.CharField('Telemovel', validators=[phone_regex], max_length=9, blank=True)
    nif = models.CharField(max_length=9, validators=[RegexValidator(regex='^.{9}$', message='O NIF não está correto',
                                                                    code='nomatch')])
    state = models.CharField('Cidade', max_length=255)
    compname = models.CharField('Nome Empresa', max_length=255)
    password = models.CharField('Password', max_length=255)

    @property
    def __str__(self):
        return self.first_name + " " + self.last_name


class Hospital(models.Model):
    first_name = models.CharField('Nome', max_length=255)
    last_name = models.CharField('Apelido', max_length=255)
    email = models.EmailField('Email', max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?9?\d{9}$',
                                 message="O número de telemóvel é inválido.")
    phone_number = models.CharField('Telemovel', validators=[phone_regex], max_length=9, blank=True)
    nif = models.CharField(max_length=9, validators=[RegexValidator(regex='^.{9}$', message='O NIF não está correto',
                                                                    code='nomatch')])
    state = models.CharField('Cidade', max_length=255)
    hospital = models.CharField('Hospital', max_length=255)
    password = models.CharField('Password', max_length=255)

    @property
    def __str__(self):
        return self.first_name + " " + self.last_name


class Pedido(models.Model):
    titulo = models.CharField(max_length=50, default="Novo Pedido Criado")
    hospital = models.CharField(max_length=255)
    severidade = models.CharField(max_length=200)
    ventilador = models.CharField(max_length=200)
    messages = models.CharField(max_length=4000)
    date = models.DateField(default=date.today, blank=True)
    answers = models.IntegerField(default=0)
    username = models.CharField(max_length=255, null=True)


class Resposta(models.Model):
    pedido = models.CharField(max_length=5)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    messages = models.CharField(max_length=4000)
    date = models.DateField(default=date.today, blank=True)
    username = models.CharField(max_length=255, null=True)
