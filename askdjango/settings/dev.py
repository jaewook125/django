#현재 공간에 있는 common을 다 가지고오겠다.
#개발용 settings이다
from .common import *


INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
