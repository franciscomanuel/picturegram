"""Posts views."""

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
	{
		'title': 'Mont Blanc',
		'user': {
			'name': 'Venus',
			'picture': 'https://picsum.photos/200/200/?image=1027'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/200/200/?image=1036'
	},
	{
		'title': 'Via Láctea',
		'user': {
			'name': 'Dark Vader',
			'picture': 'https://picsum.photos/200/200/?image=1005'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/200/200/?image=903'
	},
	{
		'title': 'Nuevo auditorio',
		'user': {
			'name': 'Francisco',
			'picture': 'https://picsum.photos/200/200/?image=883'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/200/200/?image=1076'
	}
]


def list_posts(request):
	return render(request, 'feed.html', {'posts': posts})