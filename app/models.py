from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.


class HomeSection(models.Model):
    image = models.ImageField(upload_to='uploads/')
    heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    consult_button = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'HeroSection'
        verbose_name_plural = 'HeroSections'

    def __str__(self):
        return self.title


class HealthCenter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = 'HealthCenter'
        verbose_name_plural = 'HealthCenters'

    def __str__(self):
        return self.title


class FooterBanner(models.Model):
    banner_image = models.ImageField(upload_to='uploads/')
    mobile_app_image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    google_play_image = models.ImageField(upload_to='uploads/')
    app_store_image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = 'FooterBanner'
        verbose_name_plural = 'FooterBanners'

    def __str__(self):
        return self.title


class Doctors(models.Model):
    image = models.ImageField(upload_to='uploads/')
    phone = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name


class Blog(models.Model):
    disease = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='uploads/')
    author_name = models.CharField(max_length=255)
    admitted_time = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['id']

    def __str__(self):
        return self.disease


class Appointment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    departments = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
