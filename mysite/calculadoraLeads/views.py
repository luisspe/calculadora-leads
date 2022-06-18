from django.shortcuts import render

# Create your views here.
def calculadora(request):
    context = {}
    return render(request, 'calculadoraLeads/calCantidad.html', context)

def ltv(request):
    context = {}
    return render(request, 'calculadoraLeads/calLTV.html', context)

def valor(request):
    context = {}
    return render(request, 'calculadoraLeads/calValor.html', context)