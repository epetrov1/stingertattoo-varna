from django.shortcuts import render

from . models import HomePageTemplate

def home(request):
    home_context = HomePageTemplate.objects.get(pk=1)
    context = {
        "home_context": home_context,
    }
    return render(request, "home/home.html", context)

