# Generated by Django 2.2.3 on 2019-07-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=150)),
            ],
        ),
    ]