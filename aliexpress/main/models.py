from django.db import models

class AliSubmission(models.Model):
    product = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    rating = models.CharField(max_length=10)
    sold = models.CharField(max_length=10)
    shipping = models.CharField(max_length=10, default="-")
    date = models.DateTimeField(auto_now_add=True)
    search = models.CharField(max_length=250, default="BLANK")


    def __str__(self):
        return self.product
