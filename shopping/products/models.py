from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100, unique=True)


    def __str__(self):
        return '{}'.format(self.name)

    

class products(models.Model):
    name=models.CharField(max_length=255,unique=True)
    # slug=models.SlugField(max_length=255,unique=True)
    price=models.FloatField()
    desc=models.TextField()
    image=models.ImageField(upload_to='pictures')
    stock=models.IntegerField()
    available=models.BooleanField()
    cate=models.ForeignKey(category, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return '{}'.format(self.name)  #to display the object name in admin panal


class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class cartitem(models.Model):
    product=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cartid=models.ForeignKey(cart, on_delete=models.CASCADE,null=True,blank=True)

class checkout(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    paymenttype = models.IntegerField(default=0)#1= credit card  2=Debit card 3=paypal






  