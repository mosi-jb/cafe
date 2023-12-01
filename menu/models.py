from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='عنوان')

    @property
    def main_image(self):
        if self.picture.exists():
            return self.picture.first()
        else:
            return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT)
    # price = models.PositiveBigIntegerField()
    # num_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ایتم"
        verbose_name_plural = "ایتم ها"


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='picture')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('display_order',)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        for index, image in enumerate(self.category.picture.all()):
            image.display_order = index
            image.save()
