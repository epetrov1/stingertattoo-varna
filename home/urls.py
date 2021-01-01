from django.urls import path
from .views import home, anal


urlpatterns = [
    path('', home, name="home-page"),
    path('anal/', anal, name="anal"),
]
