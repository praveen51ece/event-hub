from django.conf.urls import url

from . import views,auth_view

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.event_dashboard, name='event_dashboard'),
    url(r'^event_insert/$', views.event_insert, name='event_insert'),
    url(r'^user_insert/$', views.user_insert, name='user_insert'),

    url(r'^login/$', auth_view.login, name='login'),


]