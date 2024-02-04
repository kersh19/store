from django.contrib import admin
from .models import Task
from .models import Product, AdditionalImage


class AdditionalImageInline(admin.StackedInline):
    model = AdditionalImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageInline]

admin.site.register(AdditionalImage)

admin.site.register(Task)
