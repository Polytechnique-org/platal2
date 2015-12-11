# -*- coding: utf-8 -*-
import datetime
import django.utils.text
import django.utils.timezone
import factory
import factory.django
import factory.fuzzy
import pytz

from platal.auth import models


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Account

    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    full_name = factory.LazyAttribute('{0.firstname} {0.lastname}'.format)
    directory_name = factory.LazyAttribute('{0.firstname} {0.lastname}'.format)
    sort_name = factory.LazyAttribute('{0.lastname} {0.firstname}'.format)
    display_name = factory.LazyAttribute('{0.firstname} {0.lastname}'.format)
    sex = factory.fuzzy.FuzzyChoice(['female', 'male'])

    registration_date = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(2000, 1, 1, tzinfo=pytz.UTC),
        end_dt=datetime.datetime.now(tz=pytz.UTC))

    @factory.lazy_attribute_sequence
    def hruid(self, n):
        clean_firstname = django.utils.text.slugify(self.firstname)
        clean_lastname = django.utils.text.slugify(self.lastname)
        return '{}.{}.{}'.format(clean_firstname, clean_lastname, n)
