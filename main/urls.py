from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("research/", views.research, name="research"),
    path("contact/", views.contact, name="contact"),
]
