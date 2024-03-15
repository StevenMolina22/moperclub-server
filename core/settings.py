
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # django default setting
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # heroku setting

load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('HOST_PRODUCTION'), 'localhost', '127.0.0.1', '.vercel.app']
# ALLOWED_HOSTS = ["*"]

# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG = os.environ.get('DEBUG', 'False') == 'True'


INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic' # needed in production for static f
    'coreapi',
		'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.sites' # for getting the current host
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "storages",
    'establishments',
    'categories',
    'products',
    'events',
    'places',
    'users',
    'blog',
    'home',
    'utils',
    'phonenumber_field',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # needs to be active for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware", # corsheaders
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
}
# database_url = os.environ.get("DATABASE_URL")
DATABASES['default'] = dj_database_url.parse(os.environ.get("HEROKU_DB_URL"))


# --- AWS configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# -- aws storage configuration
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False

# -- S3 Buckets configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE  = 'storages.backends.s3boto3.S3Boto3Storage'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


# for the docs
REST_FRAMEWORK = {
    # ...: ...,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}


# for connecting front and back
CORS_ALLOWED_ORIGINS = [
	os.environ.get("LOCAL_CLIENT_HOST"),
  os.environ.get("PRODUCTION_CLIENT_HOST"),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# setting up the url for the static an img files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" # heroku  static files setting
# STATIC_ROOT = "staticfiles"

# creating the url for the images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---- for custom static files 
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATIC_DIRS = (
#   os.path.join(BASE_DIR, 'static')
# )

try: 
  from .local_settings import DATABASES, DEBUG
except ImportError as Error:
  print("Error:", Error.msg)