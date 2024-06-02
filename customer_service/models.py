from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ServiceRequest(models.Model):

    INSTALLATION = 'Installation'
    MAINTENANCE = 'Maintenance'
    REPAIR = 'Repair'
    INSPECTION = 'Inspection'
    ENERGY_AUDIT = 'Energy Audit'
    
    REQUEST_TYPE_CHOICES = [
        (INSTALLATION, 'Installation'),
        (MAINTENANCE, 'Maintenance'),
        (REPAIR, 'Repair'),
        (INSPECTION, 'Inspection'),
        (ENERGY_AUDIT, 'Energy Audit'),
    ]
    
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachments = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
   

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
