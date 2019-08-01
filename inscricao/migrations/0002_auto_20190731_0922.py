# Generated by Django 2.0.2 on 2019-07-31 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inscricao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('professor', models.CharField(max_length=150)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='participante',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matricula',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscricao.Participante'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(on_delete=False, to='inscricao.Curso'),
        ),
    ]