from urllib.parse import urljoin

from django.core.mail import send_mail
from geekshop.settings import DOMAIN_NAME
from django.urls import reverse


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key]
    )
    subject = "Подтверждение регистрации на сайте"
    message = f"""
        Для подтверждения регистрации {user.username} на сайте
        {DOMAIN_NAME} перейдите по ссылке:
        {urljoin(DOMAIN_NAME, verify_link)}
    """
    send_mail(subject, message, "noreply@localhost", [user.email])
