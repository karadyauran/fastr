# Generated by Django 5.0.4 on 2024-04-22 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'db_table': 'cart_app_cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart_app_cartitem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'product_app_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=125)),
                ('location', models.CharField(max_length=100, null=True)),
                ('profile_photo', models.CharField(max_length=250, null=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'authenticate_app_userauth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='PENDING', max_length=15)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.userauth')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.product')),
            ],
        ),
    ]
