from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'user_type')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'user_type')


class CustomAdmin(UserAdmin):  
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'password',  'user_type',)}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'user_type'),
        }),
    )
    list_display = ('username', 'user_type', 'email','uid')
    search_fields = ('email', 'first_name', 'last_name', 'username',)
    ordering = ('username',)




admin.site.register(CustomUser, CustomAdmin)








