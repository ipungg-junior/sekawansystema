import os
from service.utils import read_json

# nama akan berganti ke amorequantum by sekawan systema

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'z5=sv8lpp)7-)ysc1-2!^_upigj^=^pj^+gio+7^3-iz+@d2_1'

root_env = read_json('configuration.json')

# Project/Owner conf
APP_NAME = root_env['app_name']
APP_ALIAS_NAME = root_env['app_alias_name']
APP_INDEX_SUBTITLE = root_env['app_index_subtitle']
STORAGE_ALLOCATION = root_env['storage_allocation'] # unit storage MB
COMPANY_ADDRESS = root_env['contact_info']['company_address']
EMAIL = root_env['contact_info']['email']
PHONE_NUMBER = root_env['contact_info']['phone_number']

# Firebase conf
FIREBASE_CREDENTIALS = root_env['firebase_config']['firebase_credentials']
FIREBASE_BUCKET_NAME = root_env['firebase_config']['firebase_bucket_name']

ALLOWED_HOSTS = root_env['web_settings']['allowed_host']

AUTH_USER_MODEL = 'apps.Users'

SECRET_KEY = 'django-insecure-i28tof6w9e6a@+6zq-#-s83(k0$708-n-q*hp1tj49!+czspaq'

DEBUG = root_env['web_settings']['debug']

CSRF_TRUSTED_ORIGINS = ['https://systema.id']

INSTALLED_APPS = [
    'channels',
    'apps',
    'demo',
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = root_env['web_settings']['root_urlconf']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'sekawansystema.wsgi.application'
ASGI_APPLICATION = 'sekawansystema.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Email Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = root_env['mail_server_config']['host']
EMAIL_USE_TLS = root_env['mail_server_config']['tls']
EMAIL_PORT = root_env['mail_server_config']['port']
EMAIL_HOST_USER = root_env['mail_server_config']['user']
EMAIL_HOST_PASSWORD = root_env['mail_server_config']['password']


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True


'''
    Note for production:
        - change static root path with absolute path on vps/dedicated server
'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# during development add this line
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'