from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    users = get_user_model().objects.order_by('pk')

    context = {
        'users' : users,
    }

    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('accounts:index')
    else:   
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def detail(request, pk):
    
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user
    }

    return render(request, 'accounts/detail.html', context)