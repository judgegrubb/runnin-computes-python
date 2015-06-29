from django.db import models

# Create your models here.
class Professor(models.Model):
	name = models.CharField(default="", max_length=200)
	rating_total = models.IntegerField(default=0)
	num_of_ratings = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name