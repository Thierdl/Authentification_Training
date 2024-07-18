from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .import forms


def login_views(request):
  form = forms.LoginForm(request.POST or None)
  if form.is_valid():
    user_name = form.cleaned_data.get("user_name")
    pass_word = form.cleaned_data.get("pass_word")
    user = authenticate(username=user_name, password=pass_word)
    
    if user is not None:
      login (request, user)
      return redirect("//")


  return render(request, "authen/login.html", {"form":form})

