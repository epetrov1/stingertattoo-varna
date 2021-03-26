from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=250)
    asnwer = models.TextField()

    def __str__(self):
        return self.question