from django.db import models
from django.contrib.auth.models import AbstractUser
USER_TYPE_CHOICES = (
     ('seller', 'seller'),
     ('buyer', 'buyer'),
)
class User(AbstractUser):
    user_type = models.CharField(max_length=40,choices=USER_TYPE_CHOICES)

# Create your models here.
# class ShopOwner(models.Model):
#
#     firstname = models.CharField(max_length=10)
#     lastname = models.CharField(max_length=10)
#     username = models.CharField(max_length=20,unique=True,blank=False)
#     email = models.EmailField(unique=True,blank=False)
#     password = models.CharField()
#     Seller = models.BooleanField()
#
#
#
class Ingredients(models.Model):
    #id = models.IntegerField(primary_key=True)
    ingredient = models.CharField(max_length=20,unique=True)
    quantity = models.IntegerField(blank=False)
    class Meta:
        verbose_name_plural = "Ingredients"
    def __str__(self):
        return self.ingredient
#
#
class Products(models.Model):
    product_name = models.CharField(max_length=20,unique=True,blank=False)
    i1 = models.ForeignKey(Ingredients,blank=True,null=True ,on_delete=models.CASCADE,related_name='i1',verbose_name='Ingredients')
    i2 = models.ForeignKey(Ingredients,blank=True,null=True ,on_delete=models.CASCADE,related_name='i2',verbose_name='Ingredients')
    i3 = models.ForeignKey(Ingredients,blank=True,null=True ,on_delete=models.CASCADE,related_name='i3',verbose_name='Ingredients')
    i4 = models.ForeignKey(Ingredients,blank=True,null=True ,on_delete=models.CASCADE,related_name='i4',verbose_name='Ingredients')
    i5 = models.ForeignKey(Ingredients,blank=True,null=True ,on_delete=models.CASCADE,related_name='i5',verbose_name='Ingredients')

    cost = models.IntegerField(blank=False)
    Selling_price = models.IntegerField(blank=False)

    def __str__(self):
        return self.product_name



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),

    )

    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS)