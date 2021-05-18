from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import Userform

# Create your views here.
def index(request):

    form = Userform()
    if request.user.is_authenticated:
        return redirect(dashboard)
    elif request.method == 'POST':
        print('fail')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_active:
            auth_login(request,user)
            
            return redirect(dashboard)
                
    else:
        return render(request, 'login/login.html', {'form': form})

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect(index)


def dashboard(request):
    return render(request, 'login/dashboard.html')

def register(request):
    return render(request, 'login/register.html')