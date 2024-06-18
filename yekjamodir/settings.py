from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django_crontab',
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'rest_framework',
    "corsheaders",
    'django_jalali',
    'robots',
    'tinymce',
    'gallery',
    'custom_logs',
    'accounts',
    'warehouse',
    'financial_accounting',
    'auto_robots',
    'calendar_event',
    'dashboard',
    'documents',
    'task_manager',
    'blog',
    'website',
    'automation',
    'subscription',
    'tickets',
    'system_thread',
]

SITE_ID = 1

SILENCED_SYSTEM_CHECKS = ['security.W019', ]

X_FRAME_OPTIONS = "SAMEORIGIN"

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'height': "600",
    'plugins': '''
            emoticons textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            emoticons visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yekjamodir.middleware.blog_middleware.BlogMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://yekjamodir.ir",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
}

ROOT_URLCONF = 'yekjamodir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yekjamodir.wsgi.application'

DATABASES = {}

DATABASE_ROUTERS = ["yekjamodir.db_router.DbRouter", ]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

CSRF_TRUSTED_ORIGINS = ['https://yekjamodir.ir', 'https://*.yekjamodir.ir']

BASE_URL = 'https://panel.yekjamodir.ir'
BASE_CONTENT_URL = 'https://panel.yekjamodir.ir'

# get data from .env
SMS_PANEL_USERNAME = env('SMS_PANEL_USERNAME')
SMS_PANEL_PASSWORD = env('SMS_PANEL_PASSWORD')
STORAGE_QUOTA_LIMIT = int(env('STORAGE_QUOTA_LIMIT'))
ARVAN_CLOUD_API_KEY = env('ARVAN_CLOUD_API_KEY')

ZARINPAL_API_KEY = env('ZARINPAL_API_KEY')