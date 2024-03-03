from django.shortcuts import render, redirect

def homePage(request):
    context = {}
    return render(request, 'base/home.html', context)