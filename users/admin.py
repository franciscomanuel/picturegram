"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

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

	# Agrupación del formulario
	fieldsets = (
		(
			'Profile', 
			{
				'fields': (('user', 'picture'),)
			}
		),
		(
			'Extra info',
			{
				'fields': (
					('website', 'phone_number'),
					('biography'),
				)
			}
		),
		(
			'Metadata',
			{
				'fields':(('created', 'modified'),)
			}
		)
	)

	# Estos campos solo son de lectura y no editables
	readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
	"""Profile in-line admin for users."""

	model = Profile
	can_delete = False
	verbose_name_plural = 'Profiles'


# Agregamos en el área de administración de User, el área de Profile
class UserAdmin(BaseUserAdmin):
	"""Add profile admin to base user admin."""

	inlines = (ProfileInline,)
	list_display = (
		'username', 
		'email', 
		'first_name', 
		'last_name',
		'is_active',
		'is_staff'
	)


# Eliminamos el registro de User, para registrar el nuevo con el profile inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)