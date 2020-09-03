from django.contrib import admin

from . import models

# Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'email_validated', 'first_name', 'last_name')
#     search_fields = ['user', 'email_validated', 'first_name', 'last_name']
#     ordering = ['last_name']
#     list_filter = ['active']
#     date_hierarchy = 'created_on'

# admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Registration)