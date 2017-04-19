from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Theme(models.Model):
    name = models.CharField(_("Name"),max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")
    
    def __unicode__(self):
        return self.name
    
    def score(self):
        return sum(video.score() for video in self.videos.all())