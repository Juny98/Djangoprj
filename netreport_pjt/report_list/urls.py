from django.urls import path
from . import views

app_name = 'report_list'

urlpatterns = [
    path('', views.index, name='list'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),

]
