# -*- coding: utf-8 -*-
import datetime
import django.utils.text
import django.utils.timezone
import factory
import factory.django
import factory.fuzzy
import pytz

from platal.profiles import models
from platal.auth import factories as auth_factories


class ProfilePublicNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProfilePublicName

    lastname_initial = factory.Faker('last_name')
    lastname_main = factory.LazyAttribute('{0.lastname_initial}'.format)
    lastname_marital = ''
    lastname_ordinary = ''
    firstname_initial = factory.Faker('first_name')
    firstname_main = factory.LazyAttribute('{0.firstname_initial}'.format)
    firstname_ordinary = ''
    pseudonym = ''


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Profile

    xorg_id = factory.Sequence(lambda n: 19000000 + n)

    birthdate = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(2000, 1, 1, tzinfo=pytz.UTC),
        end_dt=datetime.datetime.now(tz=pytz.UTC))
    birthdate_ref = factory.LazyAttribute(lambda o: o.birthdate)

    deathdate = None

    public_names = factory.RelatedFactory(ProfilePublicNameFactory, 'profile')


class AccountProfileLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AccountProfileLink

    account = factory.SubFactory(auth_factories.AccountFactory)

    @factory.lazy_attribute
    def profile(self):
        # Create a profile once the hruid is known
        return ProfileFactory(
            hrpid=self.account.hruid,
            public_names__lastname_initial=self.account.lastname,
            public_names__firstname_initial=self.account.firstname)
