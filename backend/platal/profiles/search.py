# -*- coding: utf-8 -*-


from django.db.models import Q
from . import models


def filter_profiles(qs, search_term):
    pid_qs = qs.filter(
        Q(hrpid__icontains=search_term)
        | Q(profile_display__public_name__icontains=search_term)
        | Q(profile_display__short_name__icontains=search_term)
        | Q(profile_display__sort_name__icontains=search_term)
        | Q(public_names__pseudonym__icontains=search_term)
    )
    pids = pid_qs.values_list('pid')

    return qs.filter(pid__in=pids)

