from django.test import TestCase

# Create your tests here.
import uuid
 
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse
 
from .models import Category, Tag, Product
 
 
class CategoryModelTests(TestCase):
    def test_name_must_be_unique(self):
        Category.objects.create(name="Structural Materials")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Category.objects.create(name="Structural Materials")


class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Structural Materials")
        self.tag = Tag.objects.create(name="heavy-duty")

    def test_category_deletion_sets_null_instead_of_removing_product(self):
        product = Product.objects.create(name="Ready-Mix Concrete (Yard)", category=self.category)
        self.category.delete()
        product.refresh_from_db()
        self.assertIsNone(product.category)
        self.assertTrue(Product.objects.filter(pk=product.pk).exists())

    def test_tags_are_many_to_many(self):
        product = Product.objects.create(name="Ready-Mix Concrete (Yard)", category=self.category)
        other_tag = Tag.objects.create(name="bulk-pricing")
        product.tags.add(self.tag, other_tag)
 
        self.assertEqual(product.tags.count(), 2)
        self.assertIn(product, self.tag.products.all())
