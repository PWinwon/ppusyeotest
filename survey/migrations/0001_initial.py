# Generated by Django 3.2.8 on 2021-11-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(choices=[(1, '10대'), (2, '20대'), (3, '30대'), (4, '40대'), (5, '50대'), (6, '60대'), (7, '70대'), (8, '80대 이상')])),
                ('sex', models.CharField(choices=[('F', '여자'), ('M', '남자')], max_length=10)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('walk_cnt', models.IntegerField()),
                ('indoor', models.IntegerField(choices=[(1, '실내'), (0, '실외')])),
                ('alone', models.IntegerField(choices=[(1, '혼자'), (0, '같이')])),
                ('light', models.IntegerField(choices=[(1, '가볍게'), (0, '제대로')])),
            ],
        ),
    ]
