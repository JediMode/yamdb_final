from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_yamdb.settings import AUTH_USER_MODEL
from .validators import validate_year


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Категория',
        help_text='Укажите категорию'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Уникальный идентификатор',
        help_text='Укажите уникальный идентификатор категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Жанр',
        help_text='Укажите жанр'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Уникальный идентификатор',
        help_text='Укажите уникальный идентификатор жанра'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Произведение',
        help_text='Укажите произведение'
    )
    year = models.IntegerField(
        validators=(validate_year,),
        verbose_name='Год создания',
        help_text='Укажите год создания произведения'
    )
    description = models.TextField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        max_length=200,
        blank=True,
        null=True,
        related_name='titles',
        help_text='Укажите категорию',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        help_text='Укажите жанр',
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        max_length=200,
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        max_length=200,
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text="Введите текст отзыва"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10, 'Оценка не может быть больше 10'),
            MinValueValidator(1, 'Оценка не может быть меньше 1'),
        ]
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [models.UniqueConstraint(
            fields=['author', 'title'],
            name='unique_review'
        )]

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        max_length=200,
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        max_length=200,
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text="Введите текст комментария",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
