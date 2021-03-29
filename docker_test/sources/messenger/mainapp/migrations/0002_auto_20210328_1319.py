# Generated by Django 2.2 on 2021-03-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialogmemebers',
            name='role',
            field=models.CharField(choices=[('0', 'создатель'), ('1', 'собеседник')], db_index=True, max_length=64, verbose_name='роль'),
        ),
    ]