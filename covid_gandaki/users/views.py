from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout

from covid_gandaki.users.models import Employee
# Create your views here.
from django.conf import settings
import json

def landing(request):
    # with open(settings.STATICFILES_DIRS[0] + '/data.json', 'r') as f:
    #     data = eval(f.read())
    data = []
    with open(settings.STATICFILES_DIRS[0] + '/data1.json', 'r') as f:
        data = json.loads(f.read())
    context = {
        'data': data,
        'num': int(12/len(data)),
    }
    return render(request, 'users/landing.html', context)

def index(request):
    
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)


def login_view(request):
    #Loggin in the UsersConfig
    if request.user.is_authenticated:
        return redirect('form:lbindex')
    if request.method == 'POST':
        #Do sth
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['employee'] = Employee.objects.get(user=user).municipality.address.mun.mun_name
            return redirect('form:lbindex')

    else:
        #instantiate
        form = AuthenticationForm()
    request.session.set_expiry(3000)
    return render(request, 'users/login.html', {'form': form, 'message':request.session.get('message', "Welcome")})
    

def logout_view(request):
    logout(request)
    return redirect('users:login')
