from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser),
    path('login/',views.longinUser),
]