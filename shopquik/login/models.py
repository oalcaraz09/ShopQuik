from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser,  UserManager
from django.forms import ModelForm
# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=30)

    def __str__(self):
        return self.item_name

class List(models.Model):
    list_name = models.CharField(max_length=30)
    items = models.ManyToManyField(Item, null=True,blank=True)

    def __str__(self):
        return self.list_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lists = models.ForeignKey(List, on_delete=models.CASCADE,null=True, blank=True )

class Aisle(models.Model):
    number = models.IntegerField()
    items = models.ManyToManyField(Item)

class Store(models.Model):
    store_name = models.CharField(max_length=30)
    aisles = models.ForeignKey(Aisle, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

#create an associated profile everytime a user is created
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']
#
# class ItemForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['item_name']