from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'artworks', 'artworks.urls', name='artworks'),
    host(r'plants', 'plants.urls', name='plants'),
)