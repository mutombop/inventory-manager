from django import forms
from django.forms import ModelForm
from .models import Holder, Asset, Purchaseorder, Assetmodel, Assettype

class HolderForm(ModelForm):
    class Meta:
        model = Holder
        # fields = ['first_name', 'last_name', 'title', 'section', 'dutystation']
        fields = '__all__'

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class PurchaseorderForm(ModelForm):
    class Meta:
        model = Purchaseorder
        fields = ['number', 'section', 'date_delivered']

