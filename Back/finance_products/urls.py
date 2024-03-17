from django.urls import path
from . import views


urlpatterns = [
    path('getDepositProduct/', views.getDepositProduct),
    path('getSavingProduct/', views.getSavingProduct),
    path('clientDepositProduct/', views.clientDepositProduct),
    path('clientDepositDetail/<str:ptcd1>', views.clientDepositDetail),
    path('clientDepositCompare/<str:ptcd1>/<str:ptcd2>', views.clientDepositCompare),
]
