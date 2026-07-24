"""
Django settings for project_realms project.
"""

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# SEGURANÇA
# =====================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-dev-key"
)


DEBUG = os.environ.get("DEBUG", "False") == "True"


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "realmify.onrender.com",
]


CSRF_TRUSTED_ORIGINS = [
    "https://realmify.onrender.com",
]


# =====================================================
# APLICAÇÕES
# =====================================================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'usuario_realms',
    'crono_realms',
    'biblioteca_realms',
    'list_realms',
    'cronograma_realms',
]


# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # arquivos estáticos no deploy
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'project_realms.urls'


# =====================================================
# TEMPLATES
# =====================================================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(BASE_DIR,'templates')
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'usuario_realms.context_processors.player_context',

                'biblioteca_realms.context_processors.biblioteca_context',

                'list_realms.context_processors.list_block_current',

                'list_realms.context_processors.list_todo_progress',

                'crono_realms.context_processors.realm_context',
            ],
        },
    },
]


WSGI_APPLICATION = 'project_realms.wsgi.application'


# =====================================================
# DATABASE
# =====================================================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': os.environ.get(
            "DB_NAME",
            "study_banck"
        ),

        'USER': os.environ.get(
            "DB_USER",
            "root"
        ),

        'PASSWORD': os.environ.get(
            "DB_PASSWORD",
            "kau12345"
        ),

        'HOST': os.environ.get(
            "DB_HOST",
            "127.0.0.1"
        ),

        'PORT': os.environ.get(
            "DB_PORT",
            "3306"
        ),
    }
}


# =====================================================
# VALIDADORES DE SENHA
# =====================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =====================================================
# IDIOMA
# =====================================================

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_TZ = True


# =====================================================
# ARQUIVOS ESTÁTICOS
# =====================================================

STATIC_URL = 'static/'


STATICFILES_DIRS = [

    os.path.join(BASE_DIR,'templates/static')

]


STATIC_ROOT = BASE_DIR / "staticfiles"


# Compressão do WhiteNoise
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# =====================================================
# MEDIA
# =====================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =====================================================
# LOGIN
# =====================================================

LOGIN_URL = "login"