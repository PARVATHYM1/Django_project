from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def loginadmin(request):
    if request.user.is_authenticated:
        return HttpResponse('You Are already logged in')
    else:	
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                                
                if user is not None:
                    if user.is_active and user.is_superuser:
                        login(request,user)	
                        return HttpResponse('Login Successful')
                    else:
                        return HttpResponse('Your account is not active')
                else:
                    return HttpResponse('The Account does not exists')
            else:
                login_form = LoginForm()
                return render(request, "adminpannel/login.html",{"form":login_form})
        else:
            login_form = LoginForm()
        return render(request,'adminpannel/login.html',{"form":login_form})