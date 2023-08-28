from django.db import models


# Create your models here.
class Post(models.Model):
    '''Данные о посте '''
    title = models.CharField('Заголовок поста', max_length=100)
    descriotion = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



