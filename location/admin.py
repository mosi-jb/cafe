from django.contrib import admin

from location.models import Location, Chair, LocationImage


class chairInline(admin.StackedInline):
    model = Chair
    extra = 2


class ImageInline(admin.StackedInline):
    model = LocationImage
    extra = 2


# Register your models here.
@admin.register(Location)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [chairInline, ImageInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Chair)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(LocationImage)
