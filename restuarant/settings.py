import os
from pathlib import Path

# ==================================================
# BASE DIR
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# SECURITY
# ==================================================
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key-change-me")

DEBUG = os.getenv("DEBUG", "True").lower() in ("1", "true", "yes", "y")

ALLOWED_HOSTS = [
    h.strip()
    for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost,69.164.245.17").split(",")
    if h.strip()
]

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.getenv(
        "CSRF_TRUSTED_ORIGINS",
        "http://127.0.0.1,http://localhost,http://69.164.245.17:8002",
    ).split(",")
    if o.strip()
]


# ==================================================
# APPLICATIONS
# ==================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # your app
    "home",
    "menu"
]


# ==================================================
# MIDDLEWARE
# ==================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # SERVE STATIC FILES IN PRODUCTION
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS
# ==================================================
ROOT_URLCONF = "restuarant.urls"


# ==================================================
# TEMPLATES
# ==================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # we use templates inside apps
        "DIRS": [],

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


# ==================================================
# WSGI
# ==================================================
WSGI_APPLICATION = "restuarant.wsgi.application"


# ==================================================
# DATABASE
# ==================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==================================================
# PASSWORD VALIDATION
# ==================================================
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


# ==================================================
# INTERNATIONALIZATION
# ==================================================
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ==================================================
# STATIC FILES (CSS / JS / IMAGES / VIDEO)
# ==================================================
STATIC_URL = "/static/"

# collectstatic destination
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise compressed files
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# ==================================================
# MEDIA FILES (uploads)
# ==================================================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"