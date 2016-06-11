from __future__ import unicode_literals

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.

class MedicineType(models.Model):

	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Boala(models.Model):
	name = models.CharField(max_length=100)
	short_description = models.CharField(max_length=500)

class Farmacie(models.Model):
	name = models.CharField(max_length=100)
	adresa = models.CharField (max_length= 100)
	longitude = models.FloatField(null=True)
	latitude = models.FloatField(null=True)


class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	e_mail = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
class Medicament(models.Model):

	LOW = '0'
	MEDIUM = '1'
	HIGH = '2'
	PUTEREA_EFECTULUI_CHOICES = (
		(LOW, 'Low'),
		(MEDIUM, 'Medium'),
		(HIGH, 'High'),
	)
	puterea_efectului = models.CharField(max_length=2, choices=PUTEREA_EFECTULUI_CHOICES, default=0,)
	medium_price = models.DecimalField(max_digits=7, decimal_places=2)
	description = models.TextField()
	name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=512)
	image = ThumbnailerImageField(null=True, blank=True)
	medicine_type = models.ForeignKey(MedicineType)
	boala = models.ManyToManyField(Boala)
	omologi = models.ManyToManyField("self")
	

class Review(models.Model):
	comment = models.TextField()
	rating_value = models.DecimalField(max_digits=2, decimal_places=1, default=0) 
	medicament = models.ForeignKey(Medicament)
	user = models.ForeignKey(User)

class MedicamentPharmacy(models.Model):
	medicament = models.ForeignKey(Medicament)
	farmacie = models.ForeignKey(Farmacie)
	quantity = models.IntegerField (default=0)
	price = models.DecimalField(max_digits=7, decimal_places=2)






