from django.db import models

# Create your models here.


class Products(models.Model):
     product = models.CharField(max_length=50)
     price = models.DecimalField(decimal_places=2, max_digits=6)
     description = models.TextField(default='Info for products')
    # image = models.ImageField(upload_to="products", default="products")

     def __str__(self):
          return self.product


class Category(models.Model):
          type = models.CharField(max_length=50)
          gender = models.CharField(max_length=50)
          size = models.IntegerField()

          image = models.ImageField(upload_to="type", default="type")

          def __str__(self):
               return self.type


class Order(models.Model):
               category = models.CharField(max_length=50)
               price = models.DecimalField(decimal_places=2, max_digits=6)
               description = models.TextField(default='orderItems')

               #image = models.ImageField(upload_to="products", default="products")

               def __str__(self):
                    return self.category


class User(models.Model):
                    name = models.CharField(max_length=50)
                    age = models.IntegerField()
                    location = models.TextField(default='my location')

                    image = models.ImageField(upload_to="my profile", default="my profile")

                    def __str__(self):
                         return self.name