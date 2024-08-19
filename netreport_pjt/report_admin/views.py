from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('report_main:index')
        
    else:
        form = AuthenticationForm()
    context = { 'form': form }
    return render(request, 'report_admin/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('report_main:index')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_main:index')
    else:
        form = CustomUserCreationForm()
    context = { 'form': form }
    return render(request, 'report_admin/signup.html', context)


def delete(request):
    user = request.user
    user.delete()
    auth_logout(request)

    return redirect('report_main:index')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('report_main:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = { 'form': form }
    return render(request, 'report_admin/update.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('report_main:index')
    else:
        form = PasswordChangeForm(request.user)
    context = { 'form': form }
    return render(request, 'report_admin/change_password.html', context)

