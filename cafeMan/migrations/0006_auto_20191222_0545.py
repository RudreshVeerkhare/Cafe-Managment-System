# Generated by Django 3.0.1 on 2019-12-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeMan', '0005_auto_20191222_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='otp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=4.4, max_digits=2),
        ),
        migrations.AlterField(
            model_name='orders',
            name='etp',
            field=models.CharField(max_length=100),
        ),
    ]
