# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('content', markupfield.fields.MarkupField(rendered_field=True)),
                ('content_markup_type', models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='markdown', editable=False, max_length=30)),
                ('_content_rendered', models.TextField(editable=False)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='MotivationFinishedCourseTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Course')),
            ],
        ),
        migrations.CreateModel(
            name='MotivationSharedCourseTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('originLanguageCode', models.CharField(default='en', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markupfield.fields.MarkupField(rendered_field=True)),
                ('correct_answer', models.CharField(max_length=200)),
                ('content_markup_type', models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='markdown', editable=False, max_length=30)),
                ('_content_rendered', models.TextField(editable=False)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Course')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Test'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Variation'),
        ),
        migrations.AddField(
            model_name='choice',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Student'),
        ),
        migrations.AddField(
            model_name='choice',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Variation'),
        ),
    ]
