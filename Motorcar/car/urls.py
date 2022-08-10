from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('products',views.products),
    path('services',views.services),
    path('gallery',views.gallery),
]
