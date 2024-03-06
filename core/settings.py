
import dj_database_url
from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # django default setting
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # heroku setting


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = 'django-insecure-2mf9u_3ez42$zh+q^7dp%&f!fvrk7s$(*#&-329f_3ae!1bypt'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG = True

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic' # needed in production for static f
    'coreapi',
		'corsheaders',
    'rest_framework',
    'phonenumber_field',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'establishments',
    'categories',
    'products',
    'events',
    'places',
    'users',
    'blog',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware', # needs to be active for static files in production
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


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'moperclub',
        'USER': 'postgres',
        'PASSWORD': 'moper2712',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# database_url = os.environ.get("DATABASE_URL")
database_url_render = "postgres://moperclub_postgresql_database_user:BOszy84qv6Pr8gNDFpRoju5V7840ipSx@dpg-cnfnjn2cn0vc73ari7fg-a.oregon-postgres.render.com/moperclub_postgresql_database"
database_url_heroku = "postgres://ueg44p26gpk9sl:pa6b66fc63e8be9b7747b1d07ae9eaf1da1ac94872f49d4b9b5e7820ecadb0d34@ceu9lmqblp8t3q.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d9n60gekl7j738"
DATABASES['default'] = dj_database_url.parse(database_url_heroku)

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
	"http://localhost:5173"
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# setting up the url for the static an img files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" # heroku setting
# STATIC_ROOT = "staticfiles"

# creating the url for the images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# just to be sure
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_DIRS = (
  os.path.join(BASE_DIR, 'static')
)

try: 
  from .local_settings import DATABASES, DEBUG
except ImportError as Error:
  print("Error:", Error.msg)