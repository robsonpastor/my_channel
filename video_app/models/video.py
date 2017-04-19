from __future__ import unicode_literals

from django.db import models
from video_app.models.theme import Theme

class Video(models.Model):
    title         = models.CharField('Title',max_length=200)
    date_uploaded = models.DateField('Date Uploaded')
    views         = models.IntegerField('Views')
    themes        = models.ManyToManyField(Theme)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        