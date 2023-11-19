"""
URL configuration for MallMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import users.views as users_views
from . import views as project_views
from django.urls import path
from users.views import RememberMeLoginView

urlpatterns = [
    path('', project_views.landing, name='landing'),

    path('admin/', admin.site.urls),

    path('home', project_views.home, name='home'),
    path('about', project_views.about, name='about'),
    path('profile', project_views.profile, name='profile'),
    path('info', project_views.info, name='info'),


    path('register/', users_views.register, name='register'),
    path('confirm-account-mail/', users_views.confirm_account_mail, name='confirm-account-mail'),
    path('confirm-account/', users_views.confirm_account, name='confirm-account'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', RememberMeLoginView.as_view(), name='login'),  

    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', users_views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', users_views.CustomPasswordResetView.as_view(), name='password_reset_complete'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    # path('login/', users_views.login, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
