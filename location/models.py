from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=48, verbose_name='عنوان', db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    @property
    def main_image(self):
        if self.picture.exists():
            return self.picture.first()
        else:
            return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "سالن"
        verbose_name_plural = "سالن ها"


class Chair(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='میز', related_name='loc')
    title = models.CharField(max_length=48, verbose_name='عنوان', db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "میز"
        verbose_name_plural = "میز ها"


class LocationImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='میز', related_name='picture')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('display_order',)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        for index, image in enumerate(self.location.picture.all()):
            image.display_order = index
            image.save()
