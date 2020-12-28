from .base_urls import *

urlpatterns = [
     path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login.html"),
        name="account_login",
    ),
    path("signup/", views.accountSignup, name="account_signup"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="account/logout.html"),
        name="account_logout",
    ),
      path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/reset/password_reset.html",
            success_url = reverse_lazy('password_reset_done'),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/reset/password_reset_confirm.html",
            success_url = reverse_lazy('password_reset_complete')
            ),
            name="password_reset_confirm",
        ),
    path(
        "account/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
