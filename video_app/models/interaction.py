from __future__ import unicode_literals

from django.db import models

from video_app.models.video import Video


class Interaction(models.Model):
    is_positive = models.BooleanField('Is Positive')
    time        = models.TimeField('Time interaction')
    def __unicode__(self):
        return self.name
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = 'Interaction'
        verbose_name_plural = 'Interactions'

class Comment(Interaction):
    video       = models.ForeignKey(Video, related_name='comments')
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Thumb(Interaction):
    video       = models.ForeignKey(Video, related_name='thumbs')
    class Meta:
        verbose_name = 'Thumb'
        verbose_name_plural = 'Thumbs'
        