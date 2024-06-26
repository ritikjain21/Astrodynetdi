# Generated by Django 4.2.11 on 2024-04-23 09:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0004_homepage_about_description_homepage_about_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetailpage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MultipleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('part_number', models.CharField(max_length=250)),
                ('description', wagtail.fields.RichTextField()),
                ('output_voltage', models.CharField(max_length=250)),
                ('output_current', models.CharField(max_length=250)),
                ('output_power', models.CharField(max_length=250)),
                ('input_voltage_range', models.CharField(max_length=250)),
                ('isolation', models.CharField(max_length=250)),
                ('form_factor', models.CharField(max_length=250)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.document')),
                ('image', models.ForeignKey(blank=True, help_text='Products image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.productdetailpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
