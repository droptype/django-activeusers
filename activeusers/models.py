from datetime import timedelta
import logging
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext
from django.utils.timesince import timesince
from activeusers import utils
from activeusers.utils import string_with_title

log = logging.getLogger('activeusers.models')


class VisitorManager(models.Manager):
    def active(self, timeout=None):
        """
        Retrieves only visitors who have been active within the timeout
        period.
        """
        if not timeout:
            timeout = utils.get_timeout()

        now = timezone.now()
        cutoff = now - timedelta(minutes=timeout)

        return self.get_query_set().filter(last_update__gte=cutoff)


class Visitor(models.Model):
    session_key = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True)
    user_agent = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    page_views = models.PositiveIntegerField(default=0)
    session_start = models.DateTimeField()
    last_update = models.DateTimeField()

    objects = VisitorManager()

    def save(self, *args, **kwargs):
        # Truncate to avoid errors when the url is longer than the field
        # max_length
        try:
            max_length = self._meta.get_field('url').max_length
            self.url = self.url[:max_length]
        except AttributeError:
            pass

        super(Visitor, self).save(*args, **kwargs)

    def _time_on_site(self):
        """
        Attempts to determine the amount of time a visitor has spent on the
        site based upon their information that's in the database.
        """
        if self.session_start:
            seconds = (self.last_update - self.session_start).seconds

            hours = seconds / 3600
            seconds -= hours * 3600
            minutes = seconds / 60
            seconds -= minutes * 60

            return u'%i:%02i:%02i' % (hours, minutes, seconds)
        else:
            return ugettext(u'unknown')

    time_on_site = property(_time_on_site)

    def _last_seen(self):
        """
        Returns a "humanised" expression for time since the user was last seen,
        e.g. "3 minutes ago".
        """

        return ugettext(u'%s ago') % timesince(self.last_update)

    last_seen = property(_last_seen)

    class Meta:
        app_label = string_with_title('activeusers', 'Active users')
        ordering = ('-last_update',)
        unique_together = ('session_key', 'ip_address',)
        verbose_name = 'active visitor'
        verbose_name_plural = 'active visitors'
