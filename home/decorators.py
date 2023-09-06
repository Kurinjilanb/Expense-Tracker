from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def unauthorized(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func