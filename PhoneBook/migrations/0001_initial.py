# Generated by Django 2.1.7 on 2019-04-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phonebook',
            fields=[
                ('phonebookid', models.IntegerField(db_column='phoneBookId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('phonenumber', models.IntegerField(blank=True, db_column='phoneNumber', null=True)),
            ],
            options={
                'db_table': 'PhoneBook',
                'managed': False,
            },
        ),
    ]
