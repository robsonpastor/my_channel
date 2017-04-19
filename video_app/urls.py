# -*- encoding: utf-8 -*-

from django.conf.urls import url

from video_app.views.rankings import get_popular_themes


urlpatterns = [
    url(r'^get_popular_themes/$', get_popular_themes),
]
