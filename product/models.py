from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name',
                         unique_with=['name'], unique=True)
                         
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title'], unique=True)
    product_image = models.ImageField(upload_to='product_images/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


