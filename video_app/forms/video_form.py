# -*- encoding: utf-8 -*-
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from video_app.models.video import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'date_uploaded', 'themes', 'views')
        
    def clean_date_uploaded(self):
        date_uploaded = self.cleaned_data['date_uploaded']
        if (date.today() - date_uploaded).days > 365:
            raise ValidationError("Sorry, you can not add videos older than one year.")
        if (date.today() < date_uploaded):
            raise ValidationError("Sorry, but you can not add videos that you have not uploaded yet.")
        return date_uploaded