
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

        keys = ('MEDIA_URL', 'STATIC_URL')
        for key in keys:
            if hasattr(settings, key) and getattr(settings, key) != '/':
                prefixes.append(getattr(settings, key))
        
        prefixes.append('!!initialized!!')

        settings.ACTIVEUSERS_IGNORE_PREFIXES = prefixes

