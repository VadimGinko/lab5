# Generated by Django 3.0.3 on 2020-03-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('RegDate', models.DateTimeField()),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=30)),
            ],
        ),
    ]
