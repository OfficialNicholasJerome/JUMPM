from django.db import models

# Create your models here.

class AddMail(models.Model):
	email = models.CharField(max_length=200, null=False, blank=False)

def __str__(self):
	return self.title