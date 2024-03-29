from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'username', 'first_name', 'otchestvo', 'image',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff', 'otchestvo', 'image',)
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff', 'otchestvo', 'image',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'otchestvo', 'image',)}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
