from django.contrib import admin

from video_app.forms.interaction_form import ThumbForm, CommentForm
from video_app.forms.theme_form import ThemeForm
from video_app.forms.video_form import VideoForm
from video_app.models.interaction import Thumb, Comment
from video_app.models.theme import Theme
from video_app.models.video import Video


class VideoAdmin(admin.ModelAdmin):
    form = VideoForm

class ThemeAdmin(admin.ModelAdmin):
    form = ThemeForm

class ThumbAdmin(admin.ModelAdmin):
    form = ThumbForm
    
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm



admin.site.register(Theme, ThemeAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Thumb, ThumbAdmin)
admin.site.register(Comment, CommentAdmin)