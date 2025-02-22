from django.db import models
from pyuploadcare.dj.models import ImageField 

class GalleryItem(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/', blank=True)
    photo = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.caption
    
    def save(self, *args, **kwargs):
        # Check if the photo field has changed
        if self.pk:
            original = GalleryItem.objects.get(pk=self.pk)
            if original.photo != self.photo and not self.photo:
                self.photo = original.photo

        super(GalleryItem, self).save(*args, **kwargs)
    
    

class GuestMessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class TimelineEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    extra_details = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, default="fas fa-star")

    def __str__(self):
        return f"{self.title}"