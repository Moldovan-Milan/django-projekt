from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<pk>[0-9]+)/edit/$', views.product_edit, name='product_edit'),
    url("register", views.register_request, name="register"),
    url("login", views.login_request, name="login"),
    url("logout", views.logout_request, name= "log_out"),
    url("make_order", views.make_order, name= "make_order"),
    url("order_complete", views.order_complete, name= "order_complete"),
    url("order_list", views.order_list, name= 'order_list'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name="order_edit"),
]

"""
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^product/new/$', views.product_new, name='product_new'),
]
"""
