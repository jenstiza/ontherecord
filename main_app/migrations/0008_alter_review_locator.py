# Generated by Django 4.1 on 2022-08-18 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_review_locator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='locator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.locator'),
        ),
    ]