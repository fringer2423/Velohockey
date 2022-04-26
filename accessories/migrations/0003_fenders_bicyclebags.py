# Generated by Django 4.0.4 on 2022-04-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0002_delete_accessory_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('type', models.CharField(choices=[('Rear fenders for bicycle', 'Задние крылья для велосипеда'), ('Rear fenders for mountain bike', 'Задние крылья для горного велосипеда'), ('Fender kits for 26" bike', 'Комплекты крыльев для велосипеда 26 дюймов'), ('Mudguards 12″-18″ for bike', 'Крылья 12″-18″ для велосипеда'), ('Mudguards 20″ for bicycle', 'Крылья 20″ для велосипеда'), ('Mudguards 24″ for bicycle', 'Крылья 24″ для велосипеда'), ('Mudguards 26″ for bike', 'Крылья 26″ для велосипеда'), ('Mudguards 27.5″ for bike', 'Крылья 27.5″ для велосипеда'), ('Mudguards 28″ for bike', 'Крылья 28″ для велосипеда'), ('Mudguards 29″ for bike', 'Крылья 29″ для велосипеда'), ('Wings for Fatbike', 'Крылья для Fatbike'), ('Mudguards for 16 inch bike', 'Крылья для велосипеда 16 дюймов'), ('Fenders for bike Merida', 'Крылья для велосипеда Merida'), ('Mudguards for SKS 26" bike', 'Крылья для велосипеда SKS 26 дюймов'), ('Mudguards for bike Stels', 'Крылья для велосипеда Stels'), ('Mudguards for bike Stels 26 inches', 'Крылья для велосипеда Stels 26 дюймов'), ('MTB fenders', 'Крылья для горного велосипеда'), ('26" mountain bike fenders', 'Крылья для горного велосипеда 26 дюймов'), ('27.5" Mountain Bike Fenders', 'Крылья для горного велосипеда 27.5 дюймов'), ('Fenders for childrens bike', 'Крылья для детского велосипеда'), ('Fenders for childrens bike 12 inches', 'Крылья для детского велосипеда 12 дюймов'), ('Fenders for childrens bike 16 inches', 'Крылья для детского велосипеда 16 дюймов'), ('Fenders for folding bike', 'Крылья для складного велосипеда'), ('Fenders for 20" folding bike', 'Крылья для складного велосипеда 20 дюймов'), ('Fenders for fatbike 26 inches', 'Крылья для фэтбайка 26 дюймов'), ('28" road bike fenders', 'Крылья для шоссейного велосипеда 28 дюймов'), ('Metal fenders for a bicycle', 'Металлические крылья для велосипеда'), ('plastic fenders for bike', 'Пластиковые крылья на велосипед'), ('Highway', 'Шоссейные'), ('Wing kits', 'Комплекты крыльев'), ('Bicycle front fenders', 'Передние крылья для велосипеда'), ('Wing holders', 'Держатели крыльев')], max_length=100, verbose_name='Тип')),
                ('material', models.CharField(max_length=100, verbose_name='Материал')),
                ('Place_of_attachment', models.CharField(max_length=100, verbose_name='Место крепления')),
                ('size', models.CharField(max_length=100, verbose_name='Размеры')),
                ('mount_type', models.CharField(max_length=200, verbose_name='Тип крепления')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessories.photo', verbose_name='Фотографии')),
            ],
            options={
                'verbose_name': 'Крылья',
            },
        ),
        migrations.CreateModel(
            name='BicycleBags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('type', models.CharField(choices=[('Bicycle bags for phone', 'Велосумки для телефона'), ('Bicycle bags under the frame', 'Велосумки под раму'), ('Saddle bags', 'Подседельные велосумки'), ('Foldable cycling pants on the trunk', 'Складные велосумки-штаны на багажник'), ('Bicycle glove boxes', 'Сумки бардачки для велосипеда'), ('Bicycle bags', 'Сумки для велосипеда'), ('Bags for childrens bikes', 'Сумки для детских велосипедов'), ('Handlebar bags', 'Сумки на руль велосипеда'), ('Saddle bags', 'Сумки под седло'), ('Frame bags', 'Сумки на раму'), ('Trunk bags', 'Сумки на багажник')], max_length=100, verbose_name='Тип')),
                ('material', models.CharField(max_length=100, verbose_name='Материал')),
                ('clasp', models.CharField(max_length=100, verbose_name='Застежка')),
                ('mount_type', models.CharField(max_length=200, verbose_name='Тип крепления')),
                ('volume', models.CharField(max_length=40, verbose_name='Объем')),
                ('dimensions', models.CharField(max_length=60, verbose_name='Габариты')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessories.photo', verbose_name='Фотографии')),
            ],
            options={
                'verbose_name': 'Велосипедная сумка',
                'verbose_name_plural': 'Велосипедные сумки',
            },
        ),
    ]