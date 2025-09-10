from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recharge


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class RechargeForm(forms.ModelForm):
	class Meta:
		model = Recharge
		fields = ['metro_card_number', 'amount', 'payment_method']