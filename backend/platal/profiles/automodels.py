# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccountAuthOpenid(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey('Accounts', db_column='uid', blank=True, null=True)
    url = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'account_auth_openid'


class AccountLostPasswords(models.Model):
    certificat = models.CharField(primary_key=True, max_length=32)
    uid = models.ForeignKey('Accounts', db_column='uid', blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_lost_passwords'


class AccountProfiles(models.Model):
    uid = models.ForeignKey('Accounts', db_column='uid')
    pid = models.ForeignKey('Profiles', db_column='pid')
    perms = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'account_profiles'


class AccountTypes(models.Model):
    type = models.CharField(primary_key=True, max_length=16)
    perms = models.CharField(max_length=124)
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'account_types'


class AccountXnetLostPasswords(models.Model):
    uid = models.ForeignKey('Accounts', db_column='uid', primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    hash = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'account_xnet_lost_passwords'


class Accounts(models.Model):
    uid = models.IntegerField(primary_key=True)
    hruid = models.CharField(unique=True, max_length=255)
    type = models.ForeignKey(AccountTypes, db_column='type', blank=True, null=True)
    user_perms = models.CharField(max_length=96, blank=True)
    is_admin = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=8)
    password = models.CharField(max_length=40, blank=True)
    token = models.CharField(max_length=32, blank=True)
    weak_password = models.CharField(max_length=256, blank=True)
    registration_date = models.DateTimeField()
    flags = models.CharField(max_length=5)
    comment = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    directory_name = models.CharField(max_length=255, blank=True)
    sort_name = models.CharField(max_length=255, blank=True)
    display_name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=6)
    email_format = models.CharField(max_length=4)
    skin = models.ForeignKey('Skins', db_column='skin', blank=True, null=True)
    last_version = models.CharField(max_length=16)
    best_domain = models.ForeignKey('EmailVirtualDomains', db_column='best_domain', blank=True, null=True)
    from_email = models.CharField(max_length=255)
    from_format = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'accounts'


class AnnouncePhotos(models.Model):
    eid = models.ForeignKey('Announces', db_column='eid', primary_key=True)
    attachmime = models.CharField(max_length=4)
    attach = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'announce_photos'


class AnnounceRead(models.Model):
    evt = models.ForeignKey('Announces')
    uid = models.ForeignKey(Accounts, db_column='uid')

    class Meta:
        managed = False
        db_table = 'announce_read'


