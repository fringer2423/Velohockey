from django.db import models


class Photo(models.Model):
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    title = models.CharField(verbose_name="Название", max_length=40)
    image = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return self.title


class BicycleBags(models.Model):
    class Meta:
        verbose_name = "Велосипедная сумка"
        verbose_name_plural = "Велосипедные сумки"

    TYPE_CHOICES = (
        ('Bicycle bags for phone', 'Велосумки для телефона'),
        ('Bicycle bags under the frame', 'Велосумки под раму'),
        ('Saddle bags', 'Подседельные велосумки'),
        ('Foldable cycling pants on the trunk', 'Складные велосумки-штаны на багажник'),
        ('Bicycle glove boxes', 'Сумки бардачки для велосипеда'),
        ('Bicycle bags', 'Сумки для велосипеда'),
        ('Bags for childrens bikes', 'Сумки для детских велосипедов'),
        ('Handlebar bags', 'Сумки на руль велосипеда'),
        ('Saddle bags', 'Сумки под седло'),
        ('Frame bags', 'Сумки на раму'),
        ('Trunk bags', 'Сумки на багажник')
    )

    title = models.CharField(verbose_name="Название", max_length=40)
    description = models.TextField(verbose_name="Описание")
    image = models.ForeignKey(Photo, verbose_name="Фотографии", on_delete=models.CASCADE)
    type = models.CharField(verbose_name="Тип", max_length=100, choices=TYPE_CHOICES)
    material = models.CharField(verbose_name="Материал", max_length=100)
    clasp = models.CharField(verbose_name="Застежка", max_length=100)
    mount_type = models.CharField(verbose_name="Тип крепления", max_length=200)
    volume = models.CharField(verbose_name="Объем", max_length=40)
    dimensions = models.CharField(verbose_name="Габариты", max_length=60)
    weight = models.CharField(verbose_name="Вес", max_length=10)

    def __str__(self):
        return self.title


class Fenders(models.Model):
    class Meta:
        verbose_name = "Крылья"

    FENDER_CHOICES = (
        ('Rear fenders for bicycle', 'Задние крылья для велосипеда'),
        ('Rear fenders for mountain bike', 'Задние крылья для горного велосипеда'),
        ('Fender kits for 26" bike', 'Комплекты крыльев для велосипеда 26 дюймов'),
        ('Mudguards 12″-18″ for bike', 'Крылья 12″-18″ для велосипеда'),
        ('Mudguards 20″ for bicycle', 'Крылья 20″ для велосипеда'),
        ('Mudguards 24″ for bicycle', 'Крылья 24″ для велосипеда'),
        ('Mudguards 26″ for bike', 'Крылья 26″ для велосипеда'),
        ('Mudguards 27.5″ for bike', 'Крылья 27.5″ для велосипеда'),
        ('Mudguards 28″ for bike', 'Крылья 28″ для велосипеда'),
        ('Mudguards 29″ for bike', 'Крылья 29″ для велосипеда'),
        ('Wings for Fatbike', 'Крылья для Fatbike'),
        ('Mudguards for 16 inch bike', 'Крылья для велосипеда 16 дюймов'),
        ('Fenders for bike Merida', 'Крылья для велосипеда Merida'),
        ('Mudguards for SKS 26" bike', 'Крылья для велосипеда SKS 26 дюймов'),
        ('Mudguards for bike Stels', 'Крылья для велосипеда Stels'),
        ('Mudguards for bike Stels 26 inches', 'Крылья для велосипеда Stels 26 дюймов'),
        ('MTB fenders', 'Крылья для горного велосипеда'),
        ('26" mountain bike fenders', 'Крылья для горного велосипеда 26 дюймов'),
        ('27.5" Mountain Bike Fenders', 'Крылья для горного велосипеда 27.5 дюймов'),
        ('Fenders for childrens bike', 'Крылья для детского велосипеда'),
        ('Fenders for childrens bike 12 inches', 'Крылья для детского велосипеда 12 дюймов'),
        ('Fenders for childrens bike 16 inches', 'Крылья для детского велосипеда 16 дюймов'),
        ('Fenders for folding bike', 'Крылья для складного велосипеда'),
        ('Fenders for 20" folding bike', 'Крылья для складного велосипеда 20 дюймов'),
        ('Fenders for fatbike 26 inches', 'Крылья для фэтбайка 26 дюймов'),
        ('28" road bike fenders', 'Крылья для шоссейного велосипеда 28 дюймов'),
        ('Metal fenders for a bicycle', 'Металлические крылья для велосипеда'),
        ('plastic fenders for bike', 'Пластиковые крылья на велосипед'),
        ('Highway', 'Шоссейные'),
        ('Wing kits', 'Комплекты крыльев'),
        ('Bicycle front fenders', 'Передние крылья для велосипеда'),
        ('Wing holders', 'Держатели крыльев')
    )

    title = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание")
    image = models.ForeignKey(Photo, verbose_name="Фотографии", on_delete=models.CASCADE)
    type = models.CharField(verbose_name="Тип", max_length=100, choices=FENDER_CHOICES)
    material = models.CharField(verbose_name="Материал", max_length=100)
    Place_of_attachment = models.CharField(verbose_name="Место крепления", max_length=100)
    size = models.CharField(verbose_name="Размеры", max_length=100)
    mount_type = models.CharField(verbose_name="Тип крепления", max_length=200)
    color = models.CharField(verbose_name="Цвет", max_length=100)

    def __str__(self):
        return self.title
