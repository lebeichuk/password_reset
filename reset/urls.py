from django.urls import path

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="reset/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="reset/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="reset/password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="reset/password_reset_done.html"),
         name="password_reset_complete"),



]

'''
PASSWORD_RESET_TIMEOUT_DAYS = 1 in settings.py
Check the timestamp is within limit. Timestamps are rounded to
midnight (server time) providing a resolution of only 1 day. If a
link is generated 5 minutes before midnight and used 6 minutes later,
that counts as 1 day. Therefore, PASSWORD_RESET_TIMEOUT_DAYS = 1 means
"at least 1 day, could be up to 2."

1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
