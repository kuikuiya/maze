# Generated by Django 2.2.6 on 2019-12-05 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0004_auto_20191205_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('max_health_point', models.IntegerField(default='4')),
                ('health_point', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('attack_bonus', models.IntegerField()),
                ('strength_bonus', models.IntegerField()),
                ('dexterity_bonus', models.IntegerField()),
                ('intelligence_bonus', models.IntegerField()),
                ('spells', models.TextField(default='')),
                ('habitat', models.IntegerField()),
                ('monster_type', models.CharField(default='', max_length=20)),
                ('body_features', models.CharField(default='', max_length=20)),
                ('traits', models.CharField(default='', max_length=20)),
                ('ablity', models.CharField(default='', max_length=20)),
                ('tactics', models.CharField(default='', max_length=20)),
                ('personality', models.CharField(default='', max_length=20)),
                ('weakness', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitat', models.IntegerField()),
                ('word', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NPCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('max_health_point', models.IntegerField(default='4')),
                ('health_point', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('attack_bonus', models.IntegerField()),
                ('strength_bonus', models.IntegerField()),
                ('dexterity_bonus', models.IntegerField()),
                ('intelligence_bonus', models.IntegerField()),
                ('spells', models.TextField(default='')),
                ('hometown', models.CharField(default='', max_length=20)),
                ('asset', models.CharField(default='', max_length=20)),
                ('weakness', models.CharField(default='', max_length=20)),
                ('aim', models.CharField(default='', max_length=20)),
                ('misfortune', models.CharField(default='', max_length=20)),
                ('mission', models.CharField(default='', max_length=20)),
                ('method', models.CharField(default='', max_length=20)),
                ('appearance', models.CharField(default='', max_length=20)),
                ('body_features', models.CharField(default='', max_length=20)),
                ('getsup', models.CharField(default='', max_length=20)),
                ('fame', models.CharField(default='', max_length=20)),
                ('habit', models.CharField(default='', max_length=20)),
                ('relationship', models.CharField(default='', max_length=20)),
                ('divinity', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_effect', models.CharField(default='', max_length=20)),
                ('material_element', models.CharField(default='', max_length=20)),
                ('material_form', models.CharField(default='', max_length=20)),
                ('spiritual_effect', models.CharField(default='', max_length=20)),
                ('spiritual_elelment', models.CharField(default='', max_length=20)),
                ('spiritual_form', models.CharField(default='', max_length=20)),
                ('mutation', models.CharField(default='', max_length=20)),
                ('madness', models.CharField(default='', max_length=20)),
                ('magical_disaster', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='AerialAnimal',
        ),
        migrations.DeleteModel(
            name='GroundAnimal',
        ),
        migrations.DeleteModel(
            name='UnderwaterAnimal',
        ),
        migrations.AddField(
            model_name='character',
            name='spells',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='character',
            name='appearance',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='beloings',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='body_features',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='features',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='getsup',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='habit',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='health_point',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='personality',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon',
            field=models.CharField(default='', max_length=20),
        ),
    ]
