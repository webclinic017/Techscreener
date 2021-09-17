from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields.array import ArrayField

class Strategy(models.Model):
	buy = ArrayField(models.IntegerField(), blank=True)
	sell = ArrayField(models.IntegerField(), blank=True)
	name = models.CharField(max_length=50, help_text="Name of our strategy")
	length = models.IntegerField(help_text="Number of items to be looped over")

	class Meta:
		db_table = "strategy"

	def __str__(self):
		return f"Strategy: {self.name}"

	def get_absolute_url(self):
		return reverse("strategy", args=[str(self.id)])
