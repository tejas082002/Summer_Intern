# Generated by Django 4.2.2 on 2023-06-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveclass', '0006_student_records_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_records',
            name='country',
            field=models.CharField(blank=True, choices=[('INDIA', 'INDIA'), ('OTHERS', 'OTHERS')], default='INDIA', max_length=50, null=True),
        ),
    ]