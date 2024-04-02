from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Adjust max_length as needed
    categories = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=100)

class ChatGroup(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserProfile)

    def is_full(self):
        return self.users.count() >= 2 and self.users.count() <= 5
