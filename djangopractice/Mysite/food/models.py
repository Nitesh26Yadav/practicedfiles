from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default="https://th.bing.com/th/id/R.861d624cb303db96322dcaeb6ed99e9b?rik=CstlEO2%2fm6Xy4w&riu=http%3a%2f%2fthefooddisciple.com%2fwp-content%2fuploads%2f2015%2f09%2fneptune-placeholder-40.jpg&ehk=oOphLDO0j3MFugqqnhbpZY5C1OyvfNcEvqRdyVpkIzk%3d&risl=&pid=ImgRaw&r=0")
