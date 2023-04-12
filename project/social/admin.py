from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

admin.site.register(Link, LinkAdmin)