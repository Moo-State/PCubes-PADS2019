# Generated by Django 2.2.1 on 2019-06-18 10:58

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import slice_dice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('import_xes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', djongo.models.fields.EmbeddedModelField(model_container=slice_dice.models.DimensionRestriction, null=True)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_xes.Dimension')),
            ],
        ),
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values', djongo.models.fields.ArrayModelField(model_container=slice_dice.models.DimensionRestriction)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_xes.Dimension')),
            ],
        ),
    ]