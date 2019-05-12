from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Genre(models.Model):
    genre = models.CharField(max_length= 50, unique = True, verbose_name = '类别')

    class Meta:
        db_table = 'genres'
        verbose_name_plural = '类别'
        ordering = ['genre']

    def __str__(self):
        return self.genre


class Country(models.Model):
    country = models.CharField(max_length = 50, default='', verbose_name = '地区')

    class Meta:
        db_table = 'countries'
        verbose_name_plural = '地区'
        ordering = ['country']

    def __str__(self):
        return self.country


class Person(models.Model):
    name = models.CharField(max_length = 60, default = '', verbose_name = '全名')

    class Meta:
        db_table = 'person'
        verbose_name_plural = '人物'
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length = 50, verbose_name = '题目')
    pubdate = models.CharField(max_length = 50, verbose_name = '上映日期')
    poster = models.CharField(max_length=100, verbose_name='封面')
    duration = models.CharField(max_length=50, verbose_name='时长')
    year = models.CharField(max_length=50, verbose_name='年份')
    languages = models.CharField(max_length=50, verbose_name='语言')

    summary = models.TextField(
        null = True,
        blank = True,
        verbose_name = '简介'
    )
    aka = models.TextField(
        null=True,
        blank=True,
        verbose_name='别名'
    )

    countries = models.ManyToManyField(
        Country,
        related_name = 'movies',
        verbose_name = '国家或地区'
    )
    genres = models.ManyToManyField(
        Genre,
        blank = True,
        related_name = 'movies',
        verbose_name = '类别'
    )


    # ---------------------- 评分  ----------------------
    rating_average = models.CharField(max_length = 50, verbose_name = '评分')
    rating_people = models.IntegerField(
        default = 0,
        verbose_name = '评分人数'
    )
    stars1 = models.FloatField(
        default = 0,
        validators = [MinValueValidator(0), MaxValueValidator(100)],
        verbose_name = '1星人数占比'
    )
    stars2 = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='2星人数占比'
    )
    stars3 = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='3星人数占比'
    )
    stars4 = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='4星人数占比'
    )
    stars5 = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='5星人数占比'
    )

    #  ---------------------- 人员  ----------------------
    director = models.ManyToManyField(
        Person,
        blank = True,
        related_name = 'directed_movies',
        verbose_name = '导演'
    )
    casts = models.ManyToManyField(
        Person,
        blank=True,
        related_name='acted_movies',
        verbose_name='主演',
    )
    writer = models.ManyToManyField(
        Person,
        blank=True,
        related_name='wrote_movies',
        verbose_name='编剧',
    )

    class Meta:
        db_table = 'movie'
        verbose_name_plural = '电影'


    def __str__(self):
        return self.title + ', ' + str(self.pubdate)