# -*- encoding: utf-8 -*-
from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from video_app.models.video import Video, DAYS_OF_YEAR


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'date_uploaded', 'themes', 'views')
        
    def clean_date_uploaded(self):
        date_uploaded = self.cleaned_data['date_uploaded']
        if (date.today() - date_uploaded).days > DAYS_OF_YEAR:
            raise ValidationError(_("Sorry, you can not add videos older than one year."))
        if (date.today() < date_uploaded):
            raise ValidationError(_("Sorry, but you can not add videos that you have not uploaded yet."))
        return date_uploaded