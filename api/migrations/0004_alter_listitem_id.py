# Generated by Django 4.0.6 on 2022-08-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_todoitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
