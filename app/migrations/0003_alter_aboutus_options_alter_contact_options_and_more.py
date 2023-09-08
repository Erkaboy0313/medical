# Generated by Django 4.2.1 on 2023-05-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_qvp_qvptranslation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['-id'], 'verbose_name_plural': 'AboutUs'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/'),
        ),
    ]
