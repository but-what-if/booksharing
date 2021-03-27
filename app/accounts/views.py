from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, RedirectView
from django.core.mail import send_mail
from annoying.functions import get_object_or_None
from django.contrib import messages

from accounts.models import User, ContactUs

from accounts.forms import SignUpForm


def send_contact_us_email(form_data):
    message = f"""
                Email from: {form_data["contact_to_email"]}
                Name: {form_data["full_name"]}
                Message: {form_data["message"]}
            """

    send_mail(
        'Contact Us',
        message,
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user


class ContactUsView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    fields = (
        'full_name',
        'contact_to_email',
        'message'
    )

    def form_valid(self, form):
        response = super().form_valid(form)
        send_contact_us_email(form.cleaned_data)
        return response


class SignUpView(CreateView):
    model = User
    success_url = reverse_lazy('index')
    form_class = SignUpForm
    template_name = 'accounts/signup.html'


class ActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_None(User, username=username, is_active=False)
        if user:
            user.is_active = True
            user.save(update_fields=('is_active', ))
            messages.add_message(self.request, messages.INFO, 'Your account is activated!')
        return super().get_redirect_url(*args, **kwargs)
