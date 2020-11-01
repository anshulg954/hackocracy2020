from django.shortcuts import render

def homePage(request):
    context = {}
    return render(request, 'HomeIndex/HomePage.html', context)

def stats(request):
    return render(request,'HomeIndex/stats.html')