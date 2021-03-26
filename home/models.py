from django.db import models

class HomePageTemplate(models.Model):
    header_1 = models.CharField(max_length=250)
    main_image = models.ImageField(upload_to="home_page")
    main_image_alt = models.CharField(max_length=250)
    stinger_about = models.TextField()
    stinger_logo = models.ImageField(upload_to="home_page")
    stinger_special_offer = models.TextField()
    stinger_special_offer_image = models.ImageField(upload_to="home_page")


    def __str__(self):
        return "This page have to be only one and edit only"
    