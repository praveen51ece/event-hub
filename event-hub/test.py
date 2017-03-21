/home/planmytour/events/static
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Events(models.Model):
    eve_id = models.IntegerField(primary_key=True)
    eve_name = models.CharField(max_length=50)
    eve_location = models.CharField(max_length=50)
    eve_date = models.CharField(max_length=30)
    eve_entry_fee = models.IntegerField(blank=True, null=True)
    eve_discription = models.CharField(max_length=900)
    eve_isused = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Events'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class User(models.Model):
    use_id = models.IntegerField(primary_key=True)
    use_name = models.CharField(max_length=50)
    use_email = models.CharField(max_length=50)
    use_mobile = models.IntegerField()
    use_address = models.CharField(db_column='use_Address', max_length=100)  # Field name made lowercase.
    use_isused = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
