from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("login")
    else:
        form  = UserRegisterForm()

    pagename = "Sign up now!"
    context = {'pagename': pagename, 'form': form}
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    return render(request, "home/home.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password.")
            
    pagename = "Login now!"
    context = {'pagename': pagename}
    return render(request, 'home/about.html', context)
