from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib.auth import views as auth_views

from .forms import LoginForm, ResetForm, SecondFactorForm

# def send_2FA_email(request, user):
# 	# Generate a random 6-digit 2FA code
# 	code = str(random.randint(1000000, 9999999))
# 	print(code)
# 	# Store it in the session (You might prefer to store it in the database)
# 	request.session['2FA_code'] = code

# 	# Send email with the code
# 	send_mail(
# 		'Tu código 2FA',
# 		f'Tu código de verificación para 2FA es: {code}',
# 		'no-reply@help.clientis.tech',  # Your sending email
# 		[user.email],
# 		fail_silently=False,
# 	)
# 	print("Mail sent to", user.email)
# 	return

# def verify_2FA_code(request, user, provided_code):
# 	stored_code = request.session.get('2FA_code', None)
# 	print(stored_code)
# 	# Compare the provided code with the stored code
# 	if provided_code == stored_code:
# 		# Remove the code from the session after it's been used
# 		del request.session['2FA_code']
# 		return True
# 	return False

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def sign_in(request):
    if request.method == 'GET':
        try:
            if request.user.is_authenticated:
                return redirect('index')
        except:
            pass

        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Get the user associated with the provided email
            user = User.objects.get(email=email)
            print(user)
            # Authenticate using the username associated with the email
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect('index')

            # If you're using a 2FA system, include it here
            send_2FA_email(request, user)
            request.session['temp_username'] = user.username
            request.session['temp_password'] = password
            return redirect('second_factor')
        else:
            messages.error(request, 'Email or password incorrect.')

        return render(request, 'login.html')

def sign_out(request):
	logout(request)
	# messages.success(request,f'You have been logged out.')
	return redirect('login')

# def reset_password(request):
#     return auth_views.PasswordResetView.as_view()(request)

# def second_factor(request):
# 	if request.method == 'POST':
# 		form = SecondFactorForm(request.POST)

# 		if form.is_valid():
# 			second_factor = form.cleaned_data['second_factor']

# 			# Verify the 2FA code. Placeholder function here
# 			is_valid_2fa = verify_2FA_code(request, request.user, second_factor)
# 			print(is_valid_2fa)
# 			if is_valid_2fa:
# 				# Get stored username and password from session
# 				username = request.session.pop('temp_username', None)
# 				password = request.session.pop('temp_password', None)
				
# 				user = authenticate(request, username=username, password=password)
# 				if user:
# 					login(request, user)
# 					return redirect('index')

# 	form = SecondFactorForm()
	# return render(request,'access/second_factor.html',{'form': form}) 