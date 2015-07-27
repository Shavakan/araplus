from django.contrib import admin
from apps.session.models import UserProfile, Message


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'points')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'sender', 'receiver')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Message, MessageAdmin)
from apps.session.models import *

# Register your models here.
admin.site.register(UserProfile)
