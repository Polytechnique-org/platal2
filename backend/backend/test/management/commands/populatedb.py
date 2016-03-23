from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

import hashlib

from platal.auth.factories import *
from platal.auth.models import Account

class Command(BaseCommand):
    help = 'Populates the database with generated data. Can be called several times.'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--accounts', metavar='N', type=int, default=100,
                                   help='number of accounts to create')

    def handle(self, *args, **options):
        test_user = settings.TEST_USER.copy()
        test_user['password'] = hashlib.sha1(test_user['password'].encode('utf-8')).hexdigest()
        user = AccountFactory.build(**test_user)
        try: # Update test user if possible. If not, create it
            u = Account.objects.get(hruid=user.hruid)
            for k, v in test_user.items():
                setattr(u, k, v)
            u.save()
            print("Test user updated, hruid is '{}' and password is '{}'".format(user.hruid, settings.TEST_USER['password']))
        except Account.DoesNotExist:
            user.save()
            print("Test user created, hruid is '{}' and password is '{}'".format(user.hruid, settings.TEST_USER['password']))

        acc = options['accounts']
        AccountFactory.create_batch(acc)
