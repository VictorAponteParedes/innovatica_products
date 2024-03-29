# Generated by Django 4.2.5 on 2023-09-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('nuevo', 'Nuevo'), ('semi_nuevo', 'Semi Nuevo'), ('usado', 'Usado')], default='nuevo', max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('categoria', models.ManyToManyField(related_name='products', to='store_products.categoria')),
            ],
        ),
    ]
