from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("downloader/", views.downloader, name="downloader"),
    path("combinepdf/", views.combinepdf, name="combinepdf")
]