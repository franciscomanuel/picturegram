"""Users vuews."""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exception
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm


def login_view(request):
	"""Login view."""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user:
			login(request, user)
			return redirect('feed')
		else:
			return render(request, 'users/login.html', {'error': 'Invalid username and password'})
	return render(request, 'users/login.html')


@login_required
def logout_view(request):
	"""Logout user."""
	logout(request)
	return redirect('login')


def signup_view(request):
	"""Sign up view."""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']

		if password != password_confirmation:
			return render(request, 'users/signup.html', { 'error': 'El password no coincide' })

		try:
			user = User.objects.create_user(username=username, password=password)
		except IntegrityError:
			return render(request, 'users/signup.html', { 'error': 'Ya existe un usuario con esas credenciales' })


		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()

		profile = Profile(user=user)
		profile.save()

		return redirect('login')

	return render(request, 'users/signup.html')


def update_profile_view(request):
	"""Update a user's profile view."""
	
	profile = request.user.profile

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data

			profile.website = data['website']
			profile.phone_number = data['phone_number']
			profile.biography = data['biography']
			profile.picture = data['picture']
			profile.save()

			return redirect('update_profile')
	else:
		form = ProfileForm()

	return render(
		request=request, 
		template_name = 'users/update_profile.html',
		context={
			'profile': profile,
			'user': request.user,
			'form': form
		}
	)


