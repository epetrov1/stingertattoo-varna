from django.urls import path, include
from .views import GalleryView
from . import views
""" path('slide/', GallerySlideView.as_view(), name="slide"), """

urlpatterns = [
    path('', GalleryView.as_view(), name="portfolio"),
    path('slug/<int:pk>/', views.slide_show_view, name="detail-slug"),  
]