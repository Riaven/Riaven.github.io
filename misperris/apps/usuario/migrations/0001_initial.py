# Generated by Django 2.1.3 on 2018-11-21 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('run', models.CharField(max_length=10)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('telefono', models.CharField(max_length=14)),
                ('region', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('tipo_vivienda', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuario.TipoVivienda')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
