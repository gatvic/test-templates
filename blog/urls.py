from django.urls import path

from .views import index, choice

urlpatterns = [
    path('', index, name='index'),
    path('choice_plant', choice, name='choice'),
]
