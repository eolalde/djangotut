# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 13:38:09 2014

@author: Eusebio Olalde
"""

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       )
                       
