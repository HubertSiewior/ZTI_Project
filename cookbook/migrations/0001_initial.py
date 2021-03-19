# Generated by Django 3.1.7 on 2021-03-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=25)),
                ('average_time', models.IntegerField()),
                ('average_price', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'High')], default='Medium', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('time', models.IntegerField(default=0)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('kcal', models.IntegerField()),
                ('quantity', models.FloatField()),
                ('if_vegan', models.BooleanField(default=False)),
                ('recipe_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipestep')),
            ],
        ),
    ]