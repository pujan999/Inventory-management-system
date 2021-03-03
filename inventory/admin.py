from django.contrib import admin
from .models import *

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
	list_display= [
	'id',
	'name',
	'contact',
	'pan_number',
	'title'
	]
	search_fields=[
	'id',
	'name',
	'company_name',
	'contact'
	]


class ItemCategoryAdmin(admin.ModelAdmin):
	list_display=[
	'title',
	'description']
	search_fields=['title']

class ItemAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'item_name',
	'unit',
	'item_code',
	
	'category',
	

	
	
	

	]
	search_fields = [
	'item_name',
	'item_code',
	
	]

class PurchaseEntryAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'purchase',
	'item',
	'quantity',
	'price',
	'total']

class PurchaseAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	
	'vendor_detail',
	'voucher_type',
	
	
	
	
	'bill_image',
	'date',
	
	'remarks'
	]

	search_fields = [
	'item',
	'vendor_detail',
	'bill_number',
	]



class RackAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	'rack_name'
	]
	search_fields =[
	'rack_name']

class UnitAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	'symbol',

	
	'name',


	]
	search_fields =[
	'name'
	]

class PurchaseReturnAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	'vendor',
	'voucher_type',
	'date',
	'remarks',
	'total'
	]
	search_fields =['purchase']

class PurchaseReturnEntryAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'purchase_return',
	'item',
	'quantity']

class StockAdmin(admin.ModelAdmin):
	list_display=[
	'id',
	'item',
	'quantity',
	'rack',
	'quantity_after_transfer'
	]
	search_fields=['item']

class CustomerAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	'name',
	'email',
	'contact',
	'address',
	'pan_number',
	'title'
	]

	search_fields =[
	'name',
	'email',
	'contact'
	]

class LossDamageAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	'item',
	'quantity',
	'price',
	# 'rack',
	'remarks',
	'date'
	]
	search_fields =[
	'item']

class SalesAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	
	'customer',
	'bill_number',
	'date',
	'remarks'
	]
	search_fields =[
	'item',
	'bill_number'
	]

class SalesEntryAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'sales',
	'item',
	'quantity',
	'price',
	'total'
	]

class SalesReturnAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	
	'customer',
	
	'date',
	'remarks'
	]

	search_fields =[
	'item'
	]

class SalesReturnEntryAdmin(admin.ModelAdmin):
	list_display=[
	'id',
	'sales_return',
	'item',
	'quantity',
	'price',
	'total']



class StockTransferAdmin(admin.ModelAdmin):
	list_display =[
	'id',
	
	'rack',
	'quantity',
	
	]
	search_fields = [
	 'rack']


class LedgerAdmin(admin.ModelAdmin):
	list_display=[
	'id',
	'date',
	'item',
	'voucher_type',
	'quantity',
	'price',
	'get_total']

	search_fields =['item','voucher_type']

class VoucherTypeAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'voucher_type']

admin.site.register(PurchaseEntryForm, PurchaseEntryAdmin)
admin.site.register(Category, ItemCategoryAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(VoucherType, VoucherTypeAdmin)
admin.site.register(VendorDetail,VendorAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(PurchaseReturn, PurchaseReturnAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(LossDamage, LossDamageAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesReturn, SalesReturnAdmin)
admin.site.register(Ledger,LedgerAdmin)
admin.site.register(PurchaseReturnEntryForm,PurchaseReturnEntryAdmin)
admin.site.register(SalesEntryForm, SalesEntryAdmin)
admin.site.register(StockTransfer, StockTransferAdmin)
admin.site.register(SalesReturnEntryForm , SalesReturnEntryAdmin)
