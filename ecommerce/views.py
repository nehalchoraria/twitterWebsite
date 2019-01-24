from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.http import HttpResponseRedirect
from tweet.models import UserType

def loginPage(request):
    form = LoginForm(request.POST or None)
    context={'form':form}
    if request.user.is_authenticated==True:
        return HttpResponseRedirect("/home")

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if request.user.is_authenticated==True:
                return HttpResponseRedirect("/home")
            else:
                return render(request,"auth/login.html",context)
        else:
            context['update']="Username and Password is incorrect!"
    return render(request,"auth/login.html",context)

User=get_user_model()
def registerPage(request):
    form=RegisterForm(request.POST or None)
    context={'form':form}
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        email=form.cleaned_data.get("email")
        account=form.cleaned_data.get("account")
        User.objects.create_user(username,email,password)

        user = authenticate(username=username, password=password)
        UserType.objects.create(author=user,type=account)
        form=RegisterForm()
        context['update']="User added succesfully."

    return render(request,"auth/register.html",context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect("/login")
