from django.db import models

# Create your models here.

class Area(models.Model):
	# Fields
	id = models.IntegerField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	longitude = models.FloatField(max_length=20)
	latitude = models.FloatField(max_length=20)

	# Helper Methods
	def number_of_locations(self):
		return self.location_set.count()

	def average_measurement(self):
		locationsForArea = self.location_set.all()
		measurementCount = 0
		measurementSum = 0
		for location in locationsForArea:
			measurementsForLocation = location.measurement_set.all()
			for measurement in measurementsForLocation:
				measurementSum += measurement.value
				measurementCount += 1
		if measurementCount >= 1:
			return measurementSum / measurementCount
		else:
			return None

	def __str__(self):
		return self.name

	# def category_names(self):
	# 	Categories removed from assignment

class Location(models.Model):
	# Fields
	id = models.IntegerField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	altitude = models.IntegerField(max_length=20)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

	# Methods
	def __str__(self):
		string = self.area.name + ":" + self.name
		return string

class Measurement(models.Model):
	# Fields
	id = models.IntegerField(primary_key=True, max_length=10)
	value = models.FloatField(max_length=20)
	date = models.DateTimeField(max_length=30)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

	# Methods
	def __str__(self):
		string = "measurement@" + self.location.__str__()
		return string