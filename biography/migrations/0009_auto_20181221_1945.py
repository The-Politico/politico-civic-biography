# Generated by Django 2.1.3 on 2018-12-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0008_financials_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupation',
            name='organization',
        ),
        migrations.AddField(
            model_name='occupation',
            name='employer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]