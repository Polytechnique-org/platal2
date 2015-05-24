# -*- coding: utf-8 -*-

from django.core.management import base
from django.db import models
from django.db import transaction
from django.utils import importlib


class Command(base.LabelCommand):
    help = "Load one or more datasets into the database, defined in <app>/fixtures/."
    args = "<app>.<dataset_name>[, <app>.<dataset_name>[, ...]]"

    def handle_label(self, label, **options):
        verbosity = int(options.get('verbosity', 0))

        if verbosity > 0:
            self.stdout.write("Importing dataset %s..." % (label,))

        if label.count('.') != 1:
            raise ValueError("Invalid dataset name %s; expected <app>.<module> for app/fixtures/module.py" % label)

        app, name = label.split('.')
        app_models_name = models.get_app(app).__name__  # platal.auth.models
        dataset_module_name = app_models_name.replace('models', 'fixtures.%s' % name)
        dataset_module = importlib.import_module(dataset_module_name)

        with transaction.atomic():
            loaded_objects = dataset_module.run()

        if verbosity > 0:
            self.stdout.write("  OK (handled %d objects).\n" % len(loaded_objects))
