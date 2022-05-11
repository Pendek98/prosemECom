# Generated by Django 4.0.3 on 2022-03-30 18:15

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
            name='aukcja',
            fields=[
                ('Nazwa', models.CharField(max_length=200)),
                ('Cena_kt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Cena_au', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Data_Zak', models.DateTimeField()),
                ('ID', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('Opis', models.TextField(max_length=1000)),
                ('Zakonczona', models.BooleanField(default=False)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('Wygrywajacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]