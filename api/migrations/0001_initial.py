# Generated by Django 4.1.3 on 2022-11-18 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('header', models.CharField(max_length=256, verbose_name='Цвета одежды на голове')),
                ('torso', models.CharField(max_length=256, verbose_name='Цвета одежды на торсе')),
                ('legs', models.CharField(max_length=256, verbose_name='Цвета одежды ног')),
                ('patronymic', models.CharField(max_length=256, verbose_name='Отчество')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('male', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=256, verbose_name='Пол')),
                ('nationality', models.CharField(max_length=256, verbose_name='Национальность')),
                ('kid', models.BooleanField(blank=True, default=None, null=True, verbose_name='Ребенок')),
                ('animal', models.BooleanField(blank=True, default=None, null=True, verbose_name='Животное')),
                ('is_moderator', models.BooleanField(blank=True, default=False, verbose_name='Модерирование')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleCart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('count', models.IntegerField(verbose_name='Счет')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('cloth', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет товара (одежды)')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='ID категории')),
            ],
        ),
        migrations.CreateModel(
            name='Preferencies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('degree', models.IntegerField(verbose_name='Степень важности')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='ID категории')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
        ),
    ]
