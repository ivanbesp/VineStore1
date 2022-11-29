from django.db import models

class GrapeVarity(models.Model):
    """
    Описывает сорта винограда.
    """

    title = models.CharField(max_length=60, unique=True, verbose_name='Название сорта')
    place = models.CharField(max_length=60, verbose_name='Место произрастания')
    harvest_season = models.CharField(max_length=60, verbose_name='Время сбора')
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Сорт винограда'
        verbose_name_plural = 'Сорта винограда'


class WineVarity(models.Model):
    """
    Описаны сорта вин.
    """
    
    title = models.CharField(max_length=60, unique=True, verbose_name='Название')
    types_of_wine = models.CharField(max_length=60, verbose_name='Тип вина')
    color = models.CharField(max_length=60, verbose_name='Цвет')
    grape_varity = models.ForeignKey(GrapeVarity, on_delete=models.PROTECT, verbose_name='Сорт винограда')
    
    aging_barrel = models.IntegerField(choices=[(i, i) for i in range(0, 101)], 
    verbose_name='Время выдержки в бочках (год)')  # время выдержки передается в параметр choices в виде список кортежей от (0, 0) до (100, 100)
    
    aging_bottel = models.IntegerField(choices=[(i, i) for i in range(0, 1201)], 
    verbose_name='Время выдержки в бутылках (месяц)')  # время выдержки передается в параметр choices в виде список кортежей от (0, 0) до (1200, 1200)

    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Сорт вина'
        verbose_name_plural = 'Сорта вин'


class StoredBarrel(models.Model):

    """
    Описывает хранящуюся бочку.
    """
    location = models.CharField(max_length=25, 
    choices=[(f'{room} - {chr(j + 65)}', f'{room} - {chr(j + 65)}') for room in range(1, 27) 
    for j in range(room)], verbose_name='Местоположение (комната, стеллаж)')  # номера комнат и буквы стеллажей

    date_of_competion = models.DateField(auto_now=True, verbose_name='Дата заполнения')
    date_of_manufacture = models.DateField('Дата изготовления')
    volume = models.IntegerField(choices=[(i, i) for i in range(15, 226, 30)], verbose_name='Объём (литр)')
    is_empty = models.BooleanField(default=False, verbose_name='Пусто?')
    wine_varity = models.ForeignKey(WineVarity, on_delete=models.PROTECT, verbose_name='Сорт вина')

    def __str__(self) -> str:
        return self.lacotion
    
    class Meta:
         verbose_name = 'Бочка'
         verbose_name_plural = 'Бочки'
