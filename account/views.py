from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from account.forms import ProfileEditForm, RegisterForm


def user_register(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else :
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                messages.info(request, 'Registration completed.')

                new_user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
                login(request, new_user)
                return redirect('tasks')
            else :
                messages.error(request, 'Something went wrong.')
        else:
            form = RegisterForm()
        context = {
            'form': form,
            'sec_title': 'Register'
        }
        return render(request, 'register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks')
            else:
                messages.error(request, 'Invalid username or password.')

        return render(request, 'login.html', {'sec_title': "Login"})


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance = request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated.')
        else:
            messages.error(request, 'Something went wrong.')


    else:
        user_form = ProfileEditForm(instance = request.user)

    return render(request, 'profile.html', {'form': user_form, 'sec_title': 'Profile'})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

