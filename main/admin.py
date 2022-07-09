from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Order, SimpleHistoryAdmin)
admin.site.register(Courier, SimpleHistoryAdmin)
admin.site.register(Customer, SimpleHistoryAdmin)

class OrderResource(resources.ModelResource):
  class Meta:
    model = Order
    fields = (
      'products',
      'person',
      'address'
    )
    export_order = fields

class edxUserAdmin(ImportExportModelAdmin):
  resource_class = OrderResource