# -*- encoding: utf-8 -*-

from django.conf.urls import url
from video_app.views.theme_view import ThemeView


urlpatterns = [
    url(r'^themes/$', ThemeView.as_view()),
]
