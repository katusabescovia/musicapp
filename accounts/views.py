from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from django.contrib.auth.models import auth
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def landing_page(request):
    return render(request, 'registration/landing_page.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login after signup
    template_name = 'registration/signup.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile/edit_profile.html', {'form': form})




