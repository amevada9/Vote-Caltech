
"""
WSGI config for personal_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voter_site.settings')
sys.path.append('/opt/bitnami/vote_caltech/Voter-Caltech')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/vote_caltech/Vote-Caltech/egg_cache")

application = get_wsgi_application()
