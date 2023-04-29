# Generated by Django 4.1.7 on 2023-03-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('cost', models.FloatField()),
                ('weight', models.IntegerField()),
                ('date_of_trans', models.DateField(auto_now=True)),
            ],
        ),
    ]