# Generated by Django 4.2.4 on 2023-09-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_alter_signup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
