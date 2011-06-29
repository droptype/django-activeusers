from django.conf.urls.defaults import *
from django.conf import settings
from activeusers import views

urlpatterns = patterns('',
    url(r'^refresh/$', views.update_active_users, name='activeusers-refresh-active-users'),
    url(r'^refresh/json/$', views.get_active_users, name='activeusers-get-active-users'),
)

