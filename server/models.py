from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class NodeRegistration(models.Model):
    ipAddress = models.CharField(max_length=32)
    couchReplication = models.BooleanField()
    ipfsReplication = models.BooleanField()

class UserRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    publicKey = models.TextField(unique=True)

class Permission(models.Model):
    medblockId = models.CharField(max_length=200)
    user = models.ForeignKey(UserRegistration, models.CASCADE, 'permissions')
    granted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user','medblockId')
    def email(self):
        return self.user.email

class SyncParameters(models.Model):
    seq = models.TextField()
    lock1 = models.BooleanField(default=False)
    lock2 = models.BooleanField(default=False)