# -*- coding: cp1252 -*-
import datetime
from django.contrib import admin
from subscription.models import Subscription
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.conf.urls.defaults import url, patterns
from django.http import HttpResponse

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ['created_at', 'paid']

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()

    def mark_as_paid(self, request, querySet):
        count = querySet.update(paid=True)

        msg = ungettext(
                u'%(count)d inscrição foi marcada como paga',
                u'%(count)d inscrições foram marcadas como pagas',
                count
                ) % {'count': count}
        self.message_user(request, msg)

    def export_subscription(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]

        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = 'text/csv'
        response['Content-Type'] = 'text/csv' 
        response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'

        return response

    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_url = patterns('',
            url(r'exportar/$', self.admin_site.admin_view(self.export_subscription), name='export_subscription'),
        )
        return extra_url + original_urls

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True
    mark_as_paid.short_description = _(u'Marcar como paga')
    export_subscription.short_description = _(u'Exportar')

    
admin.site.register(Subscription, SubscriptionAdmin)
