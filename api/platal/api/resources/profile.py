from django import http

from rest_framework import decorators
from rest_framework import filters
from rest_framework import reverse as drf_reverse
from rest_framework import serializers
from rest_framework import views
from rest_framework import viewsets

from platal.profiles import models
from platal.profiles import search as psearch



# Photo
# =====


class ProfilePhotoSerializer(serializers.ModelSerializer):
    raw_url = serializers.SerializerMethodField()
    def get_raw_url(self, obj):
        return drf_reverse.reverse('api:profile-photo-raw',
            kwargs={'hrpid': obj.profile.hrpid},
            request=self.context.get('request'),
        )

    mimetype = serializers.CharField(source='attachmime')
    width = serializers.IntegerField(source='x')
    height = serializers.IntegerField(source='y')

    class Meta:
        model = models.ProfilePhoto
        fields = ['mimetype', 'width', 'height', 'raw_url']
        read_only_fields = fields


class ProfilePhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (models.ProfilePhoto.objects
        .select_related('profile')
        .defer('attach')
    )

    serializer_class = ProfilePhotoSerializer
    lookup_field = 'profile__hrpid'
    lookup_url_kwarg = 'hrpid'
    lookup_value_regex = r'[a-z0-9.-]+'


class RawPhotoView(views.APIView):
    def get(self, request, hrpid, format=None):
        photo = models.ProfilePhoto.objects.get(profile__hrpid=hrpid)
        response = http.HttpResponse(content_type='image/%s' % photo.attachmime)
        response.write(photo.attach)
        return response


# Profile
# =======

@decorators.api_view()
def MyProfileView(request):
    profile = request.user.profile
    if profile is None:
        raise http.Http404()

    url = drf_reverse.reverse('api:profile-detail', kwargs={'hrpid': profile.hrpid}, request=request)
    return http.HttpResponseRedirect(url)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    photo = ProfilePhotoSerializer()
    public_name = serializers.CharField(source='profile_display.public_name')
    sort_name = serializers.CharField(source='profile_display.sort_name')
    directory_name = serializers.CharField(source='profile_display.directory_name')
    short_name = serializers.CharField(source='profile_display.short_name')
    promo = serializers.CharField(source='profile_display.promo')

    class Meta:
        model = models.Profile
        fields = [
            'hrpid', 'sex', 'photo', 'promo',
            'public_name', 'sort_name', 'short_name', 'directory_name',
        ]
        read_only_fields = fields


class ProfileSearchBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        search = request.QUERY_PARAMS.get('search', None)
        if search:
            queryset = psearch.filter_profiles(queryset, search)
        return queryset


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Profile.objects.select_related(
        'profile_display',
        'photo',
    )

    filter_backends = [ProfileSearchBackend]
    serializer_class = ProfileSerializer
    lookup_field = 'hrpid'
    lookup_value_regex = r'[a-z0-9.-]+'


