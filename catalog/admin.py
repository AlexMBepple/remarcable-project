from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')


admin.site.register(Category)
admin.site.register(Tag)