# No models in this example, but keep file for Django app completeness.
from django.contrib import admin
from .models import GoogleBotVisit , NormalVisit

@admin.register(GoogleBotVisit)
class GoogleBotVisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path_accessed', 'timestamp')
    search_fields = ('ip_address', 'user_agent')
    
@admin.register(NormalVisit)
class GoogleBotVisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path_accessed', 'timestamp')
    search_fields = ('ip_address', 'user_agent')    