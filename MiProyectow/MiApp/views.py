from django.shortcuts import render

from MiApp.models import Familiares
# Create your views here.

def mostrar_familiares(request):

    a1 = Familiares(nombre='Juan Cruz', apellido= 'Romero', edad=21, cumpleaños= '2001-02-23')
    a2 = Familiares(nombre='Adrian', apellido= 'Perez', edad=50, cumpleaños= '1971-07-13')
    a3 = Familiares(nombre='Maria', apellido= 'Diaz', edad=23, cumpleaños= '1999-07-13')
    
    return render(request, 'MiApp/familiares.html', {'familiares':[a1, a2, a3]})