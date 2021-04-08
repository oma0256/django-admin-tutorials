from django.contrib import admin, messages

from djangoadmin.apps.user_info.models import UserInfo
from djangoadmin.apps.user_info.utils import duplicate_model_instance


def duplicate_user_info(modeladmin, request, queryset):
    for user_info in queryset:
        duplicate_model_instance(user_info)
    message = 'Created duplicates for the user info.'
    modeladmin.message_user(request, message, messages.SUCCESS)

duplicate_user_info.short_description = 'Duplicate selected instances'


class UserInfoAdmin(admin.ModelAdmin):
    readonly_fields = ['username', 'email']
    list_display = [
        'username', 'name', 'email', 'phone_number', 'gender'
    ]
    search_fields = [
        'username', 'first_name', 'last_name', 
        'email', 'phone_number'
    ]
    list_filter = ['country', 'gender']
    actions = [duplicate_user_info]

    def name(self, user_info):
        return f'{user_info.first_name} {user_info.last_name}'


admin.site.register(UserInfo, UserInfoAdmin)
