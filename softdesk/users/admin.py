from django.contrib import admin
from django.contrib.admin import register, ModelAdmin

from users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    pass
