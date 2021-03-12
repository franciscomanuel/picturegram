"""Model admin classes."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""Post admin."""

	# Orden de los campos
	list_display = ('pk', 'title', 'photo', 'user', 'profile', 'created', 'modified')

	# Campos con links al detalle
	list_display_links = ('pk', 'title')

	# Crea un input para buscar por los campos indicados
	search_fields = (
		'title',
		'user__username',
	)

	# Añade un filtro por fecha de creación o modificación
	list_filter = (
		'created', 
		'modified'
	)

	# Agrupación del formulario
	fieldsets = (
		(
			'Post', 
			{
				'fields': (('title', 'photo'),)
			}
		),
		(
			'User info',
			{
				'fields': (('user', 'profile'),)
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
