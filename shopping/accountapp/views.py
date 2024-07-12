from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username,"username")
        email = request.POST['email']
        print(email, "email")
        password1 = request.POST['password1']
        print(password1, "password1")
        password2 = request.POST['password2']
        print(password2, "password2")
        if User.objects.filter(username=username).exists():
             print("here")
             messages.info(request, "username taken")
             return redirect('register')
        if password1 == password2:
        
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print("user created")
        else:
              messages.info(request, "password not matching")
              return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def login(request):
     if request.method=="POST":
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request,"invalid details")
               return render(request,'login.html')
     else:
          return render(request,'login.html')

def logout(request):
     auth.logout(request)
     return redirect('login')



