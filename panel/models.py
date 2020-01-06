# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Character(models.Model):

    hostname = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    yang = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
