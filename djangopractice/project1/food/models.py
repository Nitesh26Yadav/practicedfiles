from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()


class favoriteItem(models.Model):

    def __str__(self):
        return self.favorite_item_name

    favorite_item_name = models.CharField(max_length=200)
    favorite_item_desc = models.CharField(max_length=200)
    favorite_item_price = models.IntegerField()
    favorite_item_quantity = models.IntegerField()
