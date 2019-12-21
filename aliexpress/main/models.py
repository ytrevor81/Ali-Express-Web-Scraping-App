from django.db import models

class AliSubmission(models.Model):
    product = models.CharField(max_length=250)
    price = models.FloatField()
    rating = models.FloatField()
    sold = models.IntegerField()
    epacket = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
