# Generated by Django 3.0 on 2019-12-04 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('anio_lanzamiento', models.IntegerField()),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Compania')),
            ],
        ),
        migrations.AddField(
            model_name='juego',
            name='compania',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Compania'),
        ),
    ]