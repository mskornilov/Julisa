from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/images/',
                              blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name + ' | ' + self.slug

    def get_absolute_url(self):
        return reverse('blog:index', args=[self.slug,])

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/subcategories/images',
                              blank=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Post(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    thumbnail_image = models.ImageField(upload_to='post/thumbnails',
                                        blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=status_choices,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} прокомментировал пост: {self.post}. {self.created}'
