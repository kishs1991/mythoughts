from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserTable(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    status = models.CharField(max_length=100)
    group = models.CharField(max_length=250)


class GroupTable(models.Model):
    groupName = models.CharField(max_length=250)
    status = models.CharField(max_length=100)
    numberOfMembers = models.IntegerField()


class ThoughtTable(models.Model):
    username = models.CharField(max_length=250)
    thoughtText = models.TextField()
    lastUpdateTime = models.DateTimeField()
    md5HashOfText = models.TextField()
    hashTag = models.TextField()