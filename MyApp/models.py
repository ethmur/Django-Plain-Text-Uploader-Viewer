from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Text(models.Model):
	text = models.TextField()
	time_stamp = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		# had to subtract 5 hours because of some weird thing with utc, idk why
		return "Text: " + self.text + ", Date/Time Stamp: " + (self.time_stamp-timedelta(hours=5)).strftime("%c")
		
class Pic(models.Model):
	img_file = models.FileField(upload_to='documents/%Y/%m/%d')
	time_stamp = models.DateTimeField(default=timezone.now)