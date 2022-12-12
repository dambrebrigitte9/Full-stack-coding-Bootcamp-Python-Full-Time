# Generated by Django 4.1.4 on 2022-12-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('url', models.URLField(default='admin@default.com', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('detail', models.CharField(max_length=30)),
                ('has_been_done', models.BooleanField(default=False)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_completion', models.DateField(auto_now_add=True)),
                ('deadline_date', models.DateField(auto_now_add=True)),
                ('catégorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.categorie')),
            ],
        ),
    ]
