from django import http

from rest_framework import serializers
from rest_framework import generics
from rest_framework import decorators
from rest_framework import reverse as drf_reverse

from platal.auth import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['hruid', 'full_name', 'sex']
        read_only_fields = fields


@decorators.api_view()
def MyAccountView(request):
    url = drf_reverse.reverse('api:account', kwargs={'hruid': request.user.hruid}, request=request)
    return http.HttpResponseRedirect(url)



class AccountView(generics.RetrieveAPIView):

    serializer_class = AccountSerializer
    lookup_field = 'hruid'

    def get_queryset(self):
        qs = models.Account.objects
        if not self.request.user.is_admin:
            qs = qs.filter(pk=self.request.user.pk)
        return qs
