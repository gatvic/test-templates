from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.choice, name='choice'),
    path('blog/', views.ad_plant, name='ad_plant'),
    path('blog/', views.ad_sub, name='ad_sub'),
]
