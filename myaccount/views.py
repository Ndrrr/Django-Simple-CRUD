from django.shortcuts import render
from .forms import Quiz
from django.http import HttpResponseRedirect
from accounts.models import CustomUser as User
# Create your views here.
def myaccount(request):
    user = User.objects.filter(username=request.user.username).first()
    if request.method == "POST":
        quiz = Quiz(request.POST)
        if quiz.is_valid():
            if( quiz.cleaned_data['age'] ):
                user.age = quiz.cleaned_data['age']
                print(user.age)
            if( quiz.cleaned_data['weight'] ):
                user.weight = quiz.cleaned_data['weight']
            if( quiz.cleaned_data['height']):      
                user.height = quiz.cleaned_data['height']
            user.save()
            return HttpResponseRedirect("/myaccount/")
    else:
        quiz = Quiz()
    return render(request, 'myaccount/myaccount.html', {"quiz":quiz})