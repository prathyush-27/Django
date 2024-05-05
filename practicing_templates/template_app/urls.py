from django.urls import path
from .views import templates

urlpatterns=[
    path('',templates,name='index'),
]