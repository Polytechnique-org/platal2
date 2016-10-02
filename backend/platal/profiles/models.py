from django.conf import settings
from django.db import models

class AccountProfileLink(models.Model):
    account = models.ForeignKey('auth.Account', db_column='uid', related_name='profile_links', primary_key=True)
    profile = models.ForeignKey('Profile', db_column='pid', related_name='account_links')
    perms = models.CharField(max_length=5)

    class Meta:
        managed = settings.PLATAL_MANAGED
        db_table = 'account_profiles'
        unique_together = (('account', 'profile'),)

    def __str__(self):
        return '%s -> %s' % (self.account.hruid, self.profile.hrpid)


class Profile(models.Model):
    pid = models.AutoField(primary_key=True)

    accounts = models.ManyToManyField('auth.Account', through=AccountProfileLink, related_name='profiles')

    hrpid = models.CharField(unique=True, max_length=255)
    xorg_id = models.IntegerField()
    ax_id = models.CharField(max_length=8, blank=True)

    last_change = models.DateField(auto_now=True)

    birthdate = models.DateField(blank=True, null=True)
    birthdate_ref = models.DateField(blank=True, null=True)
    next_birthday = models.DateField(blank=True, null=True)

    deathdate = models.DateField(blank=True, null=True)
    deathdate_rec = models.DateField(blank=True, null=True)

    title = models.CharField(max_length=4)
    sex = models.CharField(max_length=6)
    #nationality1 = models.ForeignKey(GeolocCountries, db_column='nationality1', blank=True, null=True)
    #nationality2 = models.ForeignKey(GeolocCountries, db_column='nationality2', blank=True, null=True)
    #nationality3 = models.ForeignKey(GeolocCountries, db_column='nationality3', blank=True, null=True)
    email_directory = models.CharField(max_length=255, blank=True)

    #section = models.ForeignKey(ProfileSectionEnum, db_column='section', blank=True, null=True)

    cv = models.TextField(blank=True)
    freetext = models.TextField(blank=True)
    axfreetext = models.TextField(blank=True)
    freetext_pub = models.CharField(max_length=7)

    medals_pub = models.CharField(max_length=7)
    alias_pub = models.CharField(max_length=7)

    class Meta:
        managed = settings.PLATAL_MANAGED
        db_table = 'profiles'

    def __str__(self):
        return self.hrpid


class ProfilePublicName(models.Model):
    profile = models.OneToOneField('Profile', db_column='pid', primary_key=True, related_name='public_names')
    lastname_initial = models.CharField(max_length=255)
    lastname_main = models.CharField(max_length=255)
    lastname_marital = models.CharField(max_length=255)
    lastname_ordinary = models.CharField(max_length=255)
    firstname_initial = models.CharField(max_length=255)
    firstname_main = models.CharField(max_length=255)
    firstname_ordinary = models.CharField(max_length=255)
    pseudonym = models.CharField(max_length=255)

    class Meta:
        managed = settings.PLATAL_MANAGED
        db_table = 'profile_public_names'

    def __str__(self):
        return "Names of %s" % self.profile


class ProfilePhoto(models.Model):
    profile = models.OneToOneField('Profile', db_column='pid', primary_key=True, related_name='photo')
    attachmime = models.CharField(max_length=4)
    attach = models.BinaryField()
    x = models.IntegerField()
    y = models.IntegerField()
    pub = models.CharField(max_length=7)
    last_update = models.DateTimeField()

    class Meta:
        managed = settings.PLATAL_MANAGED
        db_table = 'profile_photos'

    def __str__(self):
        return self.profile.hrpid


class ProfileDisplay(models.Model):
    profile = models.OneToOneField(Profile, db_column='pid', primary_key=True, related_name='profile_display')
    yourself = models.CharField(max_length=255)
    public_name = models.CharField(max_length=255)
    private_name = models.CharField(max_length=255)
    directory_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    promo = models.CharField(max_length=255)

    class Meta:
        managed = settings.PLATAL_MANAGED
        db_table = 'profile_display'

    def __str__(self):
        return self.profile.hrpid

