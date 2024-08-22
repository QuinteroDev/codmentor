# Generated by Django 5.1 on 2024-08-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='user',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='difficulty',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='language',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]