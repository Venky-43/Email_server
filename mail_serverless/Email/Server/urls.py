from django.urls import path
from .views import Mail

urlpatterns = [
    path('Email/',Mail.as_view())
]