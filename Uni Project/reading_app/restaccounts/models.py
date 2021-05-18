from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import Account

class DriverUser(Account):
	name = models.CharField(max_length=250, default='Name')
	def __str__(self):
		return self.username