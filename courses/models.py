from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

# Create your models here.

class Subject(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_details',
                       args=[self.slug,])

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])
    file = models.FileField(upload_to='files', blank=True)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model_in':('text',
                                                                   'video',
                                                                   'image',
                                                                   'file')})

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class Item(models.Model):
    module = models.ForeignKey(Module, related_name='items',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)
    file = models.FileField(upload_to='files/', blank=True, max_length=500)
    video = models.URLField(blank=True)

    def __str__(self):
        return self.title

class FileTest(models.Model):
    file = models.FileField(upload_to='files/', blank=True, max_length=500)
