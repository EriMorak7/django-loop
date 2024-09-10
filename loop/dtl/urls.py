from django.urls import path
from . import views

urlpatterns = [
    path('new-view/', views.new_view, name='new_view'),
]
