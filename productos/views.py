from django.shortcuts import render

from .models import Producto

def listar(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos': productos})
