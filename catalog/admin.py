from django.contrib import admin
from django.core.management import call_command
from django.shortcuts import redirect
from django.urls import path
from .models import Category, Tag, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/catalog/category/change_list.html'
    
    def get_urls(self):
        custom_urls = [
            path('seed-data/', self.admin_site.admin_view(self.seed_data), name='catalog_seed_data'),
        ]
        return custom_urls + super().get_urls()

    def seed_data(self, request):
        call_command('seed_data')
        self.message_user(request, "Sample data seeded successfully.")
        return redirect('..')

admin.site.register(Tag)