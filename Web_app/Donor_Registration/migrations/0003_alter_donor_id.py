# Generated by Django 3.2 on 2021-04-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor_Registration', '0002_alter_donor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
