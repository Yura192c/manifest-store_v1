from .base import *  # подгружаем настройки по умолчанию

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_=9yxshg3*kxp8djiwk$#lv%fft8d=5qpe(m@er3d81s2-#%km'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

print('development.py')
