from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')  # Customize the fields displayed in the admin list view
    actions = ['mark_as_pending', 'mark_as_in_progress', 'mark_as_completed', 'mark_as_canceled']

    def mark_as_pending(self, request, queryset):
        queryset.update(status='Pending')

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='In-Progress')

    def mark_as_completed(self, request, queryset):
        queryset.update(status='Completed')

    def mark_as_canceled(self, request, queryset):
        queryset.update(status='Canceled')

# Register the ServiceRequest model with the custom admin class
admin.site.register(ServiceRequest, ServiceRequestAdmin)
