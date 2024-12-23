from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return logout(request, 'home.html')

def homePage(request):
    return render(request, 'homePage.html')