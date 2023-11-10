from django.shortcuts import render

# Create your views here.

def sahithi(request):
    return render(request,'sahithi.html')

def lalitha(request):
    return render(request,'lalitha.html')

def vasundhara(request):
    return render(request,'vasundhara.html')

def divya(request):
    return render(request,'divya.html')
