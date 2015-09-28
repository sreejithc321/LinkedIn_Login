from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url

from views import code,linkedin


urlpatterns = patterns('',
    url(r'^code/$', code),
    url(r'^linkedin/$', linkedin),
)
