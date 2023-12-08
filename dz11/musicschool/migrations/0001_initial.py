# Generated by Django 4.2.6 on 2023-12-07 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('course', models.PositiveIntegerField()),
                ('instrument', models.CharField(choices=[('piano', 'piano'), ('violin', 'violin'), ('flute', 'flute'), ('accordion', 'accordion'), ('harp', 'harp')], max_length=255)),
                ('average_grade', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('payment', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255)),
            ],
        ),
    ]