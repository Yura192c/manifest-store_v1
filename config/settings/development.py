from .base import *  # подгружаем настройки по умолчанию

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
