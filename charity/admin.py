from django.contrib import admin
from .models import CustomUser
# zamienić na getusermodel

admin.site.register(CustomUser)
