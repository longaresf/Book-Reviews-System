from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView,
                                PasswordResetCompleteView, PasswordChangeView,
                                PasswordChangeDoneView, PasswordResetView)
from django.urls import reverse_lazy

class PasswordResetView(PasswordResetView):
   template_name = 'registration/password_reset_form.html'
   email_template_name = "registration/email_text/password_reset_email.html"
   from_email = 'admin@gmail.com'
   subject_template_name = "registration/email_text/password_reset_subject.txt"
   success_url = reverse_lazy("ue_app:password_reset_done")

class PasswordResetDoneView(PasswordResetDoneView):
   template_name = 'registration/email_text/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
   template_name = 'registration/email_text/password_reset_confirm.html'
   success_url = reverse_lazy("ue_app:password_reset_complete")

class PasswordResetCompleteView(PasswordResetCompleteView):
   template_name = 'registration/email_text/password_reset_complete.html'

class PasswordChangeView(PasswordChangeView):
   template_name = 'registration/email_text/password_change_form.html'
   success_url = reverse_lazy("ue_app:password_change_done")

class PasswordChangeDoneView(PasswordChangeDoneView):
   template_name = 'registration/email_text/password_change_done.html'