"""invproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from inventory import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.assets_index),
    # path('', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('asset/<int:pk>/update/', views.AssetUpdate.as_view(), name='asset_update'),
    path('asset/<int:pk>/', views.AssetDetail.as_view(), name='asset_detail'),
    path('asset/<int:pk>/markpsb/', views.AssetMarkpsb.as_view(), name='asset_markpsb'),
    path('assets/holder/<int:holder_id>/', views.holder_assets, name='assetsforholder'),
    path('assets/new', views.create_asset, name='newasset'),
    path('assets/', views.assets_index, name='allassets'),
    # path('holders/paginated/', views.holders_index2, name='holders_paginated'),
    path('holders/new', views.create_holder, name='newholder'),
    path('holder/<int:holder_id>/receipt/', views.receiptsheet, name='holder_receipt'),
    path('holder/<int:pk>/update/', views.HolderUpdate.as_view(), name='holder_update'),
    path('holder/<int:pk>/', views.HolderDetail.as_view(), name='holder_detail'),
    path('holders/', views.holders_index, name='allholders'),
    path('ictreturn/', views.ictreturn, name="ict_return"),
    path('laptops3year/', views.laptops3year, name='laptops3year'),
    path('pos/new', views.POView.as_view(), name='newpo'),
    # path('pos/new', views.create_po, name='newpo'),
    path('po/<int:pk>/', views.PurchaseorderDetail.as_view(), name='po_detail'),
    path('pos/', views.pos_index, name='allpos'),
    path('psbmarked/', views.psbmarked, name='psb_marked'),
    path('sections/', views.sections, name='allsections'),
    path('stockict/', views.stockict, name='stock_ict'),
    path('stockadmin/', views.stockadmin, name='stock_admin'),

   
]
