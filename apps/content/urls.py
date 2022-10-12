from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("resources/", views.ResourcesView.as_view(), name="resources"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
