# volatility_app/urls.py
from django.urls import path
from .views import calculate_volatility

urlpatterns = [
    path('', calculate_volatility, name='calculate_volatility'),
]
