import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yekjamodir.c_settings.prod')

application = get_wsgi_application()
