from .base import *

print('production.py')
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ALLOWED_HOSTS = []
# DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']


# Конфигурация сервера электронной почты
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '') # 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '') # 'your_password'

