from django.shortcuts import render
from home import models
# Create your views here.


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
        ins.save() # save to db
        print("data has been saved")
    return render(request, 'contact.html')

# make a about page
def about(reguest):
    return render(reguest, 'about.html')


def userprofile(reguest):
    return render(reguest, 'UserProfile.html')


def login(reguest):
    return render(reguest, 'login.html')

def register(reguest):
    return render(reguest, 'register.html')
