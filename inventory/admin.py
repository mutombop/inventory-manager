from django.contrib import admin
from .models import Section, Assettype, Assetmodel, Dutystation, Holder, Purchaseorder, Asset

# Register your models here.

admin.site.site_header = 'ICT Inventory Admin Dashboard'

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

admin.site.register(Section, SectionAdmin)

admin.site.register(Assettype)

# admin.site.register(Assetmodel)

class AssetmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'assettype', 'name')
    list_filter = ("assettype", "name")

admin.site.register(Assetmodel, AssetmodelAdmin)

class DutystationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Dutystation, DutystationAdmin)

class HolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'title', 'email')
    list_filter = ('section', 'dutystation')
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name']

admin.site.register(Holder, HolderAdmin)

class PurchaseorderAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'section', 'date_delivered')
    list_filter = ['section']
    search_fields = ['number']

admin.site.register(Purchaseorder, PurchaseorderAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventorytag', 'amr', 'assetmodel', 'serialnumber', 'psbstatus')
    list_filter = ['assetmodel', 'psbstatus']
    search_fields = ['amr', 'serialnumber', 'inventorytag']
    ordering = ['inventorytag']

admin.site.register(Asset, AssetAdmin)