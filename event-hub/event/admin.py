from django.contrib import admin


# Register your models here.
#from models import User
from .models import *
admin.site.register(User)
#admin.site.register(ViewUserClientBusinessPlan)