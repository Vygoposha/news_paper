from celery import shared_task
import time
from time import sleep
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_admins, mail_managers
from django.template.loader import render_to_string
from .models import Post, PostCategory, Category


@shared_task
def news_create_notify(user_id: list, news_id: int):
    news = Post.objects.get(id =news_id)
    for user_id in user_id:
        if user_id:
            user = User.objects.get(id = user_id)
            html_content = render_to_string(
                'send_email_subscribers.html',
                {'news': news,
                 'user': user}
            )

            msg = EmailMultiAlternatives(
                subject=f'{Post.Post_title}',
                body=html_content,
                from_email='igor.vigol@yandex.ru',
                to=[user.email],
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            sleep(10)

@shared_task
def news_weekly_notify():
    subject = 'Подборка новостей за неделю'
    body = 'Тестовая периодическая рассылка'
    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,  # это то же, что и message
        from_email='igor.vigol@yandex.ru',
        to=['igor.vigol@yandex.ru', 'igor.vigol@yandex.ru'],  # это то же, что и recipients_list
    )
    msg.send()
    sleep(10)