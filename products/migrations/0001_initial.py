# Generated by Django 4.2.9 on 2024-01-17 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.TextField(verbose_name='Opis')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category', verbose_name='Kategoria rodzic')),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Nazwa')),
                ('description', models.TextField(verbose_name='Opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Kategoria')),
            ],
            options={
                'verbose_name_plural': 'Produkty',
            },
        ),
    ]
