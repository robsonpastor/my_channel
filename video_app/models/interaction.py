from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from video_app.models.video import Video


class Interaction(models.Model):
    is_positive = models.BooleanField(_("Is Positive"))
    time        = models.TimeField(_("Time interaction"))
    
    def get_description(self):
        if self.is_positive:
            return _("Positive")
        return _("Negative")
    
    def __unicode__(self):
        return _("{2} is {0} at {1}").format(self.get_description(), self.time, self.video.title)
    
    class Meta:
        abstract = True
        ordering = ['-time']
        verbose_name = _("Interaction")
        verbose_name_plural = _("Interactions")

class Comment(Interaction):
    video       = models.ForeignKey(Video, related_name='comments')
    
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

class Thumb(Interaction):
    video       = models.ForeignKey(Video, related_name='thumbs')

    class Meta:
        verbose_name = _("Thumb")
        verbose_name_plural = _("Thumbs")
        