from django.urls import path
from . import views

# URLconf to call the index view 
urlpatterns = [
    path('', views.index, name="index")
]
