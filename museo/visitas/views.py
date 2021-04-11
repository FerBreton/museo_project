from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
import datetime
# Create your views here.

#def home(request):
 #   return render(request, "index.html", {})

class Home(View):
    def get(self, request):
        return render(request, 'index.html', {})

class Entrada(View):
    def get(self, request):
        form = VisitaForm()
        context = {'form': form}
        return render(request, 'entrada.html', context)

    ''' Validación 
        1. Correo no duplicado
    '''
    
    def post(self, request):
        form = VisitaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            visitas = Visita.objects.filter(timestamp_in__gte=datetime.date.today(), timestamp_out=None, email=entrada.email)
            if visitas:
                print("Ya esta registrado")
            else:
                print("Entrada registrada")
                entrada.save()
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'entrada.html', context)

class Salida(View):
    def get(self, request):
        form = SalidaForm()
        context = {'form': form}
        return render(request, 'salida.html', context)

    ''' Validación 
        1. Correo sí exista
        2. Timestamp out
        3. Datetime.today 
    '''
    
    def post(self, request):
        form = SalidaForm(request.POST)
        if form.is_valid():
            salida = form.save(commit=False)
            print(salida.email)
            print(datetime.date.today())

            visitas = Visita.objects.filter(email=salida.email, timestamp_out=None, timestamp_in__gte=datetime.date.today())
            if visitas:
                print(f"Si hay registros: {visitas}")
                visita = Visita.objects.get(pk=visitas[0].id)
                visita.timestamp_out = datetime.datetime.now()
                visita.comment = salida.comment
                visita.save()
            else:
                print("No has registrado una entrada")

            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'salida.html', context)