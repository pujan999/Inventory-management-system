from rest_framework import serializers
from .models import (
    VendorDetail,
    Item,
    Rack,
    Purchase,
    Customer,
    LossDamage,
    Sales,
    PurchaseReturn,
    SalesReturn,
    Unit,
    Ledger,
    VoucherType,
    Stock,
    Category,
    PurchaseEntryForm,
    SalesEntryForm,
    SalesReturnEntryForm,
    PurchaseReturnEntryForm,
    StockTransfer,
    TestDate
)
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()


'''

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=255)
	password2 = serializers.CharField(max_length=255,required=False)

	class Meta:
		model = User
		fields=["username","password","password2","email"]
		extra_kwargs = {"password":{"write_only":True},"password2":{"write_only":True}}

		

	def validate(self,data):

		if data['password'] != data['password2']:
			raise ValidationError("Your password doesnot match!!")

		return data
'''
'''
	def validate_email(self,value):
		if User.objects.filter(email__iexact = value).exists:
			raise ValidationError("User with this email already exists.")
		return value
'''


class VendorSerializer(serializers.ModelSerializer):

    #purchase_data = serializers.PrimaryKeyRelatedField(source='purchase_set', many=True, queryset=Purchase.objects.all())
    #purchase_total = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = VendorDetail
        fields = [
            "id",
            "address",
            "name",
            "company_name",
            "company_contact",
            "contact",
            
            "pan_number",

            # "purchase_total"
        ]
        depth = 1


'''

	def get_purchase_total(self , value):
		return value.get_purchase_sum
'''


'''
	def to_representation(self, value):
		data = super().to_representation(value)  
		mode_serializer = PurchaseSerializer(value.purchase_data)
		data['purchase_data'] = mode_serializer.data
		return data
'''

# Function to Register User and Vendor
'''
	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create(
			username = user_data['username'],
			password = user_data['password'],
			email=user_data['email'])
		user.is_staff = True
		user.save()
		vendor = VendorDetail.objects.create(user= user,**validated_data)
		vendor.save()
		return vendor

	def update(self,instance,validated_data):
		user_data = validated_data.pop('user')
		instance.name = validated_data.get('name')
		instance.company_name= validated_data.get('company_name')
		instance.contact = validated_data.get('contact')
		instance.company_contact = validated_data.get('company_contact')
		instance.pan_number = validated_data.get('pan_number')
		
		user_id = instance.user.id 
		if User.objects.get(id = user_id).exists():
			user = user_data.objects.get(id=user_id)
			user.name = user_data.get('name', user.name)
			user.company_name = user_data.get('company_name',user.company_name)
			user.contact = user_data.get('contact',user.contact)
			user.company_contact=user_data.get('company_contact',user.company_contact)
			user.pan_number=user_data.get('pan_number',user.pan_number)
			user.save()

		instance.save()

'''


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'description'
        ]


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = [
            'id',
            'symbol',
            'name'
        ]


class ItemSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    unit_id = serializers.PrimaryKeyRelatedField(



        queryset=Unit.objects.all(),

        source='unit',
        write_only=True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "unit",
            "unit_id",
            "item_name",
            "item_code",
            "item_limit",
            "local_name",
            "category",
            "category_id",



        ]
        extra_kwargs = {
            'item_code': {'read_only': True}
        }

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        item.save()
        stock = Stock.objects.create(item=item, quantity=0)
        stock.save()
        return item


class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = [
            "id",
            "rack_name"
        ]


'''
class AddStockDetailSerializer(serializers.serializer):
	item_id = serializers.IntergerField()
	rack_number = serializers.IntergerField()
	batch_number = serializers.CharField(max_length=100)
	value = serializers.CharField(max_length=255)
	bill_image = serializers.ImageField()
	item_brand_name = serializers.CharField(max_length=255)
	remarks = serializers.CharField(max_length=255)

'''


class VoucherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherType
        fields = [
            'id',
            'voucher_type',
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    '''
    item = ItemSerializer( read_only = True)
    item_id = serializers.PrimaryKeyRelatedField(
            queryset=Item.objects.all(),
            source='item',
            write_only=True
            )
    rack_name = RackSerializer(read_only = True)
    rack_id	= serializers.PrimaryKeyRelatedField(
            queryset= Rack.objects.all(),
            source='rack_name',
            write_only=True
            )
            '''
    vendor_detail = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=VendorDetail.objects.all(),
        source='vendor_detail',
        write_only=True,
    )
    grand_total = serializers.SerializerMethodField(read_only=True)
    vat = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    #voucher_type = VoucherTypeSerializer(read_only = True)
    # voucher_id = serializers.PrimaryKeyRelatedField(
    #	queryset= VoucherType.objects.all(),
    #	source= 'voucher_type',
    #	write_only = True
    #	)
    #total_item_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Purchase
        fields = [
            "id",
            "vendor_detail",
            "vendor_id",
            "bill_number",
            "voucher_type",
            "remarks",
            "total",
            "grand_total",
            "date",
            "vat"

        ]
        extra_kwargs = {
            'title': {'read_only': True}
        }
        depth = 1

    def get_total(self, obj):
        return obj.total_after_vat

    def get_grand_total(self, obj):
        return obj.total

    def get_vat(self, obj):
        return obj.vat


'''

	def get_total_item_price(self,obj):
		return obj.get_total

	def create(self,validated_data):
		#user = self.context.get('request.user')
		#vendor_detail = get_object_or_404(VendorDetail)
		#item_id = validated_data.pop('item_id')
		#item = get_object_or_404(Item,id=item_id)
		#rack_id = validated_data.pop('rack_id')
		#rack = get_object_or_404(Rack, id= rack_id)

		stock = StockDetail.objects.create(**validated_data)
		stock.save()
		return stock

	'''


class CustomerSerializer(serializers.ModelSerializer):
    #customer_sales_total = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Customer
        fields = [
            "id",
            "title",
            "name",
            "company_name",
            "company_contact",
            "email",
            "contact",
            "pan_number",
            "address"
            # "customer_sales_total"
        ]

    def get_customer_sales_total(self, obj):
        return obj.customer_sales_total


class PurchaseEntryFormSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(read_only = True)
    purchase_id = serializers.PrimaryKeyRelatedField(
        queryset = Purchase.objects.all(),
        source = 'purchase',
        write_only = True
    )

    item = ItemSerializer(read_only = True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset = Item.objects.all(),
        source = 'item',
        write_only = True
    )
    
    rack = RackSerializer(read_only = True)
    rack_id = serializers.PrimaryKeyRelatedField(
        queryset = Rack.objects.all(),
        source='rack',
        write_only = True
    )
    # total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PurchaseEntryForm
        fields = [
            "id",
            "purchase",
            "purchase_id",
            "item",
            "item_id",
            "rack",
            "rack_id",
            "batch_number",
            "brand_name",
            "quantity",
            "price",
            "total"
        ]
        depth = 1

    # def get_total(self, obj):
    #     return obj.total


class LossDamageSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        source='item',
        write_only=True
    )
    rack = RackSerializer(read_only = True)
    rack_id = serializers.PrimaryKeyRelatedField(
        queryset = Rack.objects.all(),
        source='rack',
        write_only=True
    )

    class Meta:
        model = LossDamage
        fields = [
            "id",
            "item",
            "item_id",
            "quantity",
            "price",
            "rack",
            "rack_id",
            "date",
            "remarks"
        ]
        depth = 1


class SalesSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )
    total = serializers.SerializerMethodField(read_only=True)

    #sales_item_total = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Sales

        fields = [
            "id",

            "customer",
            "customer_id",
            "voucher_type",
            "bill_number",
            "date",
            "remarks",
            "total"

        ]
        extra_kwargs = {
            'voucher_type': {'read_only': True}
        }

        depth = 1

    def get_total(self, obj):
        return obj.total

    def create(self, validated_data):
        sales = Sales.objects.create(**validated_data)
        sales.save()

        '''
		item_id = validated_data.get('item_id')
		price = validated_data['price']
		quantity = validated_data['quantity']
		item = get_object_or_404(Item , id= item_id)
		voucher_type = get_object_or_404(VoucherType, voucher_type = "Sales")
		ledger = Ledger.objects.create(
			item = item,
			quantity = quantity,
			price =price,
			voucher_type = voucher_type)
		ledger.save()
		'''

        return sales


