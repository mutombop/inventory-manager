from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import ModelForm
from .models import Holder, Asset, Purchaseorder, Assetmodel, Assettype


class HolderForm(ModelForm):
    class Meta:
        model = Holder
        fields = ['first_name', 'last_name', 'title', 'email', 'section', 'dutystation', 'active']


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class PurchaseorderForm(forms.ModelForm):
    class Meta:
        model = Purchaseorder
        fields = ['number', 'section', 'date_delivered']
        widgets = {
            # default date-format %m/%d/%Y will be used
            'date_delivered': DatePickerInput(),
        }
