# Generated by Django 4.2.1 on 2023-07-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('total', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('addresse', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=300)),
                ('zipcode', models.CharField(max_length=300)),
                ('date_commande', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='catergory',
            new_name='category',
        ),
    ]
