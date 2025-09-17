import os
import json
from pathlib import Path
from google.oauth2 import service_account

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['b-detailing.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DetailingBachkatov.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DetailingBachkatov.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC & MEDIA FILES
# -------------------------
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'inicio/static')]

# Configuración por defecto (local)
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración para producción con Google Cloud Storage
GS_BUCKET_NAME = 'archivos-static'

if os.path.exists(os.path.join(BASE_DIR, 'key.json')):
    # Local con archivo
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        os.path.join(BASE_DIR, 'key.json')
    )
elif os.environ.get('GS_CREDENTIALS'):
    # Producción con variable de entorno
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
        json.loads(os.environ['GS_CREDENTIALS'])
    )
else:
    GS_CREDENTIALS = None

if not DEBUG:
    # Usar Google Cloud Storage para estáticos y media en producción
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_DEFAULT_ACL = 'publicRead'
    STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
else:
    # Local con Whitenoise
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

if os.environ.get('FORCE_GCS') == 'True':
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
else:
    if not DEBUG:
        STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    else:
        STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# -------------------------
# Seguridad
# -------------------------
CSRF_TRUSTED_ORIGINS = ['https://b-detailing.onrender.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# -------------------------
# Email
# -------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "bachkatov.detailing@gmail.com"
EMAIL_HOST_PASSWORD = "zled ewvb rzgy pnbr"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
