from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/base.html', {})


def choice(request):
    return render(request, 'blog/choice_plant.html')
