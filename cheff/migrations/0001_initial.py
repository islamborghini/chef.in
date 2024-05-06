# Generated by Django 4.2.9 on 2024-05-04 05:23

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
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='uploads/product')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cheff.category')),
            ],
        ),
    ]