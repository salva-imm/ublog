from .settings import *  # noqa
from datetime import timedelta

DEBUG = True
ALLOWED_HOSTS = ['*']

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=8),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
