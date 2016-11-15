# coding: utf-8
from django.conf import settings
import django.apps


class SimpleRouter(object):

    @staticmethod
    def _is_platal1_app(app_label):
        appcfg = django.apps.apps.get_app_config(app_label)
        return appcfg.module.__name__.startswith('platal.')

    @staticmethod
    def _is_platal1_model(model):
        # Django migrations use __fake__ objects, unrelated to the real module.
        # So find the App which holds the module and find out whether the app
        # lies in the platal namespace.
        return SimpleRouter._is_platal1_app(model._meta.app_label)

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

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'platal1':
            if self._is_platal1_app(app_label):
                return settings.PLATAL_MANAGED
            else:
                return False
        else:
            return not self._is_platal1_app(app_label)
