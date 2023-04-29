# Generated by Django 4.1.7 on 2023-03-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('cost', models.FloatField()),
                ('weight', models.IntegerField()),
                ('date_of_appear', models.DateField(auto_now=True)),
                ('power', models.FloatField()),
                ('capacity', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='my_Table',
        ),
    ]