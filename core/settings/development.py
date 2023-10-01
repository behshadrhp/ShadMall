from .common import *


# Default secret key in debug mode
SECRET_KEY = 'll1*tq$z$%t7-$x@8*ow+*xn-av!swn!aux@)gs!c*jx=1&h64'

# Debug mode
DEBUG = True


# Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

# Default Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
