from .var_env import *

DATABASES={
            'default': {
                'ENGINE': ENGINE,
                'NAME': 'fy2023w30',
                'USER': USER,
                'PASSWORD': PASSWORD,
                'HOST': HOST,
                'PORT': PORT,
            },
            'ipsearch_db_new': {
                'ENGINE': ENGINE,
                'NAME': DBNEWLOCAL,
                'USER': USEROWN,
                'PASSWORD': PASSWORDOWN,
                'HOST': HOSTOWN,
                'PORT': PORT,
            }
        }




