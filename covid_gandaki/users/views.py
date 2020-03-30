from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)


def login_view(request):
    #Loggin in the UsersConfig
    if request.method == 'POST':
        #Do sth
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('form:dashboard')

    else:
        #instantiate
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('users:login')
