# Generated by Django 2.2.5 on 2019-10-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladnik',
            name='pizza',
        ),
        migrations.AddField(
            model_name='skladnik',
            name='pizze',
            field=models.ManyToManyField(related_name='skladniki', to='pizza.Pizza'),
        ),
        migrations.AlterField(
            model_name='skladnik',
            name='jarski',
            field=models.BooleanField(default=False, help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegeratian', verbose_name='jarski?'),
        ),
        migrations.AlterField(
            model_name='skladnik',
            name='nazwa',
            field=models.CharField(max_length=30, verbose_name='skladnik'),
        ),
    ]