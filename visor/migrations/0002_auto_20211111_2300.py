# Generated by Django 3.2.9 on 2021-11-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distritosmodel',
            name='id_manzana',
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='dens_pob',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='f0_a_14',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='f15_a_29',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='f30_a_59',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='f60_a_mas',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='hombre',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='mujer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='n_riesgo',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='pob_midis',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='pob_nbi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_30_a_59',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_densid',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_mcalor',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_mercado',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_pob60',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='q_propnbi',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='distritosmodel',
            name='ubigeo',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
