from django.core.management.base import BaseCommand, CommandError

from platal.auth.factories import *

class Command(BaseCommand):
    help = 'Populates the database with generated data. Can be called several times.'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--accounts', metavar='N', type=int, default=100,
                                   help='number of accounts to create')

    def handle(self, *args, **options):
        acc = options['accounts']
        AccountFactory.create_batch(acc)
