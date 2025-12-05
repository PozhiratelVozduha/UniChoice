from django.db import models

# Create your models here.
class Universities(models.Model):
    UNIVERSITY_TYPES = [
        ('technical', 'Технический'),
        ('medical', 'Медицинский'),
        ('humanitarian', 'Гуманитарный'),
        ('creative', 'Творческий')
    ]
    name = models.CharField('Название университета', max_length=200)
    detail_info = models.TextField('Информация')
    university_type = models.CharField('Тип универа', max_length=50, choices=UNIVERSITY_TYPES, default='technical')
    ent_score = models.IntegerField('Минимальный балл ент')
    image = models.ImageField('Фото университета', null=True, blank=True)

    def __str__(self):
        return self.name