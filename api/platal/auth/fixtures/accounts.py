from .. import models

ACCOUNT_TYPES = {
    'x': {'perms': 'xnet', 'description': "Polytechnicien"},
}


def setup():
    objects = []
    for key, fields in ACCOUNT_TYPES.items():
        obj, _created = models.AccountType.objects.update_or_create(
            type=key,
            defaults=fields,
        )
        objects.append(obj)

    return objects
