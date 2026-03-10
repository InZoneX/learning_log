from django.contrib import admin

# Register your models here.
# http://localhost:8000/admin/

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)