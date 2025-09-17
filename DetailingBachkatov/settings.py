import os
import json
from pathlib import Path
from google.oauth2 import service_account

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Seguridad básica
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default-key')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['b-detailing.onrender.com', 'localhost', '127.0.0.1']

# -------------------------
# Apps
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # sirve estáticos local
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

# -------------------------
# Database
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Password validation
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# Internacionalización
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC & MEDIA FILES
# -------------------------
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []

GS_BUCKET_NAME = 'archivos-static'

# Credenciales GCS
if os.path.exists(os.path.join(BASE_DIR, 'key.json')):
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        os.path.join(BASE_DIR, 'key.json')
    )
elif os.environ.get('GS_CREDENTIALS'):
    key_dict = json.loads(os.environ['GS_CREDENTIALS'])
    key_dict['private_key'] = key_dict['private_key'].replace('\\n', '\n')
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(key_dict)
else:
    GS_CREDENTIALS = None

# -------------------------
# Decide storage según entorno
# -------------------------
USE_GCS = os.environ.get('USE_GCS', 'false').lower() == 'true'

if USE_GCS or not DEBUG:
    # Subir static y media a GCS
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_DEFAULT_ACL = 'publicRead'
    STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/static/'
    MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/media/'
else:
    # Local con WhiteNoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# Seguridad adicional
# -------------------------
CSRF_TRUSTED_ORIGINS = ['https://b-detailing.onrender.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
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
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
