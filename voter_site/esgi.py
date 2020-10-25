import os
import sys
sys.path.append('/opt/bitnami/projects/tutorial')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/tutorial/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
