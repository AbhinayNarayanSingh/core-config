from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.apps import apps

# app = apps.get_app_config('user')

# for model_name, model in app.models.items():
#     admin.site.register(model)



class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-is_staff','is_active',)
    list_display = ('email', 'pk','name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
# admin.site.register(User)