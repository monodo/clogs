# Generated by Django 5.0.3 on 2024-06-04 05:59

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treeitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('name', models.CharField()),
                ('description', models.CharField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('type', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('action', models.CharField()),
                ('element_type', models.CharField(max_length=50)),
                ('element_id', models.IntegerField()),
                ('element_name', models.CharField()),
                ('element_url_table', models.CharField()),
                ('username', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='OgcServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('url', models.CharField()),
                ('url_wfs', models.CharField(blank=True, null=True)),
                ('type', models.CharField()),
                ('image_type', models.CharField()),
                ('auth', models.CharField()),
                ('wfs_support', models.BooleanField(blank=True, null=True)),
                ('is_single_tile', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('extent', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shorturl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, null=True)),
                ('ref', models.CharField(max_length=20, unique=True)),
                ('creator_email', models.CharField(blank=True, max_length=200, null=True)),
                ('creation', models.DateTimeField(blank=True, null=True)),
                ('last_hit', models.DateTimeField(blank=True, null=True)),
                ('nb_hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Functionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('value', models.CharField()),
                ('description', models.CharField(blank=True, null=True)),
                ('group', models.ManyToManyField(to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.treeitem')),
                ('public', models.BooleanField(blank=True, null=True)),
                ('geo_table', models.CharField(blank=True, null=True)),
                ('exclude_properties', models.CharField(blank=True, null=True)),
                ('interface', models.ManyToManyField(to='themes.interface')),
            ],
        ),
        migrations.CreateModel(
            name='Treegroup',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.treeitem')),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True)),
                ('value', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.treeitem')),
            ],
        ),
        migrations.CreateModel(
            name='Tsearch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, null=True)),
                ('layer_name', models.CharField(blank=True, null=True)),
                ('ts', models.TextField(blank=True, null=True)),
                ('the_geom', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(blank=True, null=True)),
                ('params', models.CharField(blank=True, null=True)),
                ('lang', models.CharField(blank=True, max_length=2, null=True)),
                ('actions', models.CharField(blank=True, null=True)),
                ('from_theme', models.BooleanField(blank=True, null=True)),
                ('interface', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='themes.interface')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='themes.role')),
            ],
        ),
        migrations.CreateModel(
            name='LayerVectortiles',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.layer')),
                ('style', models.CharField()),
                ('xyz', models.CharField(blank=True, null=True)),
                ('sql', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LayerWmts',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.layer')),
                ('url', models.CharField()),
                ('layer', models.CharField()),
                ('style', models.CharField(blank=True, null=True)),
                ('matrix_set', models.CharField(blank=True, null=True)),
                ('image_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restrictionarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('readwrite', models.BooleanField(blank=True, null=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('buffer', models.TextField(blank=True, null=True)),
                ('group', models.ManyToManyField(to='auth.group')),
                ('layer', models.ManyToManyField(to='themes.layer')),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True)),
                ('value', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('field', models.CharField(blank=True, null=True)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.layer')),
            ],
        ),
        migrations.CreateModel(
            name='Layergroup',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.treegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.treegroup')),
                ('icon', models.CharField(blank=True, null=True)),
                ('ordering', models.IntegerField()),
                ('public', models.BooleanField()),
                ('group', models.ManyToManyField(to='auth.group')),
                ('interface', models.ManyToManyField(to='themes.interface')),
            ],
        ),
        migrations.CreateModel(
            name='LayergroupTreeitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('treeitem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.treeitem')),
                ('treegroup', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.treegroup')),
            ],
        ),
        migrations.CreateModel(
            name='LayerWms',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.layer')),
                ('layer', models.CharField()),
                ('style', models.CharField(blank=True, null=True)),
                ('time_mode', models.CharField()),
                ('time_widget', models.CharField()),
                ('valid', models.BooleanField(blank=True, null=True)),
                ('invalid_reason', models.CharField(blank=True, null=True)),
                ('ogc_server', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.ogcserver')),
            ],
        ),
        migrations.CreateModel(
            name='ThemeFunctionality',
            fields=[
                ('theme', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='themes.theme')),
                ('functionality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='themes.functionality')),
            ],
            options={
                'unique_together': {('theme', 'functionality')},
            },
        ),
    ]
