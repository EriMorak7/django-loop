from django.urls import path
from . import views

urlpatterns = [
    path('dict/', views.my_view, name='my_view'),
]
