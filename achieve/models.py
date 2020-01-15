from django.db import models
import uuid
import os
from edu_tatar.models import Students, Teachers
from tinymce.models import HTMLField
from django.contrib import admin


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('static/img/achieves', filename)


class Subjects(models.Model):
    description = models.CharField(verbose_name='Предмет', max_length=300)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.description

class Levels(models.Model):
    level = models.CharField(verbose_name='Уровень', max_length=300, unique=True)
    coefficient = models.FloatField(verbose_name='Коэффициент', default='1')

    class Meta:
        verbose_name = 'Уровень участия'
        verbose_name_plural = 'Уровни участия'

    def __str__(self):
        return self.level


class Results(models.Model):
    result = models.CharField(verbose_name='Результат', max_length=300, unique=True)
    coefficient = models.FloatField(verbose_name='Коэффициент', default='1')

    class Meta:
        verbose_name = 'Результат участия'
        verbose_name_plural = 'Результат участия'

    def __str__(self):
        return self.result


class Type(models.Model):
    type_of_achieve = models.CharField(verbose_name='Вид события', max_length=300, unique=True)
    coefficient = models.FloatField(verbose_name='Коэффициент', default='1')

    class Meta:
        verbose_name = 'Вид конкурса'
        verbose_name_plural = 'Виды конкурса'

    def __str__(self):
        return self.type_of_achieve

class TypeAchieve(models.Model):
    type_of_achieve = models.CharField(verbose_name='Вид достижения', max_length=300, unique=True)
    coefficient = models.FloatField(verbose_name='Коэффициент', default='1')

    class Meta:
        verbose_name = 'Тип достижения'
        verbose_name_plural = 'Типы достижения'

    def __str__(self):
        return self.type_of_achieve


class Achievements(models.Model):
    subject = models.ManyToManyField(Subjects, verbose_name='Предметы')
    level = models.ForeignKey(Levels, verbose_name='Уровень участия', default=False,
                              on_delete=models.CASCADE)
    result = models.ForeignKey(Results, verbose_name='Результат участия', default=False,
                               on_delete=models.CASCADE)
    speshial = models.ForeignKey(Type,verbose_name='Вид события', default=False, on_delete=models.CASCADE)
    type_achieve = models.ForeignKey(TypeAchieve, verbose_name='Вид достижения', default=False, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата получения')
    text = HTMLField(verbose_name='Описание', default='')
    teacher = models.ManyToManyField(Teachers, verbose_name='Учитель')
    student = models.ManyToManyField(Students, verbose_name='Ученик')
    # student = models.ForeignKey(Users, verbose_name='Ученик',
    #                             on_delete=models.CASCADE,  limit_choices_to={'is_teacher': False})
    image_1 = models.ImageField(verbose_name='Изображение (главное)', upload_to=get_file_path)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super(Achieve, self).save(*args, **kwargs)
