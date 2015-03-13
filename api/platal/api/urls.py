from django.conf.urls import include, url
from rest_framework import routers

from .resources import account
from .resources import profile


router = routers.DefaultRouter()
router.register(r'profiles', profile.ProfileViewSet)
router.register(r'photos', profile.ProfilePhotoViewSet)


urlpatterns = [
    url(r'profiles/me/', profile.MyProfileView),
    url(r'^', include(router.urls)),
    url(r'accounts/me/', account.MyAccountView),
    url(r'accounts/(?P<hruid>.+)/', account.AccountView.as_view(), name='account'),
    url(r'photos/(?P<hrpid>.+)/raw/', profile.RawPhotoView.as_view(), name='profile-photo-raw'),
]
