from django.urls import path
from . import views

app_name = 'random'

urlpatterns = [
    path('', views.Index, name='index'),
    path('result', views.returnResult, name='returnResult'),
]
