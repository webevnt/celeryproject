from django.contrib import admin
from django.db.models import Subquery
from import_export.admin import ImportExportModelAdmin
from .models import *






class SaleOrderAdmin(ImportExportModelAdmin):

    ordering = ['id', 'name', ]
    list_display = ['name', 'amount', 'renewal', 'start_date', 'due_date']

    
class NotificationTrans(ImportExportModelAdmin):

    search_fields = (
        'user__email',
    )

    ordering = ['-id']
    list_display = ['user','name', 'name','sent', 'created_on']
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
    )



class SubscribersAdmin(ImportExportModelAdmin):
    search_fields = (
        'sale_order__name',
    )
    list_display = ['sale_order', 'bounce', 'status']
    


class CountryAdmin(ImportExportModelAdmin):
    list_display = ['name',]

class StoreAdmin(ImportExportModelAdmin):
    list_display = ['name',]



admin.site.register(SaleOrder, SaleOrderAdmin)
admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(NotificationTransaction, NotificationTrans)