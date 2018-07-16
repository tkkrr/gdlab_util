# Generated by Django 2.0.7 on 2018-07-15 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='journal',
        ),
        migrations.AddField(
            model_name='journal',
            name='fri',
            field=models.CharField(default='なし', max_length=100, verbose_name='金曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='mon',
            field=models.CharField(default='なし', max_length=100, verbose_name='月曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='satur',
            field=models.CharField(default='なし', max_length=100, verbose_name='土曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='sun',
            field=models.CharField(default='なし', max_length=100, verbose_name='日曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='thurs',
            field=models.CharField(default='なし', max_length=100, verbose_name='木曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='tues',
            field=models.CharField(default='なし', max_length=100, verbose_name='火曜日'),
        ),
        migrations.AddField(
            model_name='journal',
            name='wens',
            field=models.CharField(default='なし', max_length=100, verbose_name='水曜日'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='name',
            field=models.CharField(max_length=30, verbose_name='氏名'),
        ),
    ]
