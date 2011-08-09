import os
import sys
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'reggit.settings'

path = '/www/'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
