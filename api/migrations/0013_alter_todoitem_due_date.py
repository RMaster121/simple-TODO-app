# Generated by Django 4.0.6 on 2022-08-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_listitem_todo_item_alter_todoitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(default=None, null=True),
        ),
    ]