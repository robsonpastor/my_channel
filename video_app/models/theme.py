from __future__ import unicode_literals

from django.db import models


class Theme(models.Model):
    name = models.CharField('Name',max_length=200)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
    def score(self):
        return sum(video.score() for video in self.videos.all())