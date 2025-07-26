from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'profile_picture_preview', 'is_staff')

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:contain;" />',
                obj.profile_picture.url
            )
        return "No Image"

    profile_picture_preview.short_description = 'Profile picture preview'

admin.site.register(CustomUser, CustomUserAdmin)