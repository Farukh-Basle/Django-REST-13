from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def login_form_view(request):
    return render(request,'login.html')

def login_user_view(request):
    username = request.POST.get('uname')
    password = request.POST.get('pwd')
    user = authenticate(username=username,password=password) #resp may be none or obj

    if user is None:
        return redirect('login')   #keep cursor on redirect press alt+enter

    else:
        login(request,user)
        return redirect('/api/')