
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, RechargeForm
from .models import Recharge


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'htmlfiles/register.html', {'form': form})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('recharge')
	return render(request, 'htmlfiles/login.html')

def logout(request):
	logout(request)
	return redirect('login')

@login_required
def recharge(request):
	if request.method == 'POST':
		form = RechargeForm(request.POST)
		if form.is_valid():
			recharge = form.save(commit=False)
			recharge.user = request.user
			recharge.save()
			return redirect('history')
	else:
		form = RechargeForm()
	return render(request, 'htmlfiles/recharge.html', {'form': form})

@login_required
def history(request):
	recharges = Recharge.objects.filter(user=request.user).order_by('-timestamp')
	return render(request, 'htmlfiles/history.html', {'recharges': recharges})