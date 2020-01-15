from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StatusBot(models.Model):
    status_id = models.IntegerField(verbose_name='Номер статуса')
    status_title = models.CharField(verbose_name='Название статуса', max_length=300, default='')

    class Meta:
        verbose_name = 'Статус для телеграм'
        verbose_name_plural = 'Статусы для телеграм'

class StatusAdmin(models.Model):
    status_id = models.IntegerField(verbose_name='Номер статуса')
    status_title = models.CharField(verbose_name='Название статуса', max_length=300, default='')

    class Meta:
        verbose_name = 'Статус для администрирования'
        verbose_name_plural = 'Статусы для администрирования'

class Classes(models.Model):
    class_id = models.IntegerField(verbose_name='ID класса')
    class_title = models.CharField(verbose_name='Название класса', max_length=300, default='')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Elements(models.Model):
    element_id = models.IntegerField(verbose_name='ID стихии')
    element_title = models.CharField(verbose_name='Название стихии', max_length=300, default='')

    class Meta:
        verbose_name = 'Стихия'
        verbose_name_plural = 'Стихии'

class Students(models.Model):
    edu_id = models.CharField(verbose_name='EDU_ID', max_length=300, unique=True)
    telegram_id = models.CharField(verbose_name='Телеграм', max_length=300, default='')
    surname = models.CharField(verbose_name='Фамилия', max_length=300)
    name = models.CharField(verbose_name='Имя', max_length=300)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, verbose_name='Статус для бота',
                                 on_delete=models.CASCADE, default='')
    element_id = models.ForeignKey(Elements, verbose_name='Стихия', on_delete=models.CASCADE, default='')
    status_bot = models.ForeignKey(StatusBot, verbose_name='Статус для бота',
                               on_delete=models.CASCADE, default='0')
    admin_status = models.ForeignKey(StatusAdmin, verbose_name='Статус для администрирования',
                               on_delete=models.CASCADE, default='0')
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.surname


class Teachers(models.Model):
    edu_id = models.CharField(verbose_name='EDU_ID', max_length=300, unique=True)
    telegram_id = models.CharField(verbose_name='Телеграм', max_length=300, default='')
    surname = models.CharField(verbose_name='Фамилия', max_length=300)
    name = models.CharField(verbose_name='Имя', max_length=300)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, verbose_name='Статус для бота',
                                 on_delete=models.CASCADE, default='')
    element_id = models.ForeignKey(Elements, verbose_name='Стихия', on_delete=models.CASCADE, default='')
    status_bot = models.ForeignKey(StatusBot, verbose_name='Статус для бота',
                               on_delete=models.CASCADE, default='0')
    admin_status = models.ForeignKey(StatusAdmin, verbose_name='Статус для администрирования',
                               on_delete=models.CASCADE, default='0')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.surname


class ClassAbsent(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True,
                             unique=True, auto_created=True)
    class_id = models.ForeignKey(Classes, verbose_name='ID класса',
                                 on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество отсутсвующих', default=0)
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'По классам'
        verbose_name_plural = 'По классам'


class Reasons(models.Model):
    reason_id = models.IntegerField(verbose_name='ID')
    reason_title = models.CharField(verbose_name='Наименование причины',
                                    max_length=300, default='')

    class Meta:
        verbose_name = 'Причина отсутсвия'
        verbose_name_plural = 'причины отсутсвтвия'

    def __str__(self):
        return self.reason_title


class Absent(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True,
                             unique=True, auto_created=True)
    student_id = models.ForeignKey(Students, verbose_name='ID ученика',
                                   on_delete=models.CASCADE)
    reason_id = models.ForeignKey(Reasons, verbose_name='Причина отсутствия',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отсутвующие'
        verbose_name_plural = 'Отсутвующие'


class Subjects(models.Model):
    subject_id = models.IntegerField(verbose_name='ID')
    subject_title = models.CharField(verbose_name='Наименование причины', max_length=300, default='')

    class Meta:
        verbose_name = 'Предметы'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.subject_title


class Marks(models.Model):
    class_id = models.ForeignKey(Classes, verbose_name='Класс', on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, verbose_name='Предмет', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Students, verbose_name='Ученик', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка', default='')
    mark_date = models.DateField(verbose_name='Дата получения')
    state = models.CharField(verbose_name='Вид работы', max_length=200, default='')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'