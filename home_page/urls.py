from django.urls import path
from home_page import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
