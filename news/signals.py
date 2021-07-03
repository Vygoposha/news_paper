from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template.loader import render_to_string

import news.models
from .models import *

@receiver(m2m_changed, sender = Post.Post_category.through)
def notify_subscribers(sender, instance, **kwargs):
        subject = None
        for i in list(instance.Post_category.all().values("category_name")):
            subject = f"Новый пост в категории {i.get('category_name')}"
            break
        for user_id in list(instance.Post_category.all().values_list('subscribers', flat=True)):
            user = User.objects.get(id=user_id)
            html_content = render_to_string(
                'send_email_subscribers.html',
                {'instance':instance,
                 'user': user}
            )

            msg = EmailMultiAlternatives(
                            subject = subject,
                            body=html_content,
                            from_email='igor.vigol@yandex.ru',
                            to = [user.email],
                        )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()