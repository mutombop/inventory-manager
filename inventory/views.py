from datetime import datetime, timedelta
from django.conf import settings
from bootstrap_datepicker_plus import DatePickerInput
from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Section, Holder, Purchaseorder, Asset
from . import forms

from django.template import loader


# Create your views here.

def sections(request):
    sections = Section.objects.all()
    return render(request, 'inventory/sections.html', {'sections': sections})

def holders_index(request):
    holders_list = Holder.objects.filter(active=True).order_by('first_name', 'last_name')
    paginator = Paginator(holders_list, 10)
    page = request.GET.get('page')
    try:
        holders = paginator.get_page(page)
    except PageNotAnInteger:
        holders = paginator.page(1)
    except EmptyPage:
        holders = paginator.page(paginator.num_pages)
    return render(request, 'inventory/holders.html', {'holders': holders})

def pos_index(request):
    pos = Purchaseorder.objects.order_by('number')
    return render(request, 'inventory/pos.html', {'pos': pos})

@login_required(login_url='login/')
def assets_index(request):
    assets_list = Asset.objects.order_by('inventorytag')
    paginator = Paginator(assets_list, 5)
    page = request.GET.get('page')
    try:
        assets = paginator.get_page(page)
    except PageNotAnInteger:
        assets = paginator.page(1)
    except EmptyPage:
        assets = paginator.page(paginator.num_pages)
    return render(request, 'inventory/assets.html', {'assets': assets})

def create_holder(request):
    if request.method == "POST":
        form = forms.HolderForm(request.POST)
        if form.is_valid():
            holder_new = form.save(commit=False)
            holder_new.save()
            messages.success(request, f'New holder has been created!')
            return redirect('allholders')
    else:
        form = forms.HolderForm()
    return render(request, 'inventory/holder_create.html', {'form': form})

def create_asset(request):
    if request.method == "POST":
        form = forms.AssetForm(request.POST)
        if form.is_valid():
            asset_new = form.save(commit=False)
            asset_new.save()
            messages.success(request, f'New asset has been created!')
            return redirect('allassets')
    else:
        form = forms.AssetForm()
    return render(request, 'inventory/asset_create.html', {'form': form})

def create_po(request):
    if request.method == "POST":
        form = forms.PurchaseorderForm(request.POST)
        if form.is_valid():
            po_new = form.save(commit=False)
            po_new.save()
            return redirect('allpos')
    else:
        form = forms.PurchaseorderForm()
    return render(request, 'inventory/po_create.html', {'my_form': form})

def holder_assets(request, holder_id):
    assets = Asset.objects.filter(holder__id=holder_id)
    holder = Holder.objects.get(pk=holder_id)
    return render(request, 'inventory/holder_assets.html', {'assets': assets, 'holder': holder})

class HolderUpdate(UpdateView):
    model = Holder
    fields = '__all__'

class HolderDetail(DetailView):
    model = Holder
    fields = '__all__'

class AssetUpdate(UpdateView):
    model = Asset
    fields = '__all__'
    success_url="/assets/"  

class AssetDetail(DetailView):
    model = Asset
    fields = '__all__'

class PurchaseorderDetail(DetailView):
    model = Purchaseorder
    fields = '__all__'

class AssetMarkpsb(UpdateView):
    model = Asset
    fields = ['inventorytag', 'amr', 'serialnumber', 'status', 'psbstatus', 'comment']
    initial = {'psbstatus': 'MARKED'}

def laptops3year(request):
    # todaydate = datetime.datetime.now()
    assets = Asset.objects.filter(assettype__name='Laptop').filter(po__date_delivered__lte=datetime.today()-timedelta(days=600))
    return render(request, 'inventory/laptops3year.html', {'assets': assets})

def stockict(request):
    assets = Asset.objects.filter(holder__last_name='ICT').order_by('inventorytag')
    return render(request, 'inventory/stockict.html', {'assets': assets})

def stockadmin(request):
    assets = Asset.objects.filter(holder__last_name='ADMIN').order_by('inventorytag')
    return render(request, 'inventory/stockadmin.html', {'assets': assets})

def psbmarked(request):
    assets = Asset.objects.filter(psbstatus='MARKED').order_by('inventorytag')
    return render(request, 'inventory/psbmarked.html', {'assets': assets})

def receiptsheet(request, holder_id):
    context = {
        'holder' : Holder.objects.get(id=holder_id),
        'assets' : Asset.objects.filter(holder__id=holder_id)
    }
    html = loader.render_to_string('inventory/receipt_sheet.html', context)
    output = pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'inline; filename=recepit_sheet.pdf'
    response.write(output)
    return response

def ictreturn(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    asset.id = 20
    asset.save()

    return HttpResponseRedirect(request.path_info)

class POView(CreateView):
    model = Purchaseorder
    fields = ['number', 'section', 'date_delivered']
    def get_form(self):
        form = super().get_form()
        form.fields['date_delivered'].widget = DatePickerInput()
        return form







