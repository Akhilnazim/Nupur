from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username, password=password)

         if user is not None:
             auth.login(request, user)
             return redirect('/')
         else:
            return redirect('login')
    else:
         return render(request, 'my-account.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            # messages.info(request, 'Username taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            print("user created")
            return redirect('/')
            # return redirect("index.html")
        return redirect('/')

    else:
        return render(request, 'my-account.html')
