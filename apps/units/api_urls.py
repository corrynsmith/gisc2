from django.conf.urls import patterns, include, url
from apps.units import json_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^units$', json_views.UserCollection.as_view(), name='units'),

    )