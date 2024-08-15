from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib import messages

from .forms import LoginForm

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                next_url = request.GET.get('next')
                return redirect(next_url if next_url else 'home')
            
            else:
                form = LoginForm()
                messages.error(request, 'Invalid email or password')

    return render(request, 'users/login.html', {'form': form})
