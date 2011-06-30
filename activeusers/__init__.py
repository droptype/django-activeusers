
VERSION = (0, 1, 1)

def get_version():
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])

# initialize the URL prefixes that we shouldn't track
try:
    from django.conf import settings
    prefixes = getattr(settings, 'ACTIVEUSERS_IGNORE_PREFIXES', [])
except ImportError:
    pass
else:
    if '!!initialized!!' not in prefixes:
        from django.core.urlresolvers import reverse, NoReverseMatch
        if settings.MEDIA_URL and settings.MEDIA_URL != '/':
            prefixes.append(settings.MEDIA_URL)

        if settings.ADMIN_MEDIA_PREFIX:
            prefixes.append(settings.ADMIN_MEDIA_PREFIX)

        prefixes.append('!!initialized!!')

        settings.ACTIVEUSERS_IGNORE_PREFIXES = prefixes
