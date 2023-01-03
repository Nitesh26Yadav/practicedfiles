from django.db import models

# Create your models here.
class grocery(models.Model):

    def __str__(self):
        return self.grocery_name

    grocery_name = models.CharField(max_length = 100)
    grocery_quantity = models.CharField(max_length=100)
    grocery_price = models.IntegerField()

    