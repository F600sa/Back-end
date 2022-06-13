from django.db import models
from django.contrib.auth.models import User

class Product_Model(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    #photo = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Profile(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=256)
    education = models.CharField(max_length=256)
    abstract = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CommentModel(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ReviewModel(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    Product = models.ForeignKey(Product_Model, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)