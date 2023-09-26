from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', overwrite=True, max_length=250, unique=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="author_name", null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    DRAFT = 0
    PUBLISHED = 1

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    slug = AutoSlugField('slug', populate_from='title', unique=True, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    status = models.IntegerField(verbose_name="blog_status", choices=STATUS_CHOICES, default=DRAFT)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, max_length=250)
    body = RichTextField(null=True, blank=True)
    author = models.ForeignKey(Author, related_name='posts_author', on_delete=models.PROTECT)
    publication_date = models.DateTimeField(_('publication date'),db_index=True, default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='blog_category')

    def __str__(self):
        return self.title