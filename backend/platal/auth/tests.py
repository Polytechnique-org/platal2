# -*- coding: utf-8 -*-
from django.test import TestCase

from platal.auth import factories


class FactoryTest(TestCase):

    def test_account_factory(self):
        factories.AccountFactory()
