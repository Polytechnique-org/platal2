# -*- coding: utf-8 -*-

import hashlib
import hmac

from . import models


class PlatalAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            account = models.Account.objects.get(hruid=username)
        except models.Account.DoesNotExist:
            return None

        pwdhash = hashlib.sha1(password.encode('utf-8')).hexdigest()
        if hmac.compare_digest(account.password, pwdhash):
            return account
        return None

    def get_user(self, user_id):
        return models.Account.objects.get(pk=user_id)
