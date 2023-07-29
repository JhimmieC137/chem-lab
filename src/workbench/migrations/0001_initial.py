# Generated by Django 3.2.12 on 2023-07-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apparatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('type', models.CharField(blank=True, max_length=250)),
                ('category', models.CharField(choices=[('GLASSWARE', 'Glassware'), ('TOOL', 'Tool')], default='GLASSWARE', max_length=50)),
                ('material', models.CharField(choices=[('WOOD', 'Wood'), ('METAL', 'Metal'), ('GLASS', 'Glass'), ('PLASTIC', 'Plastic')], default='GLASS', max_length=50)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('thermal_properties', models.TextField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('formula', models.CharField(blank=True, max_length=250)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('phValue', models.IntegerField(blank=True, null=True)),
                ('molarity', models.FloatField(blank=True, null=True)),
                ('thermal_properties', models.TextField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
