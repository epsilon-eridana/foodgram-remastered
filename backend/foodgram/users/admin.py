from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    ordering = ('email',)
    search_fields = ('username', 'email', 'last_name')
    list_filter = ('username', 'email', 'first_name', 'last_name')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )
    list_filter = ('user', 'author')
    search_fields = ('user__username', 'user__email')


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Follow, SubscriptionAdmin)
