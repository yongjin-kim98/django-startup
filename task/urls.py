from django.urls import URLPattern, path

from task import views

URLPatterns = [
    path("index/", views.index),
    path("pokeball/", views.pokeball),
    path("lorem/", views.lorem),
]