# -*- encoding: utf-8 -*-
from django import forms

from video_app.models.theme import Theme


class ThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        fields = ('name',)