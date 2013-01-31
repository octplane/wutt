from django.conf.urls import patterns, url

from wutt.index import views



urlpatterns = patterns('',
    url(r'^$', views.index, name='wutt.index')
)
