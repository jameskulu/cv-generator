from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(subject, message, fromMail, toArr):
    send_mail(subject, message, fromMail, toArr)
    return None
