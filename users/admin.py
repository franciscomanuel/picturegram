"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile admin."""

	# Orden de los campos
	list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
	
	# Campos con links al detalle
	list_display_links = ('pk', 'user')

	# Lista de campos editables en la tabla
	list_editable = ('phone_number', 'website', 'picture')

	# Crea un input para buscar por los campos indicados
	search_fields = (
		'user__email', 
		'user__first_name', 
		'user__last_name', 
		'phone_number'
	)

	# Añade un filtro por fecha de creación o modificación
	list_filter = (
		'user__is_active',
		'user__is_staff',
		'created', 
		'modified'
	)