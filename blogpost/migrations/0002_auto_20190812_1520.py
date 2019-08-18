# Generated by Django 2.2.1 on 2019-08-12 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEOInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=64)),
                ('title', models.TextField(max_length=100)),
                ('url', models.CharField(max_length=64)),
                ('seotitle', models.TextField(max_length=100)),
                ('seodescription', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='')),
                ('keyword', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='editorinformation',
            name='status',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='image',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='seodescription',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='seotitle',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='status',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='title',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='url',
        ),
        migrations.RemoveField(
            model_name='writerinformation',
            name='status',
        ),
        migrations.AddField(
            model_name='writerinformation',
            name='writtentime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='editorinformation',
            name='topicname',
        ),
        migrations.RemoveField(
            model_name='researchinformation',
            name='topicname',
        ),
        migrations.RemoveField(
            model_name='writerinformation',
            name='topicname',
        ),
        migrations.AddField(
            model_name='editorinformation',
            name='topicname',
            field=models.ManyToManyField(to='blogpost.SEOInformation'),
        ),
        migrations.AddField(
            model_name='researchinformation',
            name='topicname',
            field=models.ManyToManyField(to='blogpost.SEOInformation'),
        ),
        migrations.AddField(
            model_name='writerinformation',
            name='topicname',
            field=models.ManyToManyField(to='blogpost.SEOInformation'),
        ),
    ]