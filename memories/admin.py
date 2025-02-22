from django.contrib import admin

# Register your models here.
from .models import TimelineEvent, GalleryItem, GuestMessage

admin.site.register(TimelineEvent)
admin.site.register(GalleryItem)    
admin.site.register(GuestMessage)
