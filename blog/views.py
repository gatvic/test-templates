from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/base.html', {})


def choice(request):
    return render(request, 'blog/choice_plant.html', {})


def ad_plant(request):
    return render(request, 'blog/ad_plant.html', {})


def ad_sub(request):
    return render(request, 'blog/ad_sub.html', {})
