from django.contrib import admin
from .models import Project, Document, Message
from services.models import  OrderedService

admin.site.register(OrderedService)
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(Message)
