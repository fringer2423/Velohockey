# Generated by Django 4.0.3 on 2022-04-08 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('remainder', models.IntegerField(verbose_name='Остаток')),
                ('vendor_code', models.CharField(max_length=40, verbose_name='Артикул')),
                ('size', models.CharField(blank=True, choices=[('6-9', '6-9'), ('9-13', '9-13'), ('12 "SO', '12 "SO'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=10, verbose_name='Размер')),
                ('male', models.CharField(blank=True, choices=[('for female', 'для женщин'), ('unisex', 'унисекс')], max_length=10, verbose_name='Пол')),
                ('age', models.CharField(blank=True, choices=[('adult', 'для взрослых'), ('teenager', 'для подростков')], max_length=10, verbose_name='Возраст')),
                ('material', models.CharField(blank=True, choices=[('aluminum', 'алюминий'), ('carbon', 'карбон'), ('steel', 'сталь')], max_length=10, verbose_name='Материал рамы')),
                ('suspension_size', models.CharField(blank=True, choices=[('100', '100'), ('120', '120'), ('130', '130'), ('150', '150'), ('160', '160'), ('165', '165'), ('190', '190'), ('200', '200')], max_length=3, verbose_name='Ход подвески')),
                ('fork_type', models.CharField(blank=True, choices=[('aerial', 'воздушная'), ('spring-elastomer', 'пружинно-эластомерная'), ('oil-air', 'масляно-воздушная'), ('spring', 'пружинная'), ('tough', 'жесткая'), ('oil-spring', 'масляно-пружинная')], max_length=20, verbose_name='Конструкция вилки')),
                ('rear_suspension_size', models.CharField(blank=True, choices=[('40', '40'), ('50', '50'), ('55', '55'), ('75', '75'), ('125', '125')], max_length=3, verbose_name='Ход задней подвески')),
                ('speed_col', models.CharField(blank=True, choices=[('1', '1'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18'), ('21', '21'), ('24', '24')], max_length=2, verbose_name='Количество скоростей')),
                ('wheel_size', models.CharField(blank=True, choices=[('20', '20'), ('24', '24'), ('26', '26'), ('27.5', '27.5'), ('29', '29')], max_length=4, verbose_name='Размер колес')),
                ('brake_type', models.CharField(blank=True, choices=[('mechanical', 'дисковые механические'), ('hydraulic', 'дисковые гидравлические'), ('v-brake', 'v-brake')], max_length=20, verbose_name='Тип тормозов')),
                ('appointment', models.CharField(blank=True, choices=[('cross country', 'кросскантри'), ('trail', 'трэйл'), ('enduro', 'эндуро'), ('dirt', 'дерт'), ('downhill', 'даунхил')], max_length=20, verbose_name='Назначение')),
                ('suspension_type', models.CharField(blank=True, choices=[('hard', 'хардтейл'), ('two', 'двухподвес'), ('rigit', 'ригид')], max_length=10, verbose_name='Тип подвески')),
                ('equipment_level', models.CharField(blank=True, choices=[('begin', 'начальный'), ('begin+', 'начальный улучшенный'), ('middle', 'средний'), ('prof-', 'полупрофессиональный'), ('prof', 'профессиональный'), ('elite', 'элитный')], max_length=10, verbose_name='Уровень оборудования')),
                ('season', models.CharField(blank=True, choices=[('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019')], max_length=4, verbose_name='Сезон')),
                ('frame', models.TextField(verbose_name='Рама')),
                ('wheel_mount', models.CharField(max_length=30, verbose_name='Крепление колеса')),
                ('fork', models.TextField(verbose_name='Вилка')),
                ('stem', models.TextField(verbose_name='Вынос руля')),
                ('steering_wheel', models.TextField(verbose_name='Руль')),
                ('handlebars', models.TextField(verbose_name='Ручки руля')),
                ('steering_column', models.TextField(verbose_name='Рулевая колонка')),
                ('shifters', models.TextField(verbose_name='Манетки')),
                ('rear_derailleur', models.TextField(verbose_name='Задний переключатель')),
                ('foot', models.TextField(verbose_name='Лапка')),
                ('cassete', models.TextField(verbose_name='Кассета')),
                ('carriage', models.TextField(verbose_name='Каретка')),
                ('system', models.TextField(verbose_name='Система')),
                ('chain', models.TextField(verbose_name='Цепь')),
                ('pedals', models.TextField(verbose_name='Педали')),
                ('front_bushing', models.TextField(verbose_name='Передняя втулка')),
                ('rear_bushing', models.TextField(verbose_name='Задняя втулка')),
                ('rims', models.TextField(verbose_name='Обода')),
                ('tires', models.TextField(verbose_name='Покрышки')),
                ('front_brake', models.TextField(verbose_name='Передний тормоз')),
                ('rear_brake', models.TextField(verbose_name='Задний тормоз')),
                ('seatpost', models.TextField(verbose_name='Подсидельный штырь')),
                ('saddle', models.TextField(verbose_name='Седло')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='bicycles.brand', verbose_name='Бренд')),
                ('image', models.ManyToManyField(related_name='images', to='bicycles.photo', verbose_name='Фотография')),
                ('type', models.ManyToManyField(related_name='types', to='bicycles.type', verbose_name='Тип')),
            ],
        ),
    ]
