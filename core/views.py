from django.shortcuts import render

def core(request):
    return render(request,'core/core.html')
def home(request):
    return render(request,'core/home.html')
