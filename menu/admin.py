from django.contrib import admin

from menu.models import Category, Product, CategoryImage


# Register your models here.


class ImageInline(admin.StackedInline):
    model = CategoryImage
    extra = 2


# Register your models here.
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


admin.site.register(CategoryImage)
admin.site.register(Product)
