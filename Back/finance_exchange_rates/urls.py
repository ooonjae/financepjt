from django.urls import path
from . import views


urlpatterns = [
    path('exchangerate/', views.getExchangeRate),
    path('clientExchangeRate/', views.clientExchangeRate),
]
