from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views import View
from auth import forms
# Create your views here.
class Login(LoginView):
    template_name = 'auth/login.html'
   

class Logout(LogoutView):
    pass

class Signup(View):
    def get(self, request):
        context = {
            'form' : forms.SignUpForm()
        }
        return render(request, 'auth/signup.html', context)
        
    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')

        context = {
            "form" : form
        }
        return render(request, 'auth/signup.html', context)
