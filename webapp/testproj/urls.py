from django.conf.urls import patterns, url

from webapp.testapp.views import hello

urlpatterns = patterns('',
    url('', hello),
)
