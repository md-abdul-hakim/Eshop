from django.db import models

# Create your models here.
class SiteContact(models.Model):
    banner = models.ImageField(upload_to='contact')
    banner_title = models.CharField(max_length=100)
    info_text = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    dial_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return self.banner_title
    
class UserContact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=70)
    message = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name

class FAQ(models.Model):
    STATUS = (
        ('False', 'False'),
        ('True', 'True')
    )
    CATEGORY = (
        ('payment', 'payment'),
        ('shipping', 'shipping'),
        ('order_and_return', 'order_and_return')
    )
    faq_order = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=500)
    status = models.CharField(max_length=150, choices=STATUS, default=False)
    category = models.CharField(max_length=100, choices=CATEGORY, default='payment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question
    
class AboutEshop(models.Model):
    heading = models.CharField(max_length=100)
    heading_span = models.CharField(max_length=100)
    vision_tittle = models.CharField(max_length=150)
    vision_description = models.CharField(max_length=1000)
    mission_tittle = models.CharField(max_length=150)
    mission_description = models.CharField(max_length=1000)
    shop_heading = models.CharField(max_length=150)
    shop_caption = models.CharField(max_length=250)
    shop_description = models.CharField(max_length=1000)
    about_img1 = models.ImageField(upload_to='about_eshop')
    about_img2 = models.ImageField(upload_to='about_eshop')
    about_banner = models.ImageField(upload_to='about_eshop')
    brands_text = models.CharField(max_length=250)
    brands_description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.heading
