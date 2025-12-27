from django.shortcuts import render
from django.http import HttpResponse  
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView, SignupView,LogoutView
from .form import CustomLoginForm, CustomSignupForm


# Create your views here.
def home(request):  
    return HttpResponse("hello")

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomSignupView(SignupView):
    template_name = 'accounts/signup.html'


def forgot_pass(request):
    return HttpResponse("hello")

class CustomLogoutView(LogoutView):
    next_page = '/'


# @login_required
def profile(request):
    # You can pass user details to the template if needed
    return render(request, 'accounts/profile.html', {'user': request.user})