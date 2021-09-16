from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta

class Strategy(models.Model):
	name = models.CharField(max_length=50, help_text="Name of our strategy")
	length = models.IntegerField(help_text="Number of items to be looped over")
    buy=ArrayField(models.IntegerField(), blank=True)
    sell=ArrayField(models.IntegerField(), blank=True)
	created_date = models.DateTimeField(auto_now_add=True, help_text="Date of creation")
	edited_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"Strategy: {self.name}"

	def get_absolute_name(self):
		return reverse("strategy", args=[str(self.id)])
