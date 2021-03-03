from django.db import models
from django.contrib.auth import get_user_model
import uuid 
import random

User = get_user_model()

def get_item_code():
    item_uuid = str(uuid.uuid1(random.randint(0, 281474976710655)))
    return item_uuid


def create_new_ref_number():
      return str(random.randint(100000, 9999999999999))

#Created models for VendorDetail
class VendorDetail(models.Model):
    company_name = models.CharField(max_length = 1000)
    address = models.CharField(max_length =1000 , default = "Kathmandu")
    name = models.CharField(max_length=255)
    company_contact =  models.CharField(max_length=15)
    contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255,unique=True)
    title = models.CharField(default='Debtor', max_length=255)

    def __str__(self):
        return self.name

    @property
    def get_purchase(self):
        return self.purchase_set.all()

'''
    @property
    def get_purchase_sum(self):
        total = 0
        purchase = self.purchase_set.all()
        for p in purchase:
            total += p.get_total

        return total

'''


        

    
    

#Created model Item


class Unit(models.Model):
    symbol = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.symbol

class Category(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

'''
class OpeningBalance(models.Model):
    quantity= models.PositiveIntegerField()
    rate= models.FloatField()

    def __str__(self):
        return f"{self.quantity}"

    @property
    def total(self):
        return self.quantity * self.rate
 '''   


class Item(models.Model):


    local_name = models.CharField(max_length=1000, null = True)
    unit = models.ForeignKey(Unit, on_delete = models.CASCADE, null =True)
    item_limit = models.PositiveIntegerField(null = True)
    
    item_name = models.CharField(max_length=255)
    #item_code = models.CharField(max_length=36, default=random.randint(100000, 9999999999999))
    item_code = models.CharField(max_length=36, default=uuid.uuid4)
    #item_code = models.CharField(default=create_new_ref_number(), max_length=255)
    
    category = models.ForeignKey(Category,on_delete = models.CASCADE, null = True)



    
    

    def __str__(self):
        return self.item_name
    

class Rack(models.Model):
    
    rack_name = models.CharField(max_length=1000, null = True)

    def __str__(self):
        return self.rack_name

class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    rack = models.ForeignKey(Rack , on_delete = models.CASCADE, null = True)
    quantity_after_transfer = models.PositiveIntegerField(default= 0 )

    def __str__(self):
        return self.item.item_name


   

    

    
    

    




#Created models Rack



class VoucherType(models.Model):
    CHOICES = (
        ('Sales','Sales'),
        ('SalesReturn','Sales Return'),
        ('PurchaseReturn','Purchase Return'),
        ('Purchase','Purchase'),
        ('LostDamage', 'Lost Damage')
        )
    voucher_type = models.CharField(choices =CHOICES, max_length=1000)

    def __str__(self):
        return self.voucher_type




class Purchase(models.Model):
    
    vendor_detail = models.ForeignKey(VendorDetail,on_delete=models.CASCADE, null= True)
    
    
    voucher_type = models.CharField(default = "Purchase", max_length = 1000)
    bill_number = models.CharField(max_length=255)
    rack_name = models.ForeignKey(Rack,on_delete=models.CASCADE,null=True)
    bill_image = models.ImageField(upload_to="bill/",null=True)
    date = models.DateField()
    #voucher_type = models.ForeignKey(VoucherType, on_delete= models.CASCADE, null = True)
    #voucher_number = models.PositiveIntegerField(null = True)
    remarks = models.TextField()

    def __str__(self):
        return self.vendor_detail.name


    @property
    def total(self):
        total = 0 
        qs = self.purchaseentryform_set.all()
        for q in qs:
            total = q.total + total
        return total
    
    @property
    def vat(self):
        vat = "13%"
        return vat
    
    
    @property
    def total_after_vat(self):
        vat = 0.13
        vat_amount = vat * self.total
        total = vat_amount + self.total
        return total
    
'''
    @property
    def get_total(self):
        return self.price * self.quantity
'''




'''
Its Like a stock 

all the purchase item are store here 
It contain the data like item, quantity, price , batch number, 
and Rack where it is stored
'''

class PurchaseEntryForm(models.Model):
    purchase= models.ForeignKey(Purchase, on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack , on_delete = models.CASCADE, null = True)
    quantity = models.IntegerField()
    price = models.FloatField()
    batch_number = models.CharField(max_length=1000, null =True)
    brand_name = models.CharField(max_length=1000, null = True)
    

    def __str__(self):
        return self.item.item_name
    
    
    @property
    def total(self):
        return int(self.quantity) * int(self.price)




'''
This is the table for purchase return which cointain the information about all the item That needs to be return to the vendor

This contain the information about the vendor where it was purchased from 


'''

class PurchaseReturn(models.Model):
    #item = models.ForeignKey(Item, on_delete= models.CASCADE, null = True)
    vendor = models.ForeignKey(VendorDetail, on_delete = models.CASCADE, null = True)
   # quantity = models.PositiveIntegerField()
    voucher_type = models.CharField(default = "Purchase Return",max_length = 1000)
    
    date = models.DateField()
    remarks = models.CharField(max_length = 1000 , null = True)

    def __str__(self):
        return self.vendor.name

    @property
    def total(self):
        total = 0 
        qs = self.purchasereturnentryform_set.all()
        for q in qs:
         total = q.total + total
          
        return total
    
    @property
    def vat(self):
        vat = "13%"
        return vat
    
    @property
    def grand_total(self):
        vat = 0.13
        vat_amount = vat*self.total
        total = vat_amount+self.total
        return total
    


'''
This table containt the information about the item for purchase return 
This table also contain information about the item quantity and its price for purchase return 

'''
class PurchaseReturnEntryForm(models.Model):
    purchase_return = models.ForeignKey(PurchaseReturn, on_delete = models.CASCADE)
    item = models.ForeignKey(PurchaseEntryForm, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    rack = models.ForeignKey(Rack, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.item.item.item_name

    @property
    def total(self):
        return int(self.quantity) * int(self.price)






'''
This table contain all the information about the customer 

'''
class Customer(models.Model):
   #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length = 100 , default = "None")
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=1000, null = True)
    company_contact = models.CharField(max_length=15 , null = True)
    email = models.EmailField()
    contact = models.CharField(max_length=255)
    
    pan_number = models.CharField(max_length=255, null = True, unique=True)
    title = models.CharField(max_length=255, default='Creditor')

    def __str__(self):
        return self.name


    #sales belonging to the customer 

'''    
    @property
    def  customer_sales(self):
        return self.sales_set.all()




    #Total sum that customer have stocked out from user 
    @property
    def customer_sales_total(self):
        total = 0
        sales = self.sales_set.all()
        for sale in sales:
            total += sale.sales_item_total

        return total
    
''' 

    




'''
This table contain all the information about the item that is in loss due to damage
'''
class LossDamage(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(PurchaseEntryForm,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    # rack = models.ForeignKey(Rack, on_delete = models.CASCADE, default=1)
    remarks = models.CharField(max_length = 1000 , null = True)
    date = models.DateField(auto_now_add=True ,null= True)

    def __str__(self):
        return self.item.item.item_name
    


    

'''
this table contain all the information about the sales voucher or bill

'''
class Sales(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    #quantity = models.PositiveIntegerField()
   # price = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    bill_number = models.CharField(null=True,blank=True,max_length=100)
    voucher_type = models.CharField(default = "Sales", max_length = 1000)

    date = models.DateField(auto_now_add=True, null=True)
    remarks = models.CharField(max_length = 1000 , null = True)

    def __str__(self):
        return self.customer.name

    @property
    def total(self):
        total = 0 
        qs = self.salesentryform_set.all()
        for q in qs:
            total = q.total + total
        return total

    '''
    @property
    def sales_item_total(self):
        return self.quantity * self.price
    '''
'''
This table contain all the information about the item that is sold to the customer

'''
class SalesEntryForm(models.Model):
    sales = models.ForeignKey(Sales, on_delete = models.CASCADE)
    item = models.ForeignKey(PurchaseEntryForm, on_delete = models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete = models.CASCADE, null = True)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.item.item.item_name


    @property
    def total(self):
        return self.quantity * self.price



    
'''
This table contain the information about the customer to who return the product
'''
class SalesReturn(models.Model):
   # item = models.ForeignKey(Item, on_delete = models.CASCADE, null = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE , null = True)
    voucher_type = models.CharField(default = "Sales Return",max_length = 1000)
    
    #quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add = True)
    remarks = models.CharField(max_length = 1000 , null = True)
    bill_number = models.CharField(max_length=1000, null = True)
    

    def __str__(self):
        return self.customer.name

    @property
    def total(self):
        total = 0 
        qs = self.salesreturnentryform_set.all()
        for q in qs:
            total = q.total + total

        return total
'''
This table contain all the information about the item that is returned from the customer
'''
class SalesReturnEntryForm(models.Model):
    sales_return = models.ForeignKey(SalesReturn, on_delete = models.CASCADE)
    item = models.ForeignKey(PurchaseEntryForm , on_delete = models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete = models.CASCADE, null = True)
    quantity = models.PositiveIntegerField()
    price  = models.FloatField()

    def __str__(self):
        return self.item.item_name

    @property
    def total(self):
        return self.quantity * self.price






'''
This table contain all the information about the item that is transfered from one rack to another
'''
class StockTransfer(models.Model):
    item = models.ForeignKey(PurchaseEntryForm, on_delete= models.CASCADE, null = True)
    rack = models.ForeignKey(Rack, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    


    def __str__(self):
        return  self.rack.name 



class Ledger(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE, null = True)
    voucher_type = models.ForeignKey(VoucherType, on_delete= models.CASCADE, null = True)
    quantity = models.PositiveIntegerField( null = True)
    price = models.FloatField(null = True)
    date = models.DateTimeField(auto_now_add =True , null = True)

    def __str__(self):
        return self.item.name

    def get_total(self):
        return self.price * self.quantity
    
    
    
    
    
class TestDate(models.Model):
    date = models.DateField()
    






        












'''
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    local_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255)
    item_limit = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.item_name

class VendorDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    company_contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Rack(models.Model):
    rack_number = models.PositiveIntegerField()

    def __str__(self):
        return self.rack_number
class StockDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    vendor_detail = models.ForeignKey(VendorDetail,on_delete=models.DO_NOTHING)
    batch_number = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    bill_number = models.CharField(max_length=255)
    rack_number = models.ForeignKey(Rack,on_delete=models.DO_NOTHING,null=True)
    bill_image = models.ImageField(upload_to="bill/")
    date = models.DateField(auto_now_add=True)
    item_brand_name = models.CharField(max_length=255)
    remarks = models.TextField()

    def __str__(self):
        return self.item.item_name


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    company_contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LostDamage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    batch_number = models.CharField(max_length=255)

    def __str__(self):
        return self.item.item_name


class StockOut(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    bill_number = models.CharField(null=True,blank=True,max_length=100)

'''

#hr@prixa.org