from django.conf.urls import url
from skill_match.views import ListHendersonParks, DetailHendersonPark, \
    ListCreateMatches, DetailUpdateMatch

urlpatterns = (
    url(r'^parks/$', ListHendersonParks.as_view(), name='list_parks'),
    url(r'^parks/(?P<pk>\d+)/$', DetailHendersonPark.as_view(),
        name='hendersonpark-detail'),
    url(r'^matches/$', ListCreateMatches.as_view(), name='list_matches'),
    url(r'^matches/(?P<pk>\d+)/$', DetailUpdateMatch.as_view(),
        name='match-detail'),

)
