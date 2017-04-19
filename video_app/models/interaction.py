from __future__ import unicode_literals

from django.db import models

from video_app.models.video import Video


class Interaction(models.Model):
    is_positive = models.BooleanField('Is Positive')
    time        = models.TimeField('Time interaction')
    
    def get_description(self):
        if self.is_positive:
            return 'Positive'
        return 'Negative'
    
    def __unicode__(self):
        return "{} at {}".format(self.get_description(), self.time)
    
    class Meta:
        abstract = True
        ordering = ['-time']
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
        