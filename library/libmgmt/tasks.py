from celery import shared_task
from datetime import date
from django.core.mail import send_mail
from .models import Checkout

@shared_task
def remind_users_to_return_book():
    checkouts_today = Checkout.objects.filter(return_date__date__lte=date.today())

    for checkout in checkouts_today:
        user = checkout.user.username
        book = checkout.book.title

        subject = 'Reminder: Return your book today\n'
        message = f'Dear {user}, \n\nThis is a reminder to return the book "{book}" today. Thank you!'
        print(subject, message)

    return f'Successfully sent reminders to {len(checkouts_today)} users.'