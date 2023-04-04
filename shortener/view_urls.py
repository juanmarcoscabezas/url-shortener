from django.urls import path
from shortener import views

urlpatterns = [
    path('<str:encoded>', views.ShortenerRedirect, name='shortener-redirect')
]