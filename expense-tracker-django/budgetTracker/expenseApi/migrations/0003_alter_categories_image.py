# Generated by Django 4.2.6 on 2024-05-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApi', '0002_alter_expense_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
