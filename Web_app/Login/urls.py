from django.urls import path ,include
# from Login.views import index
from Login.views import register
from Login.views import login
from Login.views import forgotpassword, change_password
from Login.views import logout
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [
    path("register/",register, name="register"),
    path("login/",login, name="login"),
    path("logout/",logout, name="logout"),
    path("forgotpassword/",forgotpassword, name="forgotpassword"),
    path("change_password/",change_password, name="change_password"),



 
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html'
            #  success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]




