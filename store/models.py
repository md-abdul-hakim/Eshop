from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='category', default='demo/demo.jpg', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created', ]
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Short Descriptions')
    description = models.TextField(max_length=1000, verbose_name='Descriptions')
    image = models.ImageField(upload_to='products', default='demo/demo.jpg', blank=False, null=False)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def get_product_url(self):
        return reverse('store:product-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation='size')
    def colors(self):
        return super(VariationManager, self).filter(variation='color')

VARIATIONS_TYPE = (
    ('size', 'size'),
    ('color', 'color'),
)

class VariationValue(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.name

class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    image = models.ImageField(upload_to='banner')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class MyLogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 150 or img.height > 150:
            output_size=(150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return str(self.image)

class MyFavicon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 100 or img.height >100:
            output_size=(100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return str(self.image)
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    review_number = models.IntegerField()
    def __str__(self):
        return self.subject
    
class Brand(models.Model):
    BRAND_TYPE = (
        ('national', 'National'),
        ('multi-national', 'Multi-National')
    )
    name = models.CharField(max_length=100)
    brand_logo = models.ImageField(upload_to = 'brand_logo')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_type = models.CharField(max_length=100, choices=BRAND_TYPE, default='National')
    
    def __str__(self):
        return self.name