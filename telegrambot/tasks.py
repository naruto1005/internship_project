# telegrambot/tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        subject='Welcome to Our App!',
        message='Thank you for registering, Subhashini! 🎉',
        from_email='subhashini10.3.2005@gmail.com',  # Replace with your actual email
        recipient_list=[email],
        fail_silently=False,
    )
