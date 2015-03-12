# coding: utf-8

class SimpleRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'profiles':
            return 'platal1'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'profiles':
            return 'platal1'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'profiles' or obj2._meta.app_label == 'profiles':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'platal1' or model._meta.app_label == 'profiles':
            return False
        return None

