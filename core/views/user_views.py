from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models.user import CustomUser
from core.forms.user_registration_form import UserRegistrationForm
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import urlparse


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form, 'error': form.errors})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form, 'error': form.errors})

class UserLoginView(View):
    def get(self, request):
        next_url = request.GET.get('next', '')  # Capture the 'next' parameter
        return render(request, 'login.html', {'next': next_url})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get('next', '')  # Capture the 'next' parameter from POST data

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            else:
                return redirect('home')
        elif username == '' or password == '':
            return render(request, 'login.html', {'error': 'Invalid username or password', 'next': next_url})
        else:
            return render(request, 'login.html', {'error': 'Invalid login', 'next': next_url})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('home')
