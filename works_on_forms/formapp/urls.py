from django.urls import path
from . import views
urlpatterns=[
    path('',views.show_form,name='show_form'),
    path('submit_form',views.submit_form,name='submit_form'),
    path('display_data',views.display_data,name='display_data'),
]