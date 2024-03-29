# Generated by Django 2.2 on 2019-07-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertiseContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Branding', 'Branding'), ('UI', 'UI'), ('Web development', 'Web development'), ('Mobile development', 'Mobile development'), ('Frontend & Backend', 'Frontend & Backend'), ('Ecommerce', 'Ecommerce'), ('IT & Startups Consulting', 'IT & Startups Consulting'), ('SEO', 'SEO'), ('Digital Marketing', 'Digital Marketing'), ('White Label', 'White Label')], max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
