from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from website.forms import HospitalForm, TecnicoForm
from website.models import Pedido, Resposta
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def loginv2(request):
    if request.method == "POST":
        try:
            user = request.POST['puser']
            password = request.POST['ppass']
            utilizador = authenticate(username=user, password=password)
            if utilizador is not None:
                login(request, utilizador)
                return HttpResponseRedirect(reverse('website:forum'), {'utilizador': utilizador}, )
            else:
                messages.error(request, 'Erro no utilizador e/ou password')
                return HttpResponseRedirect(reverse('website:login'))
        except User.DoesNotExist:
            raise Http404("Utilizador inválido")
    else:
        if request.user.is_authenticated:
            utilizador = request.user.username
            return HttpResponseRedirect(reverse('website:forum'), {'utilizador': utilizador}, )
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, 'login.html')


def hospital(request):
    if request.method == "POST":
        try:
            password = request.POST['password']
            confirm = request.POST['repeat_password']
            if password != confirm:
                messages.error(request, 'Password não coincide')
                return HttpResponseRedirect(reverse('website:technical'))
            else:
                hosp = HospitalForm(request.POST)
                if hosp.is_valid():
                    username = request.POST['email']
                    password = request.POST['password']
                    email = request.POST['email']
                    fname = request.POST['first_name']
                    lname = request.POST['last_name']

                    if User.objects.filter(username=request.POST['email']).exists():
                        messages.error(request, 'Utilizador já registado')
                        HttpResponseRedirect(reverse('website:hospital'))
                    else:
                        hosp.save()
                        User.objects.create_user(username=username,
                                                 password=password,
                                                 email=email,
                                                 first_name=fname,
                                                 last_name=lname)
                        messages.success(request, 'Utilizador registado com sucesso. Faça login com o seu endereço de '
                                         'email')
                        return HttpResponseRedirect(reverse('website:login'))
                else:
                    messages.error(request, hosp.errors)
                    HttpResponseRedirect(reverse('website:hospital'))
        except request.IntegrityError:
            raise Http404("Utilizador de saúde já registado")
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, 'hospital.html')


def technical(request):
    if request.method == "POST":
        try:
            password = request.POST['password']
            confirm = request.POST['repeat_password']
            if password != confirm:
                messages.error(request, 'Password não coincide')
                return HttpResponseRedirect(reverse('website:technical'))
            else:
                tech = TecnicoForm(request.POST)
                if tech.is_valid():
                    username = request.POST['email']
                    password = request.POST['password']
                    email = request.POST['email']
                    fname = request.POST['first_name']
                    lname = request.POST['last_name']

                    if User.objects.filter(username=request.POST['email']).exists():
                        messages.error(request, 'Utilizador já registado')
                        HttpResponseRedirect(reverse('website:technical'))
                    else:
                        tech.save()
                        user = User.objects.create_user(username=username,
                                                        password=password,
                                                        email=email,
                                                        first_name=fname,
                                                        last_name=lname)
                        messages.success(request, 'Utilizador registado com sucesso. Faça login com o seu endereço de '
                                                  'email.')
                        return HttpResponseRedirect(reverse('website:login'))
                else:
                    messages.error(request, 'O formulário não se encontra bem preenchido.')
                    HttpResponseRedirect(reverse('website:technical'))
        except request.IntegrityError:
            raise Http404("Utilizador técnico já registado")
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, 'technical.html')


@login_required(login_url="../templates/login.hmtl")
def forum(request):
    count_saojoao = Pedido.objects.filter(hospital="São João").count()
    count_curcabr = Pedido.objects.filter(hospital="Curry Cabral").count()
    count_hsbraga = Pedido.objects.filter(hospital="Hospital de Braga").count()
    count_hpcoimb = Pedido.objects.filter(hospital="Hospital Pediátrico de Coimbra").count()
    count_uslguar = Pedido.objects.filter(hospital="Unidade Local de Saúde da Guarda").count()
    context = {'saojoao':count_saojoao, 'curcabr':count_curcabr, 'hsbraga':count_hsbraga,
               'hpcoimb':count_hpcoimb, 'uslguar':count_uslguar}
    return render(request, 'newforum.html', context)


@login_required(login_url="../templates/login.hmtl")
def saojoao(request):
    pedidos = Pedido.objects.all().filter(hospital="São João")
    return render(request, 'newsaojoao.html',{'pedidos' : pedidos})


@login_required(login_url="../templates/login.hmtl")
def hospbraga(request):
    pedidos = Pedido.objects.all().filter(hospital="Hospital de Braga")
    return render(request, 'newhospbraga.html',{'pedidos' : pedidos})


@login_required(login_url="../templates/login.hmtl")
def ulsguarda(request):
    pedidos = Pedido.objects.all().filter(hospital="Unidade Local de Saúde da Guarda")
    return render(request, 'newulsguarda.html',{'pedidos' : pedidos})


@login_required(login_url="../templates/login.hmtl")
def currycabral(request):
    pedidos = Pedido.objects.all().filter(hospital="Curry Cabral")
    return render(request, 'newcurrycabral.html',{'pedidos' : pedidos})


@login_required(login_url="../templates/login.hmtl")
def hpcoimbra(request):
    pedidos = Pedido.objects.all().filter(hospital="Hospital Pediátrico de Coimbra")
    return render(request, 'newhpcoimbra.html',{'pedidos' : pedidos})


@login_required(login_url="../templates/login.hmtl")
def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))


@login_required(login_url="../templates/login.hmtl")
def pedido(request):
    if request.method == "POST":
        pedido = Pedido(titulo=request.POST['titulo'],
                        hospital=request.POST['hospital'],
                        severidade=request.POST['severidade'],
                        ventilador=request.POST['ventilador'],
                        messages=request.POST['messages'],
                        date=timezone.now(),
                        username=request.user.username,
                        )

        pedido.save()
        messages.success(request, 'Pedido criado com sucesso.')
        return HttpResponseRedirect(reverse('website:forum'), {'pedido': pedido}, )
    #else:
        #messages.error(request, 'Erro na criação do pedido')
        #return HttpResponseRedirect(reverse('website:pedido'))
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, 'request.html')


def changerequest(request, pedido_id):
    pedido = Pedido.objects.all().filter(pk=pedido_id)
    answer = Resposta.objects.all().filter(pedido=pedido_id)
    if request.method == "POST":
        message_data = request.POST['messages']
        resps = Resposta(pedido=(int(pedido_id)),
                         messages=message_data,
                         date=timezone.now(),
                         username=request.user.username,
                         )
        resps.save()
        return render(request, 'post.html', {'pedido':pedido, 'answer':answer})
    return render(request, 'post.html', {'pedido':pedido, 'answer':answer})

