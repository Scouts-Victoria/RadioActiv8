from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *


def index(request):
    return render("Hello World. You're at the RadioActiv8 index.")


class PatrolList(generic.ListView):
    template_name = 'patrol/index.html'

    def get_queryset(self):
        """Return a list of Patrols."""
        return Patrol.objects.all()


class PatrolDetail(generic.DetailView):
    model = Patrol
    template_name = 'patrol/detail.html'


class BaseList(generic.ListView):
    template_name = 'base/index.html'

    def get_queryset(self):
        """Return a list of Bases."""
        return Base.objects.all()


class BaseDetail(generic.DetailView):
    model = Base
    template_name = 'base/detail.html'