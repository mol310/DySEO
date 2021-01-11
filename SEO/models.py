from django.db import models
from django.utils import timezone
import django
import datetime


# Create your models here.

class keyword_table(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    main_keyword = models.CharField(max_length=100, null=True)
    meta_keyword = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    review_count = models.CharField(max_length=100, null=True)
    buy_count = models.CharField(max_length=100, null=True)
    registration_date = models.CharField(max_length=100, null=True)
    dib_count = models.CharField(max_length=100, null=True)
    link = models.TextField(null=True)
