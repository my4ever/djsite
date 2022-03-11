from django.db import models
from django.urls import reverse


class Women(models.Model):
    """This is the model for women object."""
    title = models.CharField(max_length=255, verbose_name='имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='биография')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='обнавлён')
    is_published = models.BooleanField(default=True, verbose_name='опубликован')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_created', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
