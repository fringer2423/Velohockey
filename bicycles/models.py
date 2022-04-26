from django.db import models


class Brand(models.Model):
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    title = models.CharField(verbose_name="Название", max_length=20)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)

    def __str__(self):
        return self.title


class Type(models.Model):
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    title = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)


class Bike(models.Model):
    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"

    SIZE_CHOICES = (
        ('6-9', '6-9'),
        ('9-13', '9-13'),
        ('12 "SO', '12 "SO'),
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    )

    MALE_CHOICES = (
        ('for female', 'для женщин'),
        ('unisex', 'унисекс')
    )

    AGE_CHOICES = (
        ('adult', 'для взрослых'),
        ('teenager', 'для подростков')
    )

    MATERIAL_CHOICES = (
        ('aluminum', 'алюминий'),
        ('carbon', 'карбон'),
        ('steel', 'сталь')
    )

    SUSPENSION_CHOICES = (
        ('100', '100'),
        ('120', '120'),
        ('130', '130'),
        ('150', '150'),
        ('160', '160'),
        ('165', '165'),
        ('190', '190'),
        ('200', '200')
    )

    FORK_CHOICES = (
        ('aerial', 'воздушная'),
        ('spring-elastomer', 'пружинно-эластомерная'),
        ('oil-air', 'масляно-воздушная'),
        ('spring', 'пружинная'),
        ('tough', 'жесткая'),
        ('oil-spring', 'масляно-пружинная')
    )

    REAR_SUSPENSION_CHOICES = (
        ('40', '40'),
        ('50', '50'),
        ('55', '55'),
        ('75', '75'),
        ('125', '125')
    )

    SPEED_CHOICES = (
        ('1', '1'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('21', '21'),
        ('24', '24')
    )

    WHEEL_SIZE_CHOICES = (
        ('20', '20'),
        ('24', '24'),
        ('26', '26'),
        ('27.5', '27.5'),
        ('29', '29')
    )

    BRAKE_TYPE_CHOICES = (
        ('mechanical', 'дисковые механические'),
        ('hydraulic', 'дисковые гидравлические'),
        ('v-brake', 'v-brake')
    )

    APPOINTMENT_CHOICES = (
        ('cross country', 'кросскантри'),
        ('trail', 'трэйл'),
        ('enduro', 'эндуро'),
        ('dirt', 'дерт'),
        ('downhill', 'даунхил')
    )

    SUSPENSION_TYPE_CHOICES = (
        ('hard', 'хардтейл'),
        ('two', 'двухподвес'),
        ('rigit', 'ригид')
    )

    EQUIPMENT_LEVEL_CHOICES = (
        ('begin', 'начальный'),
        ('begin+', 'начальный улучшенный'),
        ('middle', 'средний'),
        ('prof-', 'полупрофессиональный'),
        ('prof', 'профессиональный'),
        ('elite', 'элитный')
    )

    SEASON_CHOICES = (
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019')
    )

    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")
    brand = models.ForeignKey(Brand, verbose_name="Бренд", related_name="brand", on_delete=models.CASCADE)
    image = models.ManyToManyField(Photo, verbose_name="Фотография", related_name="images")
    price = models.IntegerField(verbose_name="Цена")
    remainder = models.IntegerField(verbose_name="Остаток")
    vendor_code = models.CharField(verbose_name="Артикул", max_length=40)
    type = models.ManyToManyField(Type, verbose_name="Тип", related_name="types")
    size = models.CharField(verbose_name="Размер", max_length=10, choices=SIZE_CHOICES, blank=True)
    male = models.CharField(verbose_name="Пол", max_length=10, choices=MALE_CHOICES, blank=True)
    age = models.CharField(verbose_name="Возраст", max_length=10, choices=AGE_CHOICES, blank=True)
    material = models.CharField(verbose_name="Материал рамы", max_length=10, choices=MATERIAL_CHOICES, blank=True)
    suspension_size = models.CharField(verbose_name="Ход подвески", max_length=3, choices=SUSPENSION_CHOICES,
                                       blank=True)
    fork_type = models.CharField(verbose_name="Конструкция вилки", max_length=20, choices=FORK_CHOICES, blank=True)
    rear_suspension_size = models.CharField(verbose_name="Ход задней подвески", max_length=3,
                                            choices=REAR_SUSPENSION_CHOICES, blank=True)
    speed_col = models.CharField(verbose_name="Количество скоростей", max_length=2, choices=SPEED_CHOICES, blank=True)
    wheel_size = models.CharField(verbose_name="Размер колес", max_length=4, choices=WHEEL_SIZE_CHOICES, blank=True)
    brake_type = models.CharField(verbose_name="Тип тормозов", max_length=20, choices=BRAKE_TYPE_CHOICES, blank=True)
    appointment = models.CharField(verbose_name="Назначение", max_length=20, choices=APPOINTMENT_CHOICES, blank=True)
    suspension_type = models.CharField(verbose_name="Тип подвески", max_length=10, choices=SUSPENSION_TYPE_CHOICES,
                                       blank=True)
    equipment_level = models.CharField(verbose_name="Уровень оборудования", max_length=10,
                                       choices=EQUIPMENT_LEVEL_CHOICES, blank=True)
    season = models.CharField(verbose_name="Сезон", max_length=4, choices=SEASON_CHOICES, blank=True)
    frame = models.TextField(verbose_name="Рама")
    wheel_mount = models.CharField(verbose_name="Крепление колеса", max_length=30)
    fork = models.TextField(verbose_name="Вилка")
    stem = models.TextField(verbose_name="Вынос руля")
    steering_wheel = models.TextField(verbose_name="Руль")
    handlebars = models.TextField(verbose_name="Ручки руля")
    steering_column = models.TextField(verbose_name="Рулевая колонка")
    shifters = models.TextField(verbose_name="Манетки")
    rear_derailleur = models.TextField(verbose_name="Задний переключатель")
    foot = models.TextField(verbose_name="Лапка")
    cassete = models.TextField(verbose_name="Кассета")
    carriage = models.TextField(verbose_name="Каретка")
    system = models.TextField(verbose_name="Система")
    chain = models.TextField(verbose_name="Цепь")
    pedals = models.TextField(verbose_name="Педали")
    front_bushing = models.TextField(verbose_name="Передняя втулка")
    rear_bushing = models.TextField(verbose_name="Задняя втулка")
    rims = models.TextField(verbose_name="Обода")
    tires = models.TextField(verbose_name="Покрышки")
    front_brake = models.TextField(verbose_name="Передний тормоз")
    rear_brake = models.TextField(verbose_name="Задний тормоз")
    seatpost = models.TextField(verbose_name="Подсидельный штырь")
    saddle = models.TextField(verbose_name="Седло")

    def __str__(self):
        return self.title