class Announces(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    creation_date = models.DateTimeField()
    titre = models.CharField(max_length=255)
    texte = models.TextField()
    expiration = models.DateField()
    promo_min = models.IntegerField()
    promo_max = models.IntegerField()
    flags = models.CharField(max_length=29)
    noinvite = models.IntegerField()
    post_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announces'


class Axletter(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    short_name = models.CharField(unique=True, max_length=16, blank=True)
    subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    signature = models.TextField()
    promo_min = models.IntegerField()
    promo_max = models.IntegerField()
    subset = models.TextField(blank=True)
    subset_rm = models.IntegerField(blank=True, null=True)
    echeance = models.DateTimeField()
    date = models.DateField()
    bits = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'axletter'


class Carvas(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'carvas'


class Contacts(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    contact = models.ForeignKey('Profiles', db_column='contact')

    class Meta:
        managed = False
        db_table = 'contacts'


class Downtimes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    debut = models.DateTimeField()
    duree = models.TimeField()
    resume = models.CharField(max_length=255)
    description = models.TextField()
    services = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'downtimes'


class EmailListModerate(models.Model):
    ml = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    mid = models.IntegerField()
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    action = models.CharField(max_length=6)
    ts = models.DateTimeField()
    message = models.TextField(blank=True)
    handler = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_list_moderate'


class EmailRedirectAccount(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    redirect = models.CharField(max_length=255)
    rewrite = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    action = models.CharField(max_length=18)
    broken_date = models.DateField()
    broken_level = models.IntegerField()
    last = models.DateField()
    flags = models.CharField(max_length=8)
    hash = models.CharField(max_length=32, blank=True)
    allow_rewrite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_redirect_account'


class EmailRedirectOther(models.Model):
    hrmid = models.ForeignKey('EmailSourceOther', db_column='hrmid')
    redirect = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    action = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'email_redirect_other'


class EmailSendSave(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'email_send_save'


class EmailSourceAccount(models.Model):
    email = models.CharField(max_length=255)
    domain = models.ForeignKey('EmailVirtualDomains', db_column='domain')
    uid = models.ForeignKey(Accounts, db_column='uid')
    type = models.CharField(max_length=9)
    flags = models.CharField(max_length=23)
    expire = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_source_account'


class EmailSourceOther(models.Model):
    email = models.CharField(max_length=255)
    domain = models.ForeignKey('EmailVirtualDomains', db_column='domain')
    hrmid = models.CharField(max_length=255)
    type = models.CharField(max_length=8, blank=True)
    expire = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_source_other'


class EmailVirtual(models.Model):
    email = models.CharField(max_length=255)
    domain = models.ForeignKey('EmailVirtualDomains', db_column='domain')
    redirect = models.CharField(max_length=255)
    type = models.CharField(max_length=7, blank=True)
    expire = models.DateField()

    class Meta:
        managed = False
        db_table = 'email_virtual'


class EmailVirtualDomains(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    aliasing = models.ForeignKey('self', db_column='aliasing')

    class Meta:
        managed = False
        db_table = 'email_virtual_domains'


class EmailWatch(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    state = models.CharField(max_length=9)
    detection = models.DateField(blank=True, null=True)
    last = models.DateTimeField()
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'email_watch'


class ForumInnd(models.Model):
    id_innd = models.IntegerField(primary_key=True)
    ipmin = models.IntegerField(blank=True, null=True)
    ipmax = models.IntegerField(blank=True, null=True)
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    read_perm = models.CharField(max_length=100, blank=True)
    write_perm = models.CharField(max_length=100, blank=True)
    priority = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'forum_innd'


class ForumProfiles(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    name = models.CharField(max_length=64)
    mail = models.CharField(max_length=70)
    sig = models.TextField()
    flags = models.CharField(max_length=21)
    tree_unread = models.CharField(max_length=8)
    tree_read = models.CharField(max_length=8)
    last_seen = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forum_profiles'


class ForumSubs(models.Model):
    fid = models.ForeignKey('Forums', db_column='fid')
    uid = models.ForeignKey(Accounts, db_column='uid')

    class Meta:
        managed = False
        db_table = 'forum_subs'


class Forums(models.Model):
    fid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'forums'


class FusionaxActivites(models.Model):
    ac = models.CharField(db_column='AC', max_length=2)  # Field name made lowercase.
    ax_id = models.CharField(max_length=8)
    code_etab = models.BigIntegerField(db_column='Code_etab')  # Field name made lowercase.
    raison_sociale = models.CharField(db_column='Raison_sociale', max_length=255)  # Field name made lowercase.
    libelle_fonctio = models.CharField(db_column='Libelle_fonctio', max_length=255)  # Field name made lowercase.
    annuaire = models.IntegerField(db_column='Annuaire')  # Field name made lowercase.
    date_maj = models.DateField(db_column='Date_maj')  # Field name made lowercase.
    pid = models.IntegerField(blank=True, null=True)
    jobid = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'fusionax_activites'


class FusionaxAdresses(models.Model):
    provenance = models.CharField(max_length=2)
    ax_id = models.CharField(max_length=8)
    type_adr = models.CharField(db_column='Type_adr', max_length=1)  # Field name made lowercase.
    ligne1 = models.CharField(db_column='Ligne1', max_length=90)  # Field name made lowercase.
    ligne2 = models.CharField(db_column='Ligne2', max_length=90)  # Field name made lowercase.
    ligne3 = models.CharField(db_column='Ligne3', max_length=90)  # Field name made lowercase.
    code_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=80)
    zip_cedex = models.CharField(max_length=20)
    etat_distr = models.CharField(max_length=20)
    pays = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    date_maj = models.DateField(db_column='Date_maj')  # Field name made lowercase.
    code_etab = models.BigIntegerField(db_column='Code_etab', blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(blank=True, null=True)
    jobid = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'fusionax_adresses'


class FusionaxAnciens(models.Model):
    an = models.CharField(db_column='AN', max_length=2)  # Field name made lowercase.
    ax_id = models.CharField(primary_key=True, max_length=8)
    promotion_etude = models.IntegerField()
    groupe_promo = models.CharField(max_length=1)
    nom_patronymique = models.CharField(db_column='Nom_patronymique', max_length=255)  # Field name made lowercase.
    partic_patro = models.CharField(max_length=5)
    prenom = models.CharField(max_length=30)
    nom_usuel = models.CharField(db_column='Nom_usuel', max_length=255)  # Field name made lowercase.
    partic_nom = models.CharField(max_length=5)
    nom_complet = models.CharField(db_column='Nom_complet', max_length=255)  # Field name made lowercase.
    civilite = models.CharField(db_column='Civilite', max_length=4)  # Field name made lowercase.
    code_nationalite = models.CharField(db_column='Code_nationalite', max_length=4)  # Field name made lowercase.
    corps_sortie = models.CharField(max_length=50)
    date_deces = models.DateField(db_column='Date_deces', blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(max_length=50)
    mel_usage = models.CharField(db_column='Mel_usage', max_length=255)  # Field name made lowercase.
    mel_publiable = models.IntegerField(db_column='Mel_publiable')  # Field name made lowercase.
    mob_publiable = models.IntegerField(db_column='Mob_publiable')  # Field name made lowercase.
    tel_mobile = models.CharField(max_length=30)
    date_maj = models.DateField(db_column='Date_maj')  # Field name made lowercase.
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_anciens'


class FusionaxDeceased(models.Model):
    pid = models.IntegerField()
    ax_id = models.CharField(max_length=8)
    private_name = models.CharField(max_length=255)
    promo = models.CharField(max_length=255)
    deces_xorg = models.DateField(blank=True, null=True)
    deces_ax = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_deceased'


class FusionaxEntreprises(models.Model):
    en = models.CharField(db_column='EN', max_length=2)  # Field name made lowercase.
    code_etab = models.BigIntegerField(db_column='Code_etab', primary_key=True)  # Field name made lowercase.
    raison_sociale = models.CharField(db_column='Raison_sociale', max_length=255)  # Field name made lowercase.
    sigle = models.CharField(db_column='Sigle', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fusionax_entreprises'


class FusionaxFormations(models.Model):
    date_maj = models.DateField(db_column='Date_maj')  # Field name made lowercase.
    fo = models.CharField(db_column='FO', max_length=2)  # Field name made lowercase.
    ax_id = models.CharField(max_length=8)
    intitule_formation = models.CharField(db_column='Intitule_formation', max_length=255)  # Field name made lowercase.
    intitule_diplome = models.CharField(db_column='Intitule_diplome', max_length=255)  # Field name made lowercase.
    descr_formation = models.CharField(db_column='Descr_formation', max_length=255)  # Field name made lowercase.
    pid = models.IntegerField(blank=True, null=True)
    eduid = models.IntegerField(blank=True, null=True)
    degreeid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_formations'


class FusionaxFormationsMd(models.Model):
    fo = models.CharField(db_column='FO', max_length=2)  # Field name made lowercase.
    ax_id = models.CharField(primary_key=True, max_length=8)
    field = models.CharField(max_length=255, blank=True)
    pid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_formations_md'


class FusionaxImport(models.Model):
    ax_id = models.CharField(primary_key=True, max_length=8)
    pid = models.IntegerField(blank=True, null=True)
    date_match_id = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_import'


class FusionaxPromo(models.Model):
    pid = models.IntegerField()
    ax_id = models.CharField(max_length=8, blank=True)
    private_name = models.CharField(max_length=255)
    promo = models.CharField(max_length=255)
    promo_etude_xorg = models.IntegerField(blank=True, null=True)
    groupe_promo = models.CharField(max_length=1)
    promo_etude_ax = models.IntegerField()
    promo_sortie_xorg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusionax_promo'


class FusionaxXorgAnciens(models.Model):
    pid = models.IntegerField()
    ax_id = models.CharField(max_length=8, blank=True)
    promo = models.CharField(max_length=255)
    private_name = models.CharField(max_length=255)
    public_name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    directory_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fusionax_xorg_anciens'


class GappsAccounts(models.Model):
    l_userid = models.ForeignKey(Accounts, db_column='l_userid', blank=True, null=True)
    l_sync_password = models.IntegerField(blank=True, null=True)
    l_activate_mail_redirection = models.IntegerField(blank=True, null=True)
    g_account_id = models.CharField(max_length=16, blank=True)
    g_account_name = models.CharField(primary_key=True, max_length=256)
    g_domain = models.CharField(max_length=40, blank=True)
    g_first_name = models.CharField(max_length=40)
    g_last_name = models.CharField(max_length=40)
    g_status = models.CharField(max_length=13, blank=True)
    g_admin = models.IntegerField(blank=True, null=True)
    g_suspension = models.CharField(max_length=256, blank=True)
    r_disk_usage = models.BigIntegerField(blank=True, null=True)
    r_creation = models.DateField(blank=True, null=True)
    r_last_login = models.DateField(blank=True, null=True)
    r_last_webmail = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gapps_accounts'


class GappsNicknames(models.Model):
    l_userid = models.ForeignKey(Accounts, db_column='l_userid', blank=True, null=True)
    g_account_name = models.CharField(max_length=256)
    g_nickname = models.CharField(primary_key=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'gapps_nicknames'


class GappsQueue(models.Model):
    q_id = models.IntegerField(primary_key=True)
    q_owner = models.ForeignKey(Accounts, blank=True, null=True)
    q_recipient = models.ForeignKey(Accounts, blank=True, null=True)
    p_entry_date = models.DateTimeField()
    p_notbefore_date = models.DateTimeField()
    p_start_date = models.DateTimeField(blank=True, null=True)
    p_end_date = models.DateTimeField(blank=True, null=True)
    p_status = models.CharField(max_length=8)
    p_priority = models.CharField(max_length=9)
    p_admin_request = models.IntegerField()
    j_type = models.CharField(max_length=10)
    j_parameters = models.TextField(blank=True)
    r_softfail_date = models.DateTimeField(blank=True, null=True)
    r_softfail_count = models.IntegerField()
    r_result = models.CharField(max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'gapps_queue'


class GappsReporting(models.Model):
    date = models.DateField(primary_key=True)
    num_accounts = models.IntegerField(blank=True, null=True)
    count_1_day_actives = models.IntegerField(blank=True, null=True)
    count_7_day_actives = models.IntegerField(blank=True, null=True)
    count_14_day_actives = models.IntegerField(blank=True, null=True)
    count_30_day_actives = models.IntegerField(blank=True, null=True)
    count_30_day_idle = models.IntegerField(blank=True, null=True)
    count_60_day_idle = models.IntegerField(blank=True, null=True)
    count_90_day_idle = models.IntegerField(blank=True, null=True)
    usage_in_bytes = models.BigIntegerField(blank=True, null=True)
    quota_in_mb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gapps_reporting'


class GeolocCountries(models.Model):
    iso_3166_1_a2 = models.CharField(primary_key=True, max_length=2)
    iso_3166_1_a3 = models.CharField(unique=True, max_length=3)
    iso_3166_1_num = models.IntegerField(unique=True)
    worldregion = models.CharField(db_column='worldRegion', max_length=2, blank=True)  # Field name made lowercase.
    country = models.CharField(max_length=255, blank=True)
    countryen = models.CharField(db_column='countryEn', max_length=255, blank=True)  # Field name made lowercase.
    capital = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255, blank=True)
    nationalityen = models.CharField(db_column='nationalityEn', max_length=255, blank=True)  # Field name made lowercase.
    phoneprefix = models.IntegerField(db_column='phonePrefix', blank=True, null=True)  # Field name made lowercase.
    phoneformat = models.CharField(db_column='phoneFormat', max_length=255)  # Field name made lowercase.
    licenseplate = models.CharField(db_column='licensePlate', max_length=4, blank=True)  # Field name made lowercase.
    belongsto = models.ForeignKey('self', db_column='belongsTo', blank=True, null=True)  # Field name made lowercase.
    countryplain = models.CharField(db_column='countryPlain', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geoloc_countries'


class GeolocLanguages(models.Model):
    iso_3166_1_a2 = models.ForeignKey(GeolocCountries, db_column='iso_3166_1_a2')
    language = models.CharField(max_length=5)
    country = models.CharField(max_length=255, blank=True)
    countryplain = models.CharField(db_column='countryPlain', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geoloc_languages'


class GroupAnnounces(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    asso = models.ForeignKey('Groups')
    create_date = models.DateTimeField()
    titre = models.CharField(max_length=255)
    texte = models.TextField()
    contacts = models.TextField()
    expiration = models.DateField()
    promo_min = models.IntegerField()
    promo_max = models.IntegerField()
    flags = models.CharField(max_length=12)
    post_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_announces'


class GroupAnnouncesPhoto(models.Model):
    eid = models.ForeignKey(GroupAnnounces, db_column='eid', primary_key=True)
    attachmime = models.CharField(max_length=4)
    attach = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_announces_photo'


class GroupAnnouncesRead(models.Model):
    announce = models.ForeignKey(GroupAnnounces)
    uid = models.ForeignKey(Accounts, db_column='uid')

    class Meta:
        managed = False
        db_table = 'group_announces_read'


class GroupAuth(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    privkey = models.CharField(unique=True, max_length=40)
    name = models.CharField(max_length=32)
    datafields = models.CharField(max_length=255)
    returnurls = models.CharField(max_length=255)
    last_used = models.DateField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    flags = models.CharField(max_length=21, blank=True)

    class Meta:
        managed = False
        db_table = 'group_auth'


class GroupDom(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.TextField()
    cat = models.CharField(max_length=39)

    class Meta:
        managed = False
        db_table = 'group_dom'


class GroupEventItems(models.Model):
    eid = models.ForeignKey('GroupEvents', db_column='eid')
    item_id = models.IntegerField()
    titre = models.CharField(max_length=100)
    details = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'group_event_items'


class GroupEventParticipants(models.Model):
    eid = models.ForeignKey(GroupEventItems, db_column='eid')
    uid = models.ForeignKey(Accounts, db_column='uid')
    item = models.ForeignKey(GroupEventItems)
    nb = models.IntegerField()
    flags = models.CharField(max_length=14)
    paid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'group_event_participants'


class GroupEvents(models.Model):
    eid = models.IntegerField(primary_key=True)
    asso = models.ForeignKey('Groups', blank=True, null=True)
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    intitule = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    paiement = models.ForeignKey('Payments', blank=True, null=True)
    descriptif = models.TextField()
    debut = models.DateTimeField()
    fin = models.DateTimeField(blank=True, null=True)
    show_participants = models.IntegerField()
    deadline_inscription = models.DateField(blank=True, null=True)
    noinvite = models.IntegerField()
    accept_nonmembre = models.IntegerField()
    archive = models.IntegerField()
    subscription_notification = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'group_events'


class GroupFormerMembers(models.Model):
    asso = models.ForeignKey('Groups')
    uid = models.ForeignKey(Accounts, db_column='uid')
    remember = models.IntegerField()
    unsubsciption_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'group_former_members'


class GroupMemberSubRequests(models.Model):
    asso = models.ForeignKey('Groups')
    uid = models.ForeignKey(Accounts, db_column='uid')
    ts = models.DateTimeField()
    reason = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'group_member_sub_requests'


class GroupMembers(models.Model):
    asso = models.ForeignKey('Groups')
    uid = models.ForeignKey(Accounts, db_column='uid')
    perms = models.CharField(max_length=6)
    comm = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=18, blank=True)
    flags = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'group_members'


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.CharField(max_length=255)
    diminutif = models.CharField(unique=True, max_length=64)
    cat = models.CharField(max_length=39)
    dom = models.ForeignKey(GroupDom, db_column='dom', blank=True, null=True)
    descr = models.TextField()
    logo = models.TextField(blank=True)
    logo_mime = models.TextField(blank=True)
    site = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    resp = models.CharField(max_length=255)
    forum = models.CharField(max_length=255)
    mail_domain = models.CharField(max_length=255)
    ax = models.IntegerField()
    pub = models.CharField(max_length=7)
    sub_url = models.CharField(max_length=255)
    inscriptible = models.IntegerField()
    unsub_url = models.CharField(max_length=255)
    flags = models.CharField(max_length=39)
    axdate = models.DateField(db_column='axDate', blank=True, null=True)  # Field name made lowercase.
    welcome_msg = models.TextField(blank=True)
    event_order = models.CharField(max_length=8)
    disable_mails = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'groups'


class HomonymsList(models.Model):
    hrmid = models.CharField(max_length=255)
    uid = models.ForeignKey(Accounts, db_column='uid')

    class Meta:
        managed = False
        db_table = 'homonyms_list'


class IpWatch(models.Model):
    state = models.CharField(max_length=9)
    detection = models.DateField(blank=True, null=True)
    last = models.DateTimeField()
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    description = models.TextField()
    ip = models.IntegerField(primary_key=True)
    mask = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ip_watch'


class LogActions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'log_actions'


class LogEvents(models.Model):
    stamp = models.DateTimeField()
    session = models.ForeignKey('LogSessions', db_column='session')
    action = models.ForeignKey(LogActions, db_column='action')
    data = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'log_events'


class LogLastSessions(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    id = models.ForeignKey('LogSessions', db_column='id')

    class Meta:
        managed = False
        db_table = 'log_last_sessions'


class LogSessions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    auth = models.CharField(max_length=6)
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    start = models.DateTimeField()
    host = models.CharField(max_length=128)
    sauth = models.CharField(max_length=6)
    suid = models.ForeignKey(Accounts, db_column='suid', blank=True, null=True)
    browser = models.CharField(max_length=255)
    forward_host = models.CharField(max_length=128, blank=True)
    flags = models.CharField(max_length=5)
    ip = models.IntegerField()
    forward_ip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_sessions'


class MxWatch(models.Model):
    host = models.CharField(primary_key=True, max_length=64)
    state = models.CharField(max_length=7, blank=True)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'mx_watch'


class NewsletterArt(models.Model):
    id = models.ForeignKey('NewsletterIssues', db_column='id')
    aid = models.IntegerField()
    cid = models.ForeignKey('NewsletterCat', db_column='cid', blank=True, null=True)
    pos = models.IntegerField()
    title = models.TextField()
    body = models.TextField()
    append = models.TextField()

    class Meta:
        managed = False
        db_table = 'newsletter_art'


class NewsletterCat(models.Model):
    cid = models.IntegerField(primary_key=True)
    nlid = models.ForeignKey('Newsletters', db_column='nlid')
    pos = models.IntegerField()
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'newsletter_cat'


class NewsletterIns(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    nlid = models.ForeignKey('Newsletters', db_column='nlid')
    last = models.ForeignKey('NewsletterIssues', db_column='last', blank=True, null=True)
    hash = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'newsletter_ins'


class NewsletterIssues(models.Model):
    nlid = models.ForeignKey('Newsletters', db_column='nlid')
    id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.DateField()
    send_before = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=7)
    sufb_json = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    head = models.TextField()
    signature = models.TextField()
    short_name = models.CharField(max_length=16, blank=True)
    mail_title = models.CharField(max_length=255)
    unsubscribe = models.IntegerField()
    reply_to = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'newsletter_issues'


class Newsletters(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(Groups, unique=True)
    name = models.CharField(max_length=255)
    criteria = models.CharField(max_length=14, blank=True)

    class Meta:
        managed = False
        db_table = 'newsletters'


class PaymentBankaccounts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    asso_id = models.IntegerField()
    iban = models.CharField(max_length=33)
    bic = models.CharField(max_length=11)
    owner = models.CharField(max_length=100)
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'payment_bankaccounts'


class PaymentCodec(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'payment_codeC'


class PaymentCodercb(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=64)
    codec = models.IntegerField(db_column='codeC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_codeRCB'


class PaymentMethods(models.Model):
    id = models.IntegerField()
    text = models.CharField(max_length=32)
    include = models.CharField(max_length=32)
    short_name = models.CharField(max_length=10)
    flags = models.CharField(max_length=12, blank=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class PaymentReconcilations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    method_id = models.IntegerField()
    period_start = models.DateField()
    period_end = models.DateField()
    status = models.CharField(max_length=11)
    payment_count = models.IntegerField()
    sum_amounts = models.DecimalField(max_digits=9, decimal_places=2)
    sum_commissions = models.DecimalField(max_digits=9, decimal_places=2)
    comments = models.TextField()
    recongroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_reconcilations'


class PaymentTransactions(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    method_id = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField()
    ref = models.IntegerField()
    fullref = models.CharField(max_length=15)
    ts_confirmed = models.DateTimeField(blank=True, null=True)
    ts_initiated = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    commission = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    pkey = models.CharField(max_length=5)
    comment = models.CharField(max_length=255)
    status = models.CharField(max_length=9)
    recon_id = models.IntegerField(blank=True, null=True)
    display = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_transactions'


class PaymentTransfers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    recongroup_id = models.IntegerField()
    payment_id = models.IntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    account_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transfers'


class Payments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=255)
    url = models.CharField(max_length=128)
    flags = models.CharField(max_length=17)
    amount_def = models.DecimalField(max_digits=10, decimal_places=2)
    amount_min = models.DecimalField(max_digits=10, decimal_places=2)
    amount_max = models.DecimalField(max_digits=10, decimal_places=2)
    mail = models.CharField(max_length=64)
    confirmation = models.TextField()
    asso = models.ForeignKey(Groups, blank=True, null=True)
    rib = models.ForeignKey(PaymentBankaccounts)

    class Meta:
        managed = False
        db_table = 'payments'


class PostfixBlacklist(models.Model):
    email = models.CharField(primary_key=True, max_length=150)
    reject_text = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'postfix_blacklist'


class PostfixMailseen(models.Model):
    crc = models.CharField(primary_key=True, max_length=8)
    nb = models.IntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()
    release = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'postfix_mailseen'


class PostfixWhitelist(models.Model):
    email = models.CharField(primary_key=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'postfix_whitelist'


class ProfileAddresses(models.Model):
    pid = models.IntegerField()
    jobid = models.IntegerField()
    groupid = models.IntegerField()
    type = models.CharField(max_length=5)
    id = models.IntegerField()
    flags = models.CharField(max_length=65, blank=True)
    text = models.TextField()
    postaltext = models.TextField(db_column='postalText')  # Field name made lowercase.
    formatted_address = models.TextField()
    types = models.CharField(max_length=297)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    southwest_latitude = models.FloatField(blank=True, null=True)
    southwest_longitude = models.FloatField(blank=True, null=True)
    northeast_latitude = models.FloatField(blank=True, null=True)
    northeast_longitude = models.FloatField(blank=True, null=True)
    location_type = models.CharField(max_length=18, blank=True)
    partial_match = models.IntegerField()
    pub = models.CharField(max_length=7)
    comment = models.CharField(max_length=255, blank=True)
    geocoding_date = models.DateField(blank=True, null=True)
    geocoding_calls = models.IntegerField()
    postal_code_fr = models.CharField(max_length=5, blank=True)

    class Meta:
        managed = False
        db_table = 'profile_addresses'


class ProfileAddressesComponents(models.Model):
    pid = models.ForeignKey(ProfileAddresses, db_column='pid')
    jobid = models.ForeignKey(ProfileAddresses, db_column='jobid')
    groupid = models.ForeignKey(ProfileAddresses, db_column='groupid')
    type = models.ForeignKey(ProfileAddresses, db_column='type')
    id = models.ForeignKey(ProfileAddresses, db_column='id')
    component = models.ForeignKey('ProfileAddressesComponentsEnum')

    class Meta:
        managed = False
        db_table = 'profile_addresses_components'


class ProfileAddressesComponentsEnum(models.Model):
    id = models.BigIntegerField(primary_key=True)
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    types = models.CharField(max_length=297)

    class Meta:
        managed = False
        db_table = 'profile_addresses_components_enum'


class ProfileBinetEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_binet_enum'


class ProfileBinets(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    binet = models.ForeignKey(ProfileBinetEnum)

    class Meta:
        managed = False
        db_table = 'profile_binets'


class ProfileCorps(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    original_corpsid = models.ForeignKey('ProfileCorpsEnum', db_column='original_corpsid')
    current_corpsid = models.ForeignKey('ProfileCorpsEnum', db_column='current_corpsid')
    rankid = models.ForeignKey('ProfileCorpsRankEnum', db_column='rankid')
    corps_pub = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'profile_corps'


class ProfileCorpsEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    abbreviation = models.CharField(unique=True, max_length=5)
    still_exists = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_corps_enum'


class ProfileCorpsRankEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    abbreviation = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'profile_corps_rank_enum'


class ProfileDeltaten(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'profile_deltaten'


class ProfileDisplay(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    yourself = models.CharField(max_length=255)
    public_name = models.CharField(max_length=255)
    private_name = models.CharField(max_length=255)
    directory_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    promo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_display'


class ProfileEducation(models.Model):
    id = models.IntegerField()
    pid = models.ForeignKey('Profiles', db_column='pid')
    eduid = models.ForeignKey('ProfileEducationEnum', db_column='eduid', blank=True, null=True)
    degreeid = models.ForeignKey('ProfileEducationDegreeEnum', db_column='degreeid', blank=True, null=True)
    fieldid = models.ForeignKey('ProfileEducationFieldEnum', db_column='fieldid', blank=True, null=True)
    entry_year = models.IntegerField(blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)
    promo_year = models.IntegerField(blank=True, null=True)
    program = models.CharField(max_length=255, blank=True)
    flags = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'profile_education'


class ProfileEducationDegree(models.Model):
    eduid = models.ForeignKey('ProfileEducationEnum', db_column='eduid')
    degreeid = models.ForeignKey('ProfileEducationDegreeEnum', db_column='degreeid')

    class Meta:
        managed = False
        db_table = 'profile_education_degree'


class ProfileEducationDegreeEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    degree = models.CharField(unique=True, max_length=255, blank=True)
    abbreviation = models.CharField(max_length=255)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_education_degree_enum'


class ProfileEducationEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255, blank=True)
    abbreviation = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(GeolocCountries, db_column='country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_education_enum'


class ProfileEducationFieldEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    field = models.CharField(unique=True, max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'profile_education_field_enum'


class ProfileHobby(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    id = models.IntegerField()
    type = models.CharField(max_length=6)
    text = models.CharField(max_length=255)
    pub = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'profile_hobby'


class ProfileJob(models.Model):
    id = models.IntegerField()
    pid = models.ForeignKey('Profiles', db_column='pid')
    jobid = models.ForeignKey('ProfileJobEnum', db_column='jobid', blank=True, null=True)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pub = models.CharField(max_length=7)
    email_pub = models.CharField(max_length=7)
    entry_year = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'profile_job'


class ProfileJobEntrepriseTerm(models.Model):
    eid = models.ForeignKey('ProfileJobEnum', db_column='eid')
    jtid = models.ForeignKey('ProfileJobTermEnum', db_column='jtid')

    class Meta:
        managed = False
        db_table = 'profile_job_entreprise_term'


class ProfileJobEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    acronym = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    holdingid = models.ForeignKey('self', db_column='holdingid', blank=True, null=True)
    siren_code = models.CharField(db_column='SIREN_code', max_length=9, blank=True)  # Field name made lowercase.
    naf_code = models.CharField(db_column='NAF_code', max_length=5, blank=True)  # Field name made lowercase.
    ax_code = models.BigIntegerField(db_column='AX_code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profile_job_enum'


class ProfileJobTerm(models.Model):
    pid = models.ForeignKey(ProfileJob, db_column='pid')
    jid = models.ForeignKey(ProfileJob, db_column='jid')
    jtid = models.ForeignKey('ProfileJobTermEnum', db_column='jtid')
    computed = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'profile_job_term'


class ProfileJobTermEnum(models.Model):
    jtid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_job_term_enum'


class ProfileJobTermRelation(models.Model):
    jtid_1 = models.ForeignKey(ProfileJobTermEnum, db_column='jtid_1')
    jtid_2 = models.ForeignKey(ProfileJobTermEnum, db_column='jtid_2')
    rel = models.CharField(max_length=8)
    computed = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'profile_job_term_relation'


class ProfileJobTermSearch(models.Model):
    search = models.CharField(max_length=50)
    jtid = models.ForeignKey(ProfileJobTermEnum, db_column='jtid')

    class Meta:
        managed = False
        db_table = 'profile_job_term_search'


class ProfileLangskillEnum(models.Model):
    iso_639_2b = models.CharField(primary_key=True, max_length=3)
    language = models.CharField(max_length=255)
    language_en = models.CharField(max_length=255)
    iso_639_2t = models.CharField(max_length=3)
    iso_639_1 = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'profile_langskill_enum'


class ProfileLangskills(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    lid = models.ForeignKey(ProfileLangskillEnum, db_column='lid')
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_langskills'


class ProfileManageurs(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    title = models.CharField(max_length=255)
    entry_year = models.IntegerField(blank=True, null=True)
    project = models.TextField(blank=True)
    anonymity = models.IntegerField()
    visibility = models.CharField(max_length=18)
    email = models.CharField(max_length=255)
    communication = models.CharField(max_length=17)
    push = models.CharField(max_length=6)
    network = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_manageurs'


class ProfileMedalEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=10)
    text = models.CharField(max_length=255, blank=True)
    img = models.CharField(max_length=255, blank=True)
    flags = models.CharField(max_length=21)

    class Meta:
        managed = False
        db_table = 'profile_medal_enum'


class ProfileMedalGradeEnum(models.Model):
    mid = models.ForeignKey(ProfileMedalEnum, db_column='mid')
    gid = models.IntegerField()
    text = models.CharField(max_length=255, blank=True)
    pos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_medal_grade_enum'


class ProfileMedals(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    mid = models.IntegerField()
    gid = models.IntegerField()
    level = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'profile_medals'


class ProfileMentor(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    expertise = models.TextField()

    class Meta:
        managed = False
        db_table = 'profile_mentor'


class ProfileMentorCountry(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    country = models.ForeignKey(GeolocCountries, db_column='country')

    class Meta:
        managed = False
        db_table = 'profile_mentor_country'


class ProfileMentorTerm(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    jtid = models.ForeignKey(ProfileJobTermEnum, db_column='jtid')

    class Meta:
        managed = False
        db_table = 'profile_mentor_term'


class ProfileMergeIssues(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    issues = models.CharField(max_length=48, blank=True)
    entry_year_ax = models.IntegerField(blank=True, null=True)
    deathdate_ax = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    name_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_merge_issues'


class ProfileModifications(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    uid = models.ForeignKey(Accounts, db_column='uid')
    field = models.CharField(max_length=60)
    oldtext = models.TextField(db_column='oldText')  # Field name made lowercase.
    newtext = models.TextField(db_column='newText')  # Field name made lowercase.
    type = models.CharField(max_length=11)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_modifications'


class ProfileNetworking(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    id = models.IntegerField()
    nwid = models.ForeignKey('ProfileNetworkingEnum', db_column='nwid')
    address = models.CharField(max_length=255)
    pub = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'profile_networking'


class ProfileNetworkingEnum(models.Model):
    nwid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=50)
    filter = models.CharField(max_length=6)
    network_type = models.CharField(max_length=6)
    link = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_networking_enum'


class ProfilePartnersharingEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    api_uid = models.ForeignKey(Accounts, db_column='api_uid', blank=True, null=True)
    shortname = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    default_sharing_level = models.CharField(max_length=7, blank=True)
    has_directory = models.IntegerField()
    has_bulkmail = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_partnersharing_enum'


class ProfilePartnersharingSettings(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    partner = models.ForeignKey(ProfilePartnersharingEnum)
    exposed_uid = models.CharField(max_length=255)
    sharing_level = models.CharField(max_length=7, blank=True)
    allow_email = models.CharField(max_length=6, blank=True)
    last_connection = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_partnersharing_settings'


class ProfilePhones(models.Model):
    pid = models.IntegerField()
    link_type = models.CharField(max_length=7)
    link_id = models.IntegerField()
    tel_id = models.IntegerField()
    tel_type = models.CharField(max_length=6)
    search_tel = models.CharField(max_length=25)
    display_tel = models.CharField(max_length=30)
    pub = models.CharField(max_length=7)
    comment = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'profile_phones'


class ProfilePhotoTokens(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    token = models.CharField(max_length=255)
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_photo_tokens'


class ProfilePhotos(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    attachmime = models.CharField(max_length=4)
    attach = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    pub = models.CharField(max_length=7)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_photos'


class ProfilePrivateNames(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    type = models.CharField(max_length=9)
    id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_private_names'


class ProfilePublicNames(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid', primary_key=True)
    lastname_initial = models.CharField(max_length=255)
    lastname_main = models.CharField(max_length=255)
    lastname_marital = models.CharField(max_length=255)
    lastname_ordinary = models.CharField(max_length=255)
    firstname_initial = models.CharField(max_length=255)
    firstname_main = models.CharField(max_length=255)
    firstname_ordinary = models.CharField(max_length=255)
    pseudonym = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile_public_names'


class ProfileSectionEnum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'profile_section_enum'


class ProfileSkillEnum(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    text_fr = models.CharField(max_length=110)
    text_en = models.CharField(max_length=110)
    flags = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'profile_skill_enum'


class ProfileSkills(models.Model):
    pid = models.ForeignKey('Profiles', db_column='pid')
    cid = models.ForeignKey(ProfileSkillEnum, db_column='cid')
    level = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'profile_skills'


class ProfileVisibilityEnum(models.Model):
    access_level = models.CharField(max_length=7, blank=True)
    best_display_level = models.CharField(max_length=7, blank=True)
    display_levels = models.CharField(max_length=24, blank=True)

    class Meta:
        managed = False
        db_table = 'profile_visibility_enum'


class Profiles(models.Model):
    pid = models.IntegerField(primary_key=True)
    hrpid = models.CharField(unique=True, max_length=255)
    xorg_id = models.IntegerField()
    ax_id = models.CharField(max_length=8, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    birthdate_ref = models.DateField(blank=True, null=True)
    next_birthday = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    deathdate_rec = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=6)
    section = models.ForeignKey(ProfileSectionEnum, db_column='section', blank=True, null=True)
    cv = models.TextField(blank=True)
    freetext = models.TextField(blank=True)
    freetext_pub = models.CharField(max_length=7)
    axfreetext = models.TextField(blank=True)
    medals_pub = models.CharField(max_length=7)
    alias_pub = models.CharField(max_length=7)
    nationality1 = models.ForeignKey(GeolocCountries, db_column='nationality1', blank=True, null=True)
    nationality2 = models.ForeignKey(GeolocCountries, db_column='nationality2', blank=True, null=True)
    nationality3 = models.ForeignKey(GeolocCountries, db_column='nationality3', blank=True, null=True)
    email_directory = models.CharField(max_length=255, blank=True)
    last_change = models.DateField()
    title = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'profiles'


class RegisterMarketing(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    sender = models.ForeignKey(Accounts, db_column='sender', blank=True, null=True)
    email = models.CharField(max_length=255)
    date = models.DateField()
    last = models.DateField()
    nb = models.IntegerField()
    type = models.CharField(max_length=5, blank=True)
    hash = models.CharField(max_length=32)
    message = models.CharField(max_length=16)
    message_data = models.CharField(max_length=64, blank=True)
    personal_notes = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'register_marketing'


class RegisterMstats(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    sender = models.ForeignKey(Accounts, db_column='sender', blank=True, null=True)
    success = models.DateField()

    class Meta:
        managed = False
        db_table = 'register_mstats'


class RegisterPending(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    forlife = models.CharField(unique=True, max_length=255)
    bestalias = models.CharField(unique=True, max_length=255)
    mailorg2 = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=255)
    date = models.DateField()
    relance = models.DateField()
    naissance = models.DateField()
    hash = models.CharField(max_length=12)
    services = models.CharField(max_length=38)

    class Meta:
        managed = False
        db_table = 'register_pending'


class RegisterPendingXnet(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    hruid = models.ForeignKey(Accounts, db_column='hruid', unique=True)
    email = models.CharField(max_length=255)
    date = models.DateField()
    last_date = models.DateField(blank=True, null=True)
    hash = models.CharField(max_length=12)
    sender_name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'register_pending_xnet'


class RegisterSubs(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    type = models.CharField(max_length=5)
    sub = models.CharField(max_length=32)
    domain = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'register_subs'


class Reminder(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    type = models.ForeignKey('ReminderType')
    status = models.CharField(max_length=7)
    remind_last = models.DateTimeField()
    remind_next = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reminder'


class ReminderTips(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    text = models.TextField()
    priority = models.IntegerField()
    expiration = models.DateField()
    promo_min = models.IntegerField()
    promo_max = models.IntegerField()
    state = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'reminder_tips'


class ReminderType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    weight = models.IntegerField()
    remind_delay_yes = models.IntegerField()
    remind_delay_no = models.IntegerField()
    remind_delay_dismiss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reminder_type'


class Requests(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    type = models.CharField(max_length=16)
    data = models.TextField()
    stamp = models.DateTimeField()
    pid = models.ForeignKey(Profiles, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'


class RequestsAnswers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    category = models.CharField(max_length=16)
    title = models.CharField(max_length=50)
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'requests_answers'


class RequestsHidden(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    hidden_requests = models.TextField()

    class Meta:
        managed = False
        db_table = 'requests_hidden'


class SearchAutocomplete(models.Model):
    name = models.CharField(max_length=20)
    query = models.CharField(max_length=100)
    result = models.TextField()
    generated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'search_autocomplete'


class SearchName(models.Model):
    pid = models.ForeignKey(Profiles, db_column='pid')
    token = models.CharField(max_length=255)
    score = models.IntegerField()
    soundex = models.CharField(max_length=4)
    flags = models.CharField(max_length=6)
    general_type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'search_name'


class Skins(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    date = models.DateField()
    comment = models.CharField(max_length=255)
    auteur = models.CharField(max_length=30)
    skin_tpl = models.CharField(max_length=32)
    ext = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'skins'


class SurveyAnswers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    vote = models.ForeignKey('SurveyVotes')
    question_id = models.IntegerField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'survey_answers'


class SurveyVotes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    survey = models.ForeignKey('Surveys')
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_votes'


class Surveys(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    questions = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    uid = models.ForeignKey(Accounts, db_column='uid', blank=True, null=True)
    end = models.DateField()
    mode = models.IntegerField()
    promos = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'surveys'


class T(models.Model):
    a = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't'


class UrlShortener(models.Model):
    alias = models.CharField(primary_key=True, max_length=255)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'url_shortener'


class Watch(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid', primary_key=True)
    flags = models.CharField(max_length=13)
    actions = models.CharField(max_length=35)
    last = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'watch'


class WatchGroup(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    groupid = models.ForeignKey(Groups, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'watch_group'


class WatchNonins(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    ni = models.ForeignKey(Accounts)

    class Meta:
        managed = False
        db_table = 'watch_nonins'


class WatchProfile(models.Model):
    pid = models.ForeignKey(Profiles, db_column='pid')
    ts = models.DateTimeField()
    field = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'watch_profile'


class WatchPromo(models.Model):
    uid = models.ForeignKey(Accounts, db_column='uid')
    promo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'watch_promo'
