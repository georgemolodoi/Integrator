from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze, name='analyze'),
    # path('', views.index, name='index'),
    ]
