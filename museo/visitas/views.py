from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
# Create your views here.

#def home(request):
 #   return render(request, "index.html", {})

class Home(View):
    def get(self, request):
        form = VisitaForm()
        context = {'form': form}
        return render(request, 'index.html', context)
    
    def post(self, request):
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'index.html', context)