# encoding: utf-8
from django.conf.urls import patterns, url

from views import IndexView
from views import CustomProductionView, LibraryProductionView
from views import CustomDevView, LibraryDevView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^cp/$', CustomProductionView.as_view(), name='cp'),
    url(r'^cd/$', CustomDevView.as_view(), name='cd'),
    url(r'^lp/$', LibraryProductionView.as_view(), name='lp'),
    url(r'^ld/$', LibraryDevView.as_view(), name='ld'),

)
