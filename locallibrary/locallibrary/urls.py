"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('accounts/', include('accounts.urls')),
    path('classbasedview/', include('classbasedview.urls')),
]


#import accounts
#from accounts import views as accounts_views

# registration


#urlpatterns = [
    #path('signup/', accounts.views.signup, name='signup'),
#]
#urlpatterns = [
    #path('signup/', accounts_views.signup, name='signup'),
    
    #path('login/', auth_views.LoginView.as_view(), name='login'),

    #path ('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),

    #path ('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html')),
    #path ('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')),
    #path ('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_confirm.html')),
    #path ('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')),

#]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)