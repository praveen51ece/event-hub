from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth import hashers


class Events(models.Model):
    eve_id = models.IntegerField(db_column='eve_id', primary_key=True, blank=True, null=False)
    eve_name = models.CharField(db_column='eve_name', max_length=50,) 
    eve_location = models.CharField(db_column='eve_location',max_length=100)    
    eve_date = models.DateTimeField(db_column='eve_date')
    eve_entry_fee = models.IntegerField(db_column='eve_entry_fee')
    eve_discription = models.CharField(db_column='eve_discription', max_length=900, blank=True)
    eve_isused = models.IntegerField(default=0)   

    class Meta:
        managed = False
        db_table = 'Events'

class User(models.Model):
    use_id = models.IntegerField(db_column='use_id', primary_key=True, blank=True, null=False)
    use_name = models.CharField(db_column='use_name', max_length=50,) 
    use_email = models.CharField(db_column='use_email',max_length=100)    
    use_mobile = models.CharField(db_column='use_mobile', max_length=16,)
    use_Address = models.CharField(db_column='use_Address', max_length=100,)
    use_pwd = models.CharField(max_length=100, blank=True, help_text='0')
    use_login_id = models.CharField(db_column='use_login_id', max_length=50,) 
    use_isused = models.IntegerField(default=0)   

    class Meta:
        managed = False
        db_table = 'user'

    def set_password(self, password):
        try:
            self.use_pwd = hashers.make_password(password)
            return True
        except:
            return False

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













