from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("editpage", views.editpage, name="editpage"),
    path("randompage", views.random_page, name="random_page"),
]
