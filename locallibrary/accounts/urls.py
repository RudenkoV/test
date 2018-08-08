from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
import accounts
from accounts import views as accounts_views
from . import views




#log in and gog out




#urlpatterns = [
    #path('signup/', views.signup, name='signup'),
#]


urlpatterns = [

path('signup/', views.signup, name='signup'),

path('login/', auth_views.LoginView.as_view(), name='login'),

path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),

path ('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html')),

path ('change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), name='password_change_done'),

path ('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html')),
path ('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')),
path ('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_confirm.html')),
path ('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')),



]