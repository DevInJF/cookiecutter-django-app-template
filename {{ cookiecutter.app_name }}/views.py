# -*- coding: utf-8 -*-

from django.views import generic

from .forms import ExampleForm
from .models import Example


class ExampleCreateView(generic.CreateView):
    form_class = ExampleForm


class ExampleUpdateView(generic.UpdateView):
    form_class = ExampleForm


class ExampleDeleteView(generic.DeleteView):
    model = Example


class ExampleDetailView(generic.DetailView):
    model = Example
