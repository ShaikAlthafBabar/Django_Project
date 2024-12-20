from django.contrib import admin
from watchlistApp.models import watchList,streamingPlatform,Review

# Register your models here.
admin.site.register(watchList)
admin.site.register(streamingPlatform)
admin.site.register(Review)
