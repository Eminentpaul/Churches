from django.contrib import admin
from .models import User, Artist, Album, Song, Sermon, Testimony, MusicFavorite
# Register your models here.

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Sermon)
admin.site.register(Testimony)
admin.site.register(MusicFavorite)