from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Recharge(models.Model):
	PAYMENT_CHOICES = [
		('bKash', 'bKash'),
		('Nagad', 'Nagad'),
		('Card', 'Card'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	metro_card_number = models.CharField(max_length=20)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.metro_card_number} - {self.amount}"

