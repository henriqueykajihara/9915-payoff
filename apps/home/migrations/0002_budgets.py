# Generated by Django 3.2.16 on 2022-11-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('codigo_categoria', models.IntegerField()),
                ('codigo_banco', models.IntegerField()),
                ('codigo_fornecedor', models.IntegerField()),
                ('valor_estimado', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
    ]