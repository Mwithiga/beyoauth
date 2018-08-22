from django.conf.urls import url
from django.contrib.auth import views
from . import views as cust_views
urlpatterns = [
 # previous login view
 # url(r'^login/$', views.user_login, name='login'),
 # login / logout urls
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login,  name='logout_then_login'),
    url(r'^$', cust_views.dashboard, name='dashboard'),
    url(r'^password-change/$', views.password_change, name='password_change'),
	url(r'^password-change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', cust_views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', cust_views.activate, name='activate'),
]