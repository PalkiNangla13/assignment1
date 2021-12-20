from django.db import models
class ProductItem(models.Model):

    class ProductItem(models.Model):
        product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_vendor = models.CharField(max_length= 200)
    product_quantity = models.PositiveIntegerField()
    product_warranty = models.FloatField()

