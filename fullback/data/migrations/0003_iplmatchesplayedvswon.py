# Generated by Django 3.2.12 on 2022-02-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20220220_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iplmatchesplayedvswon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('teamname', models.CharField(max_length=40)),
                ('teamabbr', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('matchesplayed', models.IntegerField()),
                ('matcheswon', models.IntegerField()),
            ],
        ),
    ]
