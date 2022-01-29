from django.shortcuts import render, redirect
from qrcode import *
# for authenticates
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from home import models

# Create your views here.
data = None


def home(request):
    # can pass variables to html page
    # context = {
    #     'name':'mohamed',
    #     'learning': 'web'
    # }
    # return HttpResponse("this is my homepage (/)")
    return render(request, 'home.html')


def material(request):
    return render(request, 'material.html')


def contact(request):
    if request.method == 'POST':
        # do stuff
        print("Got Post Request")
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = models.Contact(name=name, email=email, message=message)
        ins.save()  # save to db
        print("data has been saved")
    return render(request, 'contact.html')


# make a about page
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def userprofile(request):
    context = {}
    return render(request, 'UserProfile.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def login(request):
    if request.method == 'POST':
        # authenticate user login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('userprofile')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can log in now {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def quiz(request):
    return render(request, 'quiz.html')


def qrcode(request):
    global data
    if request.method == "POST":
        data = request.POST['data']
        img = make(data)
        img.save("static/image/test.png")
    else:
        pass
    return render(request, "qrcode.html", {'data': data})
