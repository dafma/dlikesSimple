from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_detail,
    PostLikeToggle,
    PostLikeAPIToggle,
    )

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    ]