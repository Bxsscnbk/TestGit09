# Generated by Django 5.0.3 on 2024-03-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('product_title', models.CharField(max_length=200)),
                ('product_unit', models.CharField(max_length=50)),
                ('display_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('description', models.CharField(max_length=250)),
                ('product_pic', models.CharField(blank=True, max_length=200)),
                ('created_by', models.CharField(default='Auto', max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='Auto', max_length=30)),
                ('void', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
    ]
