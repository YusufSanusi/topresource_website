from django.dispatch.dispatcher import receiver
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('landing-page')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'landing-page')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    form = CustomUserCreationForm()
    print(form)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'form': form}
    return render(request, 'users/register.html', context)
