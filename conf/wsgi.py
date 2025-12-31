import os
import sys

# Loyihangizning asosiy papkasi
path = '/home/Qudratullaeev/BlogSite'
if path not in sys.path:
    sys.path.append(path)

# DIQQAT: settings fayli conf papkasida bo'lgani uchun conf.settings deb yozamiz
os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()