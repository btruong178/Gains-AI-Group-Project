# Generated by Django 5.0.3 on 2024-04-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_prompt_age_prompt_duration_prompt_fitness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='typeofworkout',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
