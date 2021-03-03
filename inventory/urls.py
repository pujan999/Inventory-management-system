from django.urls import path
from .views import (
    VendorAPIView,
    VendorDetailAPIView,
    AddItemAPI,
    FacebookLogin,
    ItemDetailAPI,
    PurchaseAPIView,
    RackAPIView,
    RackDetailAPIView,
    PurchaseDetailEditAPIView,
    CustomerAPIView,
    CustomerDetailAPIView,
    LossDamageAPIView,
    LossDamageDetailAPIView,
    SalesAPIView,
    SalesDetailAPIView,
    VendorPurchaseAPIView,
    CustomerSalesAPIView,
    StockInAPIView,
    StockOutOrder,
    PurchaseReturnAPIView,
    PurchaseReturnDetailAPIView,
    UnitAPIView,
    UnitDetailAPIView,
    SalesReturnAPIView,
    SalesReturnDetailAPIView,
    LedgerAPIView,
    CategoryDetailAPIView,
    CategoryAPIView,
    VoucherAPIView,
    PurchaseItemAPIView,
    SalesItemAPIView,
    PurchaseReturnItemAPIView,
    SalesReturnItemAPIView,
    VendorNameReturn,
    StockTransferAPIView,
    StockAPIView,
    TestDateAPIView,
    VendorPurchaseReturnAPIView,
    CustomerSalesReturnAPIView,
    ItemCountAPIView,
    ItemInRackAPIView,

    PurchaseEntryFormDetail,
    PurchaseReturnEntryFormAPIView,
    PurchaseAllItemAPIView,

    PurchaseReturnEntryFormPostAPIView)

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('',VendorAPIView.as_view(),name="vendor-registration" ),
    path('vendor-detail/<int:id>/', VendorDetailAPIView.as_view(),name='vendor-detail'),

    path('item/',csrf_exempt(AddItemAPI.as_view()),name= "add-item"),
    path('item-detail/<int:id>/',ItemDetailAPI.as_view(),name="item-detail"),

    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

    path('purchase/',PurchaseAPIView.as_view(),name ='purchase'),
    path('purchase-detail-edit/<int:id>/', PurchaseDetailEditAPIView.as_view(), name='purchase-detail-update'),

    path('rack/',RackAPIView.as_view(),name = 'rack'),
    path('rack-detail/<int:id>/',RackDetailAPIView.as_view(),name='rack-detail'),

    path('category-detail/<int:id>/',CategoryDetailAPIView.as_view(), name = 'category-detail'),
    path('category/',CategoryAPIView.as_view(),name = 'category'),

    path('voucher/',VoucherAPIView.as_view(), name ='voucher-type'),

    path('customer/', CustomerAPIView.as_view(), name= 'customer'),
    path('customer-detail/<int:id>/', CustomerDetailAPIView.as_view(), name='customer-detail'),

    path('lost-damage/',LossDamageAPIView.as_view(), name='lost-damage'),
    path('lost-damage-detail/<int:id>/', LossDamageDetailAPIView.as_view(), name='lost-damage-detail'),
    
    path('sales/', SalesAPIView.as_view(), name= 'sales'),
    path('sales-detail/<int:id>/',SalesDetailAPIView.as_view(), name='sales-detail'),

    #send vendor id to get the vendor related purchase
    path('vendor-purchase-detail/<int:id>/',VendorPurchaseAPIView.as_view(), name='purchase-detail'),
    #send vendor id to get vendor purchase return 
    path('vendor-purchase-return/<int:id>/',VendorPurchaseReturnAPIView.as_view(), name = 'vendor-purchasse-return'),
    
    #send customer id to get sales related to customer
    path('customer-sales-detail/<int:id>/',CustomerSalesAPIView.as_view(), name= 'customer-saless-detail'),
    #send customer id to get sales return related to customer
    path('customer-sales-return/<int:id>/',CustomerSalesReturnAPIView.as_view(), name = 'customer-sales-return'),

    path('stock-in/',StockInAPIView.as_view(), name='stock-in'),
    path('stock-out-order/', StockOutOrder.as_view(), name='stock-out-order'),
    path('purchase-return/',PurchaseReturnAPIView.as_view(), name='purchase-return'),
    path('purchase-return-detail/<int:id>/',PurchaseReturnDetailAPIView.as_view(), name='purchase-return-detail'),
    path('unit/', UnitAPIView.as_view(), name='unit'),
    path('unit-detail/<int:id>/', UnitDetailAPIView.as_view(), name = 'unit-detail'),
    path('sales-return/', SalesReturnAPIView.as_view(), name = 'sales-return'),
    path('sales-return-detail/<int:id>/', SalesReturnDetailAPIView.as_view(), name = 'sales-return-detail'),
    path('ledger/', LedgerAPIView.as_view(), name = 'ledger'),
    path('stock/',StockAPIView.as_view(), name='stock'),
    
    path('date/',TestDateAPIView.as_view(),name = 'date'),

    # send purchase id here

    path('perticular-purchase/<int:id>/',PurchaseItemAPIView.as_view(),name ='perticular-purchase'),

    #send sales id here
    # You will get all the sales voucher item from this link 
    
    path('particular-sales/<int:id>/',SalesItemAPIView.as_view(), name =' perticular-sales'),

    # send sales-return id here
    path('perticular-sales-return/<int:id>/', SalesReturnItemAPIView.as_view(), name ='perticular-sales-return'),

    #send purchase-return id here
    path('perticular-purchase-return/<int:id>/', PurchaseReturnItemAPIView.as_view(), name = 'perticular-purchase-return'),
    path('vendor-name-return/<int:id>/',VendorNameReturn.as_view(), name = "vendor-return"),
    
    #stock transfer
    #send stock-id here
    path('stock-transfer/<int:id>/',StockTransferAPIView.as_view(), name = 'stock-transfer'),
    
    #total item return 
    path('item-total/',ItemCountAPIView.as_view(), name='item-total'),
    
    #send rack id in this url
    path('rack-item/<int:id>/',ItemInRackAPIView.as_view(),name='rack-item'),
    
    #To edit purchase item 
    path('purchase-item/<int:id>/',PurchaseEntryFormDetail.as_view(),name='purchase-item'),
path('purchase-item/<int:id>/',PurchaseEntryFormDetail.as_view(),name='purchase-item'),
    
    #send purchasereturn id to edit delete or update the purchasereturn item
    path('purchase-return-item/<int:id>/',PurchaseReturnEntryFormAPIView.as_view(),name='purchase-return-item'),
    path('purchase-return-itempost/',PurchaseReturnEntryFormPostAPIView.as_view(),name='purchase-return-item entry'),
    
    #to get all purchase item 
    path('purchase-all-item/',PurchaseAllItemAPIView.as_view(), name="purchase-all-item")

    
]