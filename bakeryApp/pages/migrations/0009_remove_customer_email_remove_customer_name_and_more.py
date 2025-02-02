# Generated by Django 5.0.4 on 2024-05-21 15:23

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_category_created_at_menu_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='review',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 23, 23, 1, 159345)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 23, 23, 1, 160346)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 23, 23, 1, 163347)),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 21, 23, 23, 1, 161346))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.customer')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.menu')),
            ],
        ),
    ]
