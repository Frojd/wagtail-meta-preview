# Generated by Django 3.0.8 on 2020-07-30 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('app', '0003_twitterpage_og_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Og image'),
        ),
    ]
