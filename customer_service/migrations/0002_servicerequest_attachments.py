# Generated by Django 5.0.6 on 2024-06-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='service_request_attachments/'),
        ),
    ]