# coding: utf-8
from django.conf import settings


class SimpleRouter(object):

    def _is_platal1_model(self, model):
        return model.__module__.startswith('platal.')

    def db_for_read(self, model, **hints):
        if self._is_platal1_model(model):
            return 'platal1'
        return None

    def db_for_write(self, model, **hints):
        if self._is_platal1_model(model):
            return 'platal1'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if self._is_platal1_model(obj1) or self._is_platal1_model(obj2):
            return True
        return None

    def allow_migrate(self, db, model):
        if db == 'platal1':
            if self._is_platal1_model(model):
                return settings.PLATAL_MANAGED
            else:
                return False
        else:
            return not self._is_platal1_model(model)
