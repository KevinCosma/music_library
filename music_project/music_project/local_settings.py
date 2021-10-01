# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--l!*#60*xq((qvh0@5-x_r3)418p39ap*uylohb4^@!y2bn=vr'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_project',
        'USER': 'root',
        'PASSWORD': 'P!rateKing92',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}