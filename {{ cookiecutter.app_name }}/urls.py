# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (
    ExampleCreateView,
    ExampleDeleteView,
    ExampleDetailView,
    ExampleListView,
    ExampleUpdateView,
)


urlpatterns = [
    url(r'^$', ExampleListView.as_view(), name='list'),
    url(r'^create/$', ExampleCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', ExampleDeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)/$', ExampleUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/$', ExampleDetailView.as_view(), name='detail'),
]
