from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

def UserSignUp(request):
     
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user=form.save()
               username=form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(request,username=username,password=password)
               login(request,user)
               return redirect('create_profile')
          
     else:
          form = UserCreationForm()
     context = {'form':form}
     return render (request,'signup.html',context)



def UserLogin(request):
     
     if request.method == 'POST':
          username = request.POST.get('username',None)
          password = request.POST.get('password',None)
          user = authenticate(request,username = username,password=password)

          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               messages.error(request,'Invalid Username or Password')
               return render (request,'login.html')
     else:
          context = {'user': request.user}
          return render(request,'login.html',context)
     

def UserLogout(request):
     logout(request)
     return redirect('home')
