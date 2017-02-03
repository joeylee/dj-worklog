from django.db import models

# Create your models here.
class Title(models.Model):
	title = models.CharField(max_length=200)
	def publish(self):
		self.save()
	def __str__(self):
		return self.title

class Author(models.Model):
	author = models.CharField(max_length=200)
	def publish(self):
		self.save()
	def __str__(self):
		return self.title

