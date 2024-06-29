from django.contrib import admin
from .models import PediaObject,UserAdmin,UserPedia
# Register your models here.
admin.site.register(PediaObject)
admin.site.register(UserAdmin)
admin.site.register(UserPedia)

