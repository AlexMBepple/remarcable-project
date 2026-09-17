from django.contrib import admin
from django.urls import path
from catalog.views import home, products_api, tags_api, categories_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', products_api, name='products_api'),
    path('api/tags/', tags_api, name='tags_api'),
    path('api/categories/', categories_api, name='categories_api'),
    path('', home, name='home'),
]