from django.shortcuts import render
from accounts.forms import CustomUserCreationForm as RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login/")
        
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})
