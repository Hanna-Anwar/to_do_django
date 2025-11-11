from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from user_app.forms import RegistrationForm

from user_app.models import User

from django.contrib.auth import authenticate,login,logout

from task_app.models import TaskModel

#adding to db

class RegistrationView(View):

    def get(self,request):

        form = RegistrationForm()

        return render(request,"registration.html",{"form":form})


    def post(self,request):

        print(request.POST)

        username= request.POST.get('username')

        first_name= request.POST.get('first_name')

        last_name= request.POST.get('last_name')

        email= request.POST.get('email')
        
        password= request.POST.get('password')

        User.objects.create_user(username=username,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email,
                                 password=password)
        
        form = RegistrationForm()
        
        return redirect("login")

#login

#get,post


class LoginView(View):

    def get(self,request):

        return render(request,"login.html")
    
    def post(self,request):
   
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        # print("Authenticated user:", user)

        if user:

            login(request,user)

            return redirect("home")
        
        return redirect("login")


class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("home")

class HomeView(View):

    def get(self,request):

        if request.user.is_authenticated:

            task = TaskModel.objects.filter(user = request.user)

            return render(request,"home.html",{"task":task})
        
        return render(request,"home.html")
        
    
