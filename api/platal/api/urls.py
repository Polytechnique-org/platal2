from django.conf.urls import include, url
from rest_framework import routers

from .resources import account


router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'account/me/', account.MyAccountView),
    url(r'account/(?P<hruid>.+)/', account.AccountView.as_view(), name='account'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
