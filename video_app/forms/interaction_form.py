# -*- encoding: utf-8 -*-

from django import forms

from video_app.models.interaction import Thumb, Comment


class InteractionForm(forms.ModelForm):
    class Meta:
        abstract = True
    
class ThumbForm(InteractionForm):
    class Meta:
        model = Thumb
        fields = ('video', 'is_positive', 'time')

class CommentForm(InteractionForm):
    class Meta:
        model = Comment
        fields = ('video', 'is_positive', 'time' )