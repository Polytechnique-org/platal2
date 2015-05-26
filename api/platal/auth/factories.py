import factory
import factory.django

from . import models


class EmailVirtualDomainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EmailVirtualDomain

    name = factory.Faker('domain_name')


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Account

    type = factory.Iterator(models.AccountType.objects.all())

    hruid = factory.Faker('user_name')

    best_domain = factory.SubFactory(EmailVirtualDomainFactory)
    email = factory.LazyAttribute(lambda o: '%s@%s' % (o.hruid, o.best_domain.name))
    from_email = factory.SelfAttribute('email')

    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    full_name = factory.LazyAttribute(lambda o: '%s %s' % (o.firstname, o.lastname))
    directory_name = factory.LazyAttribute(lambda o: '%s %s' % (o.lastname, o.firstname))
    sort_name = factory.SelfAttribute('directory_name')
    display_name = factory.SelfAttribute('full_name')
