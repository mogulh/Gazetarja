from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Kategori(models.Model):
	title = models.CharField(default='', max_length=999900000)
	slug = models.SlugField(default='', editable=False, max_length=50)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category', kwargs={'slug': self.slug, 'pk': self.id})

	def save(self, *args, **kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)



class Lajmet(models.Model):
	kategorit = models.ForeignKey(Kategori, on_delete=models.CASCADE)
	titulli = models.CharField(default='', max_length=350)
	slug = models.SlugField(default='', editable=False, max_length=1000)
	shikime = models.IntegerField(default=0)
	fotografit = models.ImageField(upload_to='imgs/')
	detajet = RichTextUploadingField()
	data_e_postimit = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	verified = models.BooleanField(default=True)

	def __str__(self):
		return self.titulli

	def get_absolute_url(self):
		return reverse('lajme-detail', kwargs={'slug': self.slug, 'pk': self.id})

	def save(self, *args, **kwargs):
		value = self.titulli
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)


class SponsorPost(models.Model):
	titulli = models.CharField(default='', max_length=350)
	slug = models.SlugField(default='', editable=False, max_length=1000)
	shikime = models.IntegerField(default=0)
	fotografit = models.ImageField(upload_to='sponsor/')
	detajet = RichTextUploadingField()
	data_e_postimit = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulli

	def get_absolute_url(self):
		return reverse('sponsor-detail', kwargs={'slug': self.slug, 'pk': self.id})

	def save(self, *args, **kwargs):
		value = self.titulli
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)


class Terms(models.Model):
	titulli = models.CharField(default='', max_length=50)
	slug = models.SlugField(default='', editable=False, max_length=1000)
	detajet = RichTextUploadingField()

	def __str__(self):
		return self.titulli

	def get_absolute_url(self):
		return reverse('terms-detail', kwargs={'slug': self.slug, 'pk': self.id})

	def save(self, *args, **kwargs):
		value = self.titulli
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)


class Privacy(models.Model):
	titulli = models.CharField(default='', max_length=50)
	slug = models.SlugField(default='', editable=False, max_length=1000)
	detajet = RichTextUploadingField()

	def __str__(self):
		return self.titulli

	def get_absolute_url(self):
		return reverse('privacy-detail', kwargs={'slug': self.slug, 'pk': self.id})

	def save(self, *args, **kwargs):
		value = self.titulli
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)




