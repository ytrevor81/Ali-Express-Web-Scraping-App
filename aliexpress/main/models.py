from django.db import models

class AliSubmission(models.Model):
    User = models.CharField(max_length=250, default="Ghost user...")
    Products = models.TextField()
    Prices = models.TextField()
    Ratings = models.TextField()
    Sold = models.TextField()
    Suppliers = models.TextField(default="N/A")
    Shipping = models.TextField(blank=True)
    Search = models.CharField(max_length=250, default="BLANK")
    Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.User + '---' + self.Search
