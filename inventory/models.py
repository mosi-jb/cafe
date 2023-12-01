from django.db import models


# Create your models here.

class StockRecord(models.Model):
    product = models.ForeignKey('menu.Product', on_delete=models.CASCADE, related_name='stockrecords')
    sale_price = models.PositiveBigIntegerField()
    num_stock = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.title} , {self.sale_price}'

    class Meta:
        verbose_name = "انبارداری"
        verbose_name_plural = "انبارداری ها"
