"""Views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

import json


def hello_world(request):
	return HttpResponse('Hello World!')


def get_time(request):
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse(f'Oh, hi! Current server time is {now}')


def sorted_integer(request):
	numbers = request.GET['numbers']
	params_list = numbers.split(",")
	params_list_number_sorted = sorted(list(map(int, params_list)))
	data = {
	'status': 'ok',
	'numbers': params_list_number_sorted,
	'message': 'Integers sorted successfully'
	}
	return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
	message = 'Bienvenido'
	if age < 18:
		message = 'Lo siento, eres menor de edad'
	return HttpResponse(f'Hi {name}: {message}')