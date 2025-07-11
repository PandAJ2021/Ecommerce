from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ('phone',)
    list_display = ('phone', 'email', 'name', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('phone', 'email', 'name')
    filter_horizontal = ()

    fieldsets = (
        ('Login Info', {'fields': ('phone', 'password')}),
        ('Personal Info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('phone', 'email', 'name', 'password', 'password2', 'is_active', 'is_admin')}
        ),
    )


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
