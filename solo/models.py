from django.db import models

# Create your models here.
class Result(models.Model):
	result = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.result)