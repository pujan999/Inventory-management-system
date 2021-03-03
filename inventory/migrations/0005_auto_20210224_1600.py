# Generated by Django 3.1.5 on 2021-02-24 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210224_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesentryform',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.purchaseentryform'),
        ),
        migrations.AlterField(
            model_name='salesreturnentryform',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.purchaseentryform'),
        ),
    ]