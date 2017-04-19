# -*- encoding: utf-8 -*-
from django.shortcuts import render

from video_app.models.theme import Theme


def get_popular_themes(request):
    themes = sorted(Theme.objects.all(),key=lambda theme: theme.score(), reverse=True)
    
    
    
    
    return render(request, 'rankings/themes.html', {'rows':themes})
