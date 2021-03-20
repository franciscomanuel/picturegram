"""User Forms"""

# Django
from django import forms

# Model
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):
	"""Profile form."""

	website = forms.URLField(max_length=200, required=True)
	biography = forms.CharField(max_length=500, required=False)
	phone_number = forms.CharField(max_length=20, required=False)
	picture = forms.ImageField()


class SignupForm(forms.Form):
	"""Sign up form."""

	username = forms.CharField(min_length=4, max_length=50)

	password = forms.CharField(
		max_length=70, 
		widget=forms.PasswordInput()
	)
	password_confirmation = forms.CharField(
		max_length=70, 
		widget=forms.PasswordInput()
	)

	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)

	email = forms.CharField(
		min_length=6, 
		max_length=70, 
		widget=forms.EmailInput()
	)


	def clean_username(self):
		"""Username must be unique."""
		username = self.cleaned_data['username']
		exist_user = User.objects.filter(username=username).exists()

		if exist_user:
			raise forms.ValidationError('Username is already in use.')
		return username


	def clean_password_confirmation(self):
		"""Verify password confirmation match."""

		password = self.cleaned_data['password']
		password_confirmation = self.cleaned_data['password_confirmation']

		if password != password_confirmation:
			raise forms.ValidationError('Passwords do not match.')
		return password_confirmation


	def save(self):
		"""Create user and profile."""
		data = self.cleaned_data
		data.pop('password_confirmation')

		user = User.objects.create_user(**data)
		profile = Profile(user=user)
		profile.save()
