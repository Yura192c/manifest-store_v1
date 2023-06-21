from .base import *  # подгружаем настройки по умолчанию

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_=9yxshg3*kxp8djiwk$#lv%fft8d=5qpe(m@er3d81s2-#%km'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS += ['127.0.0.1', 'localhost']
print('development.py')

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
try:
    from .local_settings import *

    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', LOC_EMAIL_HOST_USER)  # 'your_account@gmail.com'
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', LOC_EMAIL_HOST_PASSWORD)  # 'your_password'

except ImportError:
    print('local_settings.py does not exist')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# IMPORT EXPORT
IMPORT_EXPORT_SKIP_ADMIN_CONFIRM = True
IMPORT_EXPORT_USE_TRANSACTIONS = False
IMPORT_EXPORT_SKIP_ADMIN_LOG = True
