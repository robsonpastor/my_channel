# -*- encoding: utf-8 -*-
from django import forms

from video_app.models.video import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'date_uploaded', 'themes', 'views')