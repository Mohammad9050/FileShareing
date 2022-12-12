from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from Accounts.forms import *


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponse(username)
    else:
        form = SignUpForm()
    return render(request, 'Accounts/sign_up.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            context['error'] = 'username or password is wrong!'
            return render(request, 'Accounts/login.html', context)
        else:
            login(request, user)
            return HttpResponse(username)
    else:
        return render(request, 'Accounts/login.html', context)