class SalesEntryFormSerializer(serializers.ModelSerializer):
    sales = SalesSerializer(read_only=True)
    sales_id = serializers.PrimaryKeyRelatedField(
        queryset = Sales.objects.all(),
        source='sales',
        write_only= True
    )
    item = PurchaseEntryFormSerializer(read_only=True)
    item_id= serializers.PrimaryKeyRelatedField(
        queryset = PurchaseEntryForm.objects.all(),
        source = 'item',
        write_only = True
    )
    rack = RackSerializer(read_only=True)
    rack_id = serializers.PrimaryKeyRelatedField(
        queryset = Rack.objects.all(),
        source = 'rack',
        write_only= True
    )
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SalesEntryForm
        fields = [
            'id',
            'sales',
            'sales_id',
            'item',
            'item_id',
            'rack',
            'rack_id',
            'quantity',
            'price',
            'total']

    def get_total(self, obj):
        return obj.total


class PurchaseReturnSerializer(serializers.ModelSerializer):

    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=VendorDetail.objects.all(),
        source='vendor',
        write_only=True)
    total = serializers.SerializerMethodField(read_only=True)
    vat = serializers.SerializerMethodField(read_only=True)
    grand_total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PurchaseReturn
        fields = [
            "id",

            "vendor",
            "vendor_id",

            "voucher_type",


            "date",
            "remarks",
            "total",
            "vat",
            "grand_total"
        ]
        depth = 1
        extra_kwargs = {
            'voucher_type': {'read_only': True}
        }

    def get_total(self, obj):
        return obj.total

    def get_total(self, obj):
        return obj.total

    def get_vat(self, obj):
        return obj.vat

    def get_grand_total(self, obj):
        return obj.grand_total


class PurchaseReturnEntrySerializer(serializers.ModelSerializer):
    purchase_return = PurchaseReturnSerializer(read_only=True)
    purchase_return_id = serializers.PrimaryKeyRelatedField(
        queryset = PurchaseReturn.objects.all(),
        source='purchase_return',
        write_only= True
    )
    item = PurchaseEntryFormSerializer(read_only=True)
    item_id= serializers.PrimaryKeyRelatedField(
        queryset = PurchaseEntryForm.objects.all(),
        source='item',
        write_only=True
    )
    rack = RackSerializer(read_only=True)
    rack_id= serializers.PrimaryKeyRelatedField(
        queryset = Rack.objects.all(),
        source='rack',
        write_only = True
    )

    class Meta:
        model = PurchaseReturnEntryForm
        fields = [
            'id',
            'purchase_return',
            'purchase_return_id',
            'item',
            'item_id',
            'rack',
            'rack_id',
            'quantity',
            'price',
            'total',
        ]
        depth = 1


class SalesReturnSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SalesReturn
        fields = [
            'id',

            'customer',
            'customer_id',
            'voucher_type',

            'remarks',
            'date',
            'total',
            'bill_number'
        ]
        extra_kwargs = {
            'voucher_type': {'read_only': True}
        }
        depth = 1

    def get_total(self, obj):
        return obj.total


class SalesReturnEntrySerializer(serializers.ModelSerializer):
    sales_return = SalesReturnSerializer(read_only=True)
    item = PurchaseEntryFormSerializer(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SalesReturnEntryForm
        fields = [
            'sales_return',
            'item',
            'quantity',
            'price',
            'total']

    def get_total(self, obj):
        return obj.total


class LedgerSerializer(serializers.ModelSerializer):
    sales = SalesSerializer(read_only=True)
    purchase = PurchaseSerializer(read_only=True)

    class Meta:
        model = Ledger
        fields = [
            'id',
            'sales',
            'purchase'
        ]


class StockSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only = True)
    class Meta:
        model = Stock
        fields = [
            'item',
            'quantity',
            'rack'
        ]
        depth = 2


class StockTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransfer
        fields = "__all__"
        depth = 1


class PurchaseDetailSerializer(serializers.Serializer):

    customer_id = serializers.IntegerField(write_only=True)


class DateTime(serializers.ModelSerializer):
    class Meta:
        model = TestDate
        fields = "__all__"
