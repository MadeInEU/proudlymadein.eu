import os
import sys

sys.path.append('/usr/local/lib/python2.7/django/')
sys.path.append('/usr/local/lib/python2.7/site-packages/')
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'MadeInEU.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
