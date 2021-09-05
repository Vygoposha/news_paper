import os
from celery import Celery
from celery.schedules import crontab

# связываем настройки джанго с celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

# Создаем экземпляр приложения Celery
app = Celery('NewsPaper')
# Устанавливаем для экземпляра файл конфигурации и указываем пространство имен, чтобы приложение Celery
# само находило настройки в общем файле конфигруации settings.py. Поиск по шаблону "CELERY_***"
app.config_from_object('django.conf:settings', namespace='CELERY')
# Автоматический поиск заданий в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notify_every_week': {
        'task': 'news.tasks.news_weekly_notify',
        'schedule': crontab(minute='0', hour='8', day_of_week='monday'),
    },
}