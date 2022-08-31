from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Юзер', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

