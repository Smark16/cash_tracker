# Generated by Django 4.2.6 on 2024-05-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApi', '0003_alter_categories_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
