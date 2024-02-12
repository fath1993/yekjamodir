from yekjamodir.settings import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['yekjamodir.ir', '*.yekjamodir.ir', '*']


DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'jamiyat_central_db',
    'USER': 'jamiyat_central_db_admin',
    'PASSWORD': 'fdg54$55%34DA',
    'HOST': '188.253.2.195',
    'PORT': '5432',
}

DATABASES['log_db'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'jamiyat_log_db',
    'USER': 'jamiyat_central_db_admin',
    'PASSWORD': 'fdg54$55%34DA',
    'HOST': '188.253.2.195',
    'PORT': '5432',
}

CRONJOBS = [
    ('* * * * *', 'auto_robots.tasks.start_task_thread',),
]
