from .var_env import *

DATABASES={  
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'dblocal_default',  
                'USER': USEROWN,
                'PASSWORD': PASSWORDOWN, 
                'HOST': HOSTOWN,
                'PORT': PORT,
            },
            'dblocal_mantto': {
                'ENGINE': ENGINE,
                'NAME': 'dblocal_mantto',
                'USER': USEROWN,
                'PASSWORD': PASSWORDOWN, 
                'HOST': HOSTOWN,
                'PORT': PORT,
            },
            'ipsearch_db_new': {
                'ENGINE': ENGINE,
                'NAME': "",
                'USER': USEROWN,
                'PASSWORD': PASSWORDOWN,
                'HOST': HOSTOWN,
                'PORT': PORT,
            },
        }