from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from video_app.models.theme import Theme


DAYS_OF_YEAR = 365

class Video(models.Model):
    title         = models.CharField(_("Title"),max_length=200)
    date_uploaded = models.DateField(_("Date Uploaded"))
    views         = models.IntegerField(_("Views"))
    themes        = models.ManyToManyField(Theme,related_name='videos')
    
    class Meta:
        ordering = ['title']
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
    
    def __unicode__(self):
        return self.title
    
    def days_since_upload(self):
        return (date.today() - self.date_uploaded).days
    
    def time_factor(self):
        return max(0,1-(self.days_since_upload()/DAYS_OF_YEAR))
    
    def positive_comments(self):
        return self.comments.filter(is_positive=True)
    
    def negative_comments(self):
        return self.comments.filter(is_positive=False)
    
    """GoodComments"""
    def good_comments_rating(self):
        positive = self.positive_comments().count()
        negative = self.negative_comments().count()
        try:
            return positive/(positive+negative)
        except ZeroDivisionError:
            return 0
        
    def thumbs_up(self):
        return self.thumbs.filter(is_positive=True)
    
    def thumbs_down(self):
        return self.thumbs.filter(is_positive=False)
    
    """ThumbsUp"""
    def thumbs_up_rating(self):
        positive = self.thumbs_up().count()
        negative = self.thumbs_down().count()
        try:
            return positive/(positive+negative)
        except ZeroDivisionError:
            return 0
    
    def positivity_factor(self):
        return 0.7 * self.good_comments_rating() + 0.3 * self.thumbs_up_rating()
    
    def score(self):
        return self.views * self.time_factor() * self.positivity_factor()
        
    
        