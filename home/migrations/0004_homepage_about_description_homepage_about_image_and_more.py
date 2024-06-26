# Generated by Django 4.2.11 on 2024-04-21 11:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0003_applicantdetailpage_applicantpage_contactpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_title',
            field=models.CharField(blank=True, help_text='Write an about title for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='application_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='application_title',
            field=models.CharField(blank=True, help_text='Write an application title for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, help_text='Write an Banner title for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='left_demand_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='left_demand_image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='left_demand_title',
            field=models.CharField(blank=True, help_text='Write an left demand title for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='right_demand_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='right_demand_image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='right_demand_title',
            field=models.CharField(blank=True, help_text='Write an right demand for the site', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='solution_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='solution_title',
            field=models.CharField(blank=True, help_text='Write an solution title for the site', max_length=255),
        ),
    ]
