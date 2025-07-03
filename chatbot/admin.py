from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'session_id', 'message', 'response', 'created_at']
    list_filter = ['created_at']
    search_fields = ['message', 'response']