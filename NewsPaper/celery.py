import os
from celery import Celery

# связываем настройки джанго с celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

# Создаем экземпляр приложения Celery
app = Celery('NewsPaper')
# Устанавливаем для экземпляра файл конфигурации и указываем пространство имен, чтобы приложение Celery
# само находило настройки в общем файле конфигруации settings.py. Поиск по шаблону "CELERY_***"
app.config_from_object('django.conf:settings', namespace='CELERY')
# Автоматический поиск заданий в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()

