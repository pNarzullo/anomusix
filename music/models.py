from django.db import models
from django.urls import reverse


class Music(models.Model):
    audio = models.FileField('Песня', upload_to='uploads/%Y/%m/%d/')
    cover = models.ImageField('Обложка', upload_to='uploads/%Y/%m/%d', default='default_note.jpg', null=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT,
                               verbose_name='Исполнитель', null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Категория', null=True)
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name} — {self.author.name}'

    def get_absolute_url(self):
        return reverse('music:song', kwargs={'song_id': self.pk})


class Author(models.Model):
    name = models.CharField('Имя исполнителя', max_length=50)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:category', kwargs={'category_id': self.pk})


class BestSong(Music):
    pass

