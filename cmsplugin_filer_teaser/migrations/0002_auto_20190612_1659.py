# Generated by Django 2.0 on 2019-06-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_teaser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerteaser',
            name='style',
            field=models.CharField(blank=True, choices=[('default', 'Default'), ('drones', 'Drones'), ('news', 'News'), ('drone_news', 'Drone News'), ('about', 'About'), ('sustainability', 'Sustainability')], default='', max_length=255, verbose_name='Style'),
        ),
    ]
