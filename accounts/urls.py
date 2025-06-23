from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    # Home page for accounts section
    path('', views.accounts, name='accounts-home'),

    # Built-in authentication views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Signup view
    path('signup/', views.signup_view, name='signup'),

    # Profile views
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),

    path('complete-profile/', views.complete_profile_view, name='complete_profile'),


     path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        success_url=reverse_lazy('accounts:password_reset_done'),
        email_template_name='accounts/password_reset_email.html',  # ✅ ye zaroori hai
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='accounts/password_reset_confirm.html',
    success_url=reverse_lazy('accounts:password_reset_complete')
), name='password_reset_confirm'),


    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]


