# Generated by Django 4.2.4 on 2023-08-15 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='fotos/')),
                ('ordem', models.PositiveIntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='fotos.categoria')),
            ],
        ),
    ]
