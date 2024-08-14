from django.urls import path
# from . import views
from main import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings






urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.sign_in, name='login'),
	path('logout/', views.sign_out, name='logout'),
	# path('reset/password/', views.reset_password, name='forgot_password'),
	# path('second-factor/', views.second_factor, name='second_factor'),
	# path('password_reset/', views.reset_password, name='password_reset'),
	# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	# path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	# path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)