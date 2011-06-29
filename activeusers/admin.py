from django.contrib import admin
from activeusers.models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    model = Visitor
    list_display = ('ip_address', 'user', 'url', 'last_update')
    def queryset(self, request):

        qs = self.model._default_manager.active()
        ordering = self.ordering or () # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


    # Can't modify any data here
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Visitor, VisitorAdmin)