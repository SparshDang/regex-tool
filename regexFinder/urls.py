from django.urls import path
from regexFinder import views

urlpatterns = [
    path('', views.index, name='home')
]
