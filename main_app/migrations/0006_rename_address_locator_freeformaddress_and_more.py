# Generated by Django 4.1 on 2022-08-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_review_remove_locator_rating_remove_locator_reviews_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locator',
            old_name='address',
            new_name='freeformAddress',
        ),
        migrations.RemoveField(
            model_name='locator',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='locator',
            name='location',
        ),
        migrations.AddField(
            model_name='locator',
            name='countrySubdivision',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locator',
            name='municipality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locator',
            name='shopId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locator',
            name='streetName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locator',
            name='streetNumber',
            field=models.CharField(max_length=100, null=True),
        ),
    ]