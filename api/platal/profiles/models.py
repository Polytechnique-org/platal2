from django.db import models


class AccountTypes(models.Model):
    type = models.CharField(primary_key=True, max_length=16)
    perms = models.CharField(max_length=124)
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'account_types'

    def __str__(self):
        return self.type


class EmailVirtualDomains(models.Model):
    name = models.CharField(max_length=255)
    aliasing = models.ForeignKey('self', db_column='aliasing')

    class Meta:
        managed = False
        db_table = 'email_virtual_domains'

    def __str__(self):
        return self.name


class Account(models.Model):
    uid = models.AutoField(primary_key=True)

    hruid = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=40, blank=True)
    token = models.CharField(max_length=32, blank=True)
    weak_password = models.CharField(max_length=256, blank=True)

    type = models.ForeignKey(AccountTypes, db_column='type', blank=True, null=True)

    user_perms = models.CharField(max_length=96, blank=True)
    is_admin = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=8)
    flags = models.CharField(max_length=5)

    registration_date = models.DateTimeField()

    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    directory_name = models.CharField(max_length=255, blank=True)
    sort_name = models.CharField(max_length=255, blank=True)
    display_name = models.CharField(max_length=255, blank=True)

    email = models.CharField(max_length=255, blank=True)
    best_domain = models.ForeignKey('EmailVirtualDomains', db_column='best_domain', blank=True, null=True)
    from_email = models.CharField(max_length=255)
    from_format = models.CharField(max_length=4)

    sex = models.CharField(max_length=6)
    comment = models.CharField(max_length=255, blank=True)

    email_format = models.CharField(max_length=4)
    skin = models.ForeignKey('Skins', db_column='skin', blank=True, null=True)
    last_version = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'accounts'

    def __str__(self):
        return self.hruid
