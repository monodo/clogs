"""
Django settings for clogs project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from django.conf import settings

# Set environment mode
ENV = os.getenv("ENV")
if ENV not in ["DEV", "PROD"]:
    raise Exception(
        f"Incorrect setting for ENV: `{ENV}`. Expecting one of `DEV` or `PROD`."
    )
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if ENV == "DEV":
    DEBUG = True

ROOT_URLCONF = "clogs.urls"
PREFIX_URL = os.environ.get("PREFIX_URL", "")
CLEAR_PUBLIC_SCHEMA_ON_FIXTURIZE = os.getenv("CLEAR_PUBLIC_SCHEMA_ON_FIXTURIZE")


SECURE_PROXY_SSL_HEADER = (
    tuple(os.getenv("SECURE_PROXY_SSL_HEADER").split(","))
    if os.getenv("SECURE_PROXY_SSL_HEADER")
    else None
)

# This is django's default but make sure no one turns it to False
SESSION_COOKIE_HTTPONLY = True
SITE_HTTPS = ENV == "PROD"

# Allow CORS in DEV, useful for development
if ENV == "DEV":
    SESSION_COOKIE_HTTPONLY = False
    CORS_ALLOW_CREDENTIALS = True

LOCAL_TIME_ZONE_UTC = int(os.getenv("LOCAL_TIME_ZONE_UTC", +1))

# Highest level of security is 'Strict'
SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE", "Strict")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")


# SESSION TIMEOUT
# default session time is one hour
SESSION_COOKIE_AGE = int(os.getenv("SESSION_COOKIE_AGE", 60 * 60))
SESSION_SAVE_EVERY_REQUEST = os.getenv("SESSION_SAVE_EVERY_REQUEST", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS").lower() == "true"
EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
    if os.getenv("EMAIL_TO_CONSOLE").lower() == "false"
    else "django.core.mail.backends.console.EmailBackend"
)

DEFAULT_CHARSET = "utf-8"

SITE_ID = None
SITE_DOMAIN = os.getenv("SITE_DOMAIN", None)
# Default domain on which all forms could be made visible by any integrator
DEFAULT_SITE = os.getenv("DEFAULT_SITE")

# 2FA activation
ENABLE_2FA = os.getenv("ENABLE_2FA", "false").lower() == "true"

# Application definition

INSTALLED_APPS = [
    # our apps
    "clogs.core",
    "clogs.users",
    "clogs.themes",
    "django_oapif",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "rest_framework",
    "rest_framework_gis",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "computedfields",
    "migrate_sql",
]

if ENABLE_2FA:
    INSTALLED_APPS += [
        "django_otp",
        "django_otp.plugins.otp_static",
        "django_otp.plugins.otp_totp",
        "two_factor",
    ]

if ENV == "DEV":
    INSTALLED_APPS += [
        "debug_toolbar",
        "django_extensions",
    ]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

if ENABLE_2FA:
    MIDDLEWARE += ["django_otp.middleware.OTPMiddleware"]

MIDDLEWARE += [
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

if ENV == "DEV":
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

ROOT_URLCONF = "clogs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = "clogs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("PGDATABASE"),
        "USER": os.getenv("PGUSER"),
        "HOST": os.getenv("PGHOST"),
        "PORT": os.getenv("PGPORT"),
        "PASSWORD": os.getenv("PGPASSWORD"),
        "OPTIONS": {"options": "-c search_path=clogs,public"},
    }
}

AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CORS_ALLOWED_ORIGINS = [] + os.getenv("ALLOWED_CORS").split(",")

if DEBUG and not CORS_ALLOWED_ORIGINS:
    CORS_ALLOW_ALL_ORIGINS = True

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "fr-CH"
TIME_ZONE = "Europe/Zurich"
USE_I18N = True
USE_L10N = True
USE_TZ = True

gettext = lambda x: x

LANGUAGES = (
    ("fr", gettext("French")),
    ("en", gettext("English")),
    ("de", gettext("German")),
    ("it", gettext("Italian")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
STATIC_URL = os.environ["STATIC_URL"]
STATIC_ROOT = "/static_root"

# OAUTH2 Config
OAUTH2_PROVIDER = {
    "PKCE_REQUIRED": os.getenv("OAUTH2_PKCE_REQUIRED", "false").lower() == "true"
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


def show_toolbar(request):
    """Shows the debug toolbar when DEBUG is enabled."""
    return settings.DEBUG


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "clogs.settings.show_toolbar",
    "DISABLE_PANELS": {
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
