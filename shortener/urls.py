from django.urls import path
from shortener import views

urlpatterns = [
    path('', views.ShortenerView.as_view(), name='shortener-post')
]