from django.contrib import admin

from .models import *

admin.site.register(Author)
admin.site.register(Music)
admin.site.register(Category)
admin.site.register(BestSong)