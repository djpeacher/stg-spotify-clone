from django.urls import path

from . import views

urlpatterns = [
    path("catalog/", views.CatalogView.as_view(), name="catalog"),
]
