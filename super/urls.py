from django.urls import path
from . import views

app = 'super'

urlpatterns = [
    path('', views.index, name='index'),
]
