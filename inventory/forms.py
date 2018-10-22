from bootstrap_datepicker_plus import DatePickerInput
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

class PurchaseorderForm(forms.ModelForm):
    class Meta:
        model = Purchaseorder
        fields = ['number', 'section', 'date_delivered']
        widgets = {
            'date_delivered': DatePickerInput(), # default date-format %m/%d/%Y will be used
        }
