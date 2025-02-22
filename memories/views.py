from django.shortcuts import render, redirect
from .models import GalleryItem, GuestMessage, TimelineEvent
from django.utils import timezone

def home(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            GuestMessage.objects.create(name=name, message=message, timestamp=timezone.now())
            success = True

    gallery_items = GalleryItem.objects.all()
    guest_messages = GuestMessage.objects.all().order_by('-timestamp')
    timeline_events = TimelineEvent.objects.all()
    return render(request, 'home.html', {
        'gallery_items': gallery_items,
        'guest_messages': guest_messages,
        'timeline_events': timeline_events,
        'success': success
    })
