from django.db import models

class Listing(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    no_bedroom=models.IntegerField()
    no_bathroom=models.IntegerField()
    square_photage=models.IntegerField()
    address =models.CharField(max_length=100)
    image=models.ImageField()

    def __str__(self):
        return self.title