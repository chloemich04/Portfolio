from django.shortcuts import render

from .projects import PROJECTS


def index(request):
    featured = [project for project in PROJECTS if project["featured"]]
    return render(request, "main/index.html", {"projects": featured})


def projects(request):
    return render(request, "main/projects.html", {"projects": PROJECTS})


def contact(request):
    return render(request, "main/contact.html", {})


def research(request):
    return render(request, "main/research.html", {})
