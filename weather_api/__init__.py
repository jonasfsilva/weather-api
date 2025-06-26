from __future__ import absolute_import, unicode_literals

# Importa o celery quando o Django inicia
from .celery import app as celery

__all__ = ('celery',)