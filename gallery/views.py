from django.shortcuts import render
from .models import Gallery
from django.urls import reverse
from django.views.generic import ListView
from django.core import serializers


class GalleryView(ListView):
    model = Gallery
    order_by = ['-day_publish']


""" class GallerySlideView(ListView):
    model = Gallery
    template_name = "gallery/gallery_slide.html" """

def slide_show_view(request, *args, **kwargs):
    all_images = Gallery.objects.all()
    choosen_image = Gallery.objects.get(**kwargs)
    image_id = choosen_image.id

    context = {
        'all_images': all_images,
        'choosen_image': choosen_image,
        'image_id': image_id
    }
    return render(request, "gallery/gallery_slide.html", context)