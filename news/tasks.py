<<<<<<< HEAD
from celery import shared_task
import time

@shared_task
def hello():
    time.sleep(10)
    print('Hello World!')
=======
from time import sleep

import pytz

from celery import shared_task
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_admins, mail_managers
from django.template.loader import render_to_string

from .models import Post, Category


@shared_task
def news_create_notify(users_id: list, news_id: int):
    news = Post.objects.get(id=news_id)
    for user_id in users_id:
        if user_id:
            user = User.objects.get(id=user_id)
            html_content = render_to_string('news_create_notify.html',
                                            {'news': news,
                                             'username': user.username,
                                             }
                                            )
            msg = EmailMultiAlternatives(
                subject=f'{news.post_title}',
                # body=news.post_content,  # это то же, что и message
                from_email='epanisimov@yandex.ru',
                to=[user.email],  # это то же, что и recipients_list
                )
            msg.attach_alternative(html_content, "text/html")  # добавляем html
            msg.send()
            sleep(10)


@shared_task
def news_weekly_notify():
    # post_datetime_filter = datetime.now(pytz.timezone('Europe/Moscow')) - timedelta(days=7)

    # notify_dict = {}
    # for category in Category.objects.all():
    #     for subscriber in category.subscribers.all():
    #         if subscriber not in notify_dict.keys():
    #             notify_dict.update({subscriber: Post.objects.filter(post_category=category,
    #                                                                 post_datetime__gte=post_datetime_filter)})
    #         else:
    #             notify_dict[subscriber] = notify_dict[subscriber].union(Post.objects.filter(post_category=category,
    #                                                                                         post_datetime__gte=post_datetime_filter)).order_by('post_datetime')
    #
    # subject = 'Подборка новостей за неделю'
    # for user, news in notify_dict.items():
    #     html_content = render_to_string('news_weekly_notify.html',
    #                                     {'news': list(news),
    #                                      'username': user.username,
    #                                      }
    #                                     )
    #     msg = EmailMultiAlternatives(
    #         subject=subject,
    #         # body=news.post_content,  # это то же, что и message
    #         from_email='epanisimov@yandex.ru',
    #         to=[user.email],  # это то же, что и recipients_list
    #     )
    #     msg.attach_alternative(html_content, "text/html")  # добавляем html
    #     msg.send()
    #     sleep(10)

    subject = 'Подборка новостей за неделю'
    body = 'Тестовая периодическая рассылка'
    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,  # это то же, что и message
        from_email='epanisimov@yandex.ru',
        to=['epanisimov@yandex.ru', 'egoranisimov@gmail.com'],  # это то же, что и recipients_list
    )
    msg.send()
    sleep(10)



# celery -A NewsPaper worker -l INFO -P eventlet    - запуск задач
# celery -A NewsPaper worker -l INFO --pool=solo    - запуск задач по событию
# celery -A NewsPaper.celery beat -l INFO    - запуск задач по расписанию

# celery -A NewsPaper.celery beat --loglevel=INFO
>>>>>>> 82e6c34c1a595dd205a53b062a96944bc44fe19e
