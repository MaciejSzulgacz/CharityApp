from django.contrib import admin
from .models import Category, CustomUser, Donation, Institution
# zamienić na getusermodel

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Institution)
