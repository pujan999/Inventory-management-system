from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import (
    VendorSerializer,
    ItemSerializer,
    PurchaseSerializer,
    RackSerializer,
    CustomerSerializer,
    LossDamageSerializer,
    SalesSerializer,
    PurchaseDetailSerializer,
    PurchaseReturnSerializer,
    UnitSerializer,
    SalesReturnSerializer,
    LedgerSerializer,
    CategorySerializer,
    VoucherTypeSerializer,
    PurchaseEntryFormSerializer,
    SalesEntryFormSerializer,
    SalesReturnEntrySerializer,
    PurchaseReturnEntrySerializer,
    StockTransferSerializer,
    StockSerializer,
    DateTime,
    StockTransferSerializer



    )
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from braces.views import CsrfExemptMixin
from .filter import *
from .models import (
    Item,
    VendorDetail,
    Purchase,
    Rack,
    Customer,
    LossDamage,
    Sales,
    PurchaseReturn,
    Unit,
    SalesReturn,
    Ledger,
    VoucherType,
    Category,
    Stock,
    PurchaseEntryForm,
    PurchaseReturnEntryForm,
    SalesEntryForm,
    SalesReturnEntryForm,
    StockTransfer


    )
from django.shortcuts import get_object_or_404



'''
use item as foreign key to rack 

'''


# Create your views here.



class VendorAPIView(APIView):

    def post(self, request):
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        qs = VendorDetail.objects.all().order_by('-id')
        serializer = VendorSerializer(qs, many= True)
        return Response(serializer.data, status =status.HTTP_200_OK)


class VoucherAPIView(APIView):
    def get(self,request):
        query_set = VoucherType.objects.all()
        serializer = VoucherTypeSerializer(query_set , many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        serializer = VoucherTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class VendorDetailAPIView(APIView):
    def get(self,request,id):
        query_set = get_object_or_404(VendorDetail, id= id)
        serializer = VendorSerializer(query_set)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id):
        print(request.data)
        query_set= get_object_or_404(VendorDetail , id =id )
        serializer = VendorSerializer(query_set, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request , id):
        query_set = get_object_or_404(VendorDetail, id= id)
        query_set.delete()
        msg = {"msg":"Item deleted sucessfully"}
        return Response(msg, status=status.HTTP_200_OK)

class CategoryAPIView(APIView):
    def get(self,request):
        query_set = Category.objects.all()
        serializer = CategorySerializer(query_set, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)





class CategoryDetailAPIView(APIView):
    def get(self, request, id):
        query_set = get_object_or_404(Category, id = id)
        serializer = CategorySerializer(query_set)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self,request,id):
        print(request.data)
        query_set = get_object_or_404(Category, id = id)
        serializer = CategorySerializer(query_set, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        query_set = get_object_or_404(Category, id = id)
        query_set.delete()
        msg = {"msg":"Category Deleted successfully"}
        return Response(msg, status = status.HTTP_200_OK)










class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter





class UnitAPIView(APIView):

    def get(self, request):
        query_set = Unit.objects.all().order_by('-id')
        serializer = UnitSerializer(
            query_set,
            many =True
            )

        return Response(
            serializer.data,
            status =status.HTTP_200_OK
            )

    def post(self, request):
        serializer = UnitSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
                )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
            )



class UnitDetailAPIView(APIView):

    def get(self, request,id):
        query_set = get_object_or_404(
            Unit,
            id=id
            )
        serializer = UnitSerializer(query_set)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )


    def put(Self, request, id):
        query_set = get_object_or_404(
            Unit,
            id=id
            )

        serializer = UnitSerializer(
            query_set,
            data = request.data,
            partial = True
            )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
                )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def delete(self,request, id):
        query_set = get_object_or_404(
            Unit,
            id = id
            )
        query_set.delete()

        msg = {
        "msg":"Varitaion deleted successfully"
        }

        return Response(
            msg,
            status = status.HTTP_200_OK
            )




class AddItemAPI(APIView):



    def get(self,request):
        query_set = Item.objects.all()
        serializer = ItemSerializer(query_set,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = ItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()


            return Response(serializer.data, status = status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)





class ItemDetailAPI(APIView):
    permissions_classes = [IsAuthenticated,]

    def get(self,request,id):
        query_set = get_object_or_404(Item, id= id)
        serializer = ItemSerializer(query_set)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,id):

        query_set = get_object_or_404(Item, id=id)
        serializer = ItemSerializer(
            query_set,
            data= request.data,
            partial= True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        query_set = get_object_or_404(Item,id = id)
        query_set.delete()
        msg={"msg":"Item deleted sucessfully"}
        return Response(msg,status= status.HTTP_200_OK)






class PurchaseAPIView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']


    def post (self,request):
        print(request)
        item = request.data.pop('item')


        print(item)
        print(f"this is request data after pop {request.data}")
        serializer = PurchaseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            for i in item:
                print(serializer.data['id'])

                purchase = get_object_or_404(Purchase, id = serializer.data['id'])
                print("I'm Here")
                i['purchase_id']=purchase.id
                print(i)
                ser =PurchaseEntryFormSerializer(data= i)
                # print(ser.data)
                if ser.is_valid():

                    ser.save()
                    print('saved')
                print(ser.errors)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)

 
 


    def get(self,request,*args, **kwargs):
        qs = Purchase.objects.all().order_by('-id')
        date = request.query_params.get('date')
        print(request.query_params.get('date'))
        month =request.query_params.get('month')
        year = request.query_params.get('year')

        if date:
            qs = Purchase.objects.filter(date = date)
            serializer = PurchaseSerializer(qs, many=True)
            return Response(serializer.data)
        if month:
            qs = Purchase.objects.filter(date__month = month)
        if year:
            qs = Purchase.objects.filter(date__year = year)

        serializer = PurchaseSerializer(qs, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)






class PurchaseDetailEditAPIView(APIView):

    def get(self, request, id):
        query_set = get_object_or_404(Purchase,id =id)
        serializer = PurchaseSerializer(query_set)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, id):
        qs = get_object_or_404(Purchase, id = id )
        qs.delete()
        return Response({"msg":"Purchase deleted sucessfully"})

    def put(self, request, id):
        qs = get_object_or_404(Purchase , id=id)
        serializer = PurchaseSerializer(qs, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
   
   
   


 


'''
    def put(self,request,id):
        query_set = get_object_or_404(Purchase, id = id)
        serializer = PurchaseSerializer(
            query_set, 
            data= request.data, 
            partial = True
            )
        if serializer.is_valid():
            stock = get_object_or_404(Stock, item= query_set.item)
            quantity = request.data.get('quantity')
            if request.data.get('rack_id'):
                rack_id = request.data.get('rack_id')
                rack = get_object_or_404(Rack, id = rack_id)
                stock.rack= rack
            if quantity:
                previous_quantity = stock.quantity
                updated_quantity = previous_quantity - query_set.quantity +quantity
                stock.quantity =updated_quantity

            stock.save()
            
            prevous_quantity = int(query_set.quantity)
            print(f"this is previous quantity {prevous_quantity}")
            quantity = int(request.data.get('quantity'))
            print(quantity)
            item_quantity = int(query_set.item.quantity)
            item = query_set.item
            updated_quantity = (item_quantity - prevous_quantity + quantity)
            print(item.quantity)
            if quantity:
                item.quantity = updated_quantity
                item.save()
                print(f"this is updated_quantity: {item.quantity}")
                
            #serializer.save()
            ##return Response(serializer.data, status= status.HTTP_200_OK)

        #return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
'''
'''
    def delete(self,request,id):
        query_set = get_object_or_404(StockDetail, id=id)
        query_set.delete()
        msg = {"msg":"Stock detail deleted sucessfully"}
        return Response(msg, status= status.HTTP_200_OK)
        '''

class PurchaseAllItemAPIView(APIView):
    def get(self,request):
        query_set = PurchaseEntryForm.objects.all()
        serializer = PurchaseEntryFormSerializer(query_set, many= True)
        return Response(serializer.data)
 
 
class PurchaseReturnAPIView(APIView):

    def get(self,request):
        query_set = PurchaseReturn.objects.all().order_by('-id')
        serializer= PurchaseReturnSerializer(
            query_set,
            many=True
            )
        return Response(
            serializer.data,
            status= status.HTTP_200_OK
            )

    def post(self,request):

        item = request.data.pop('item')
        print(f"This is data after pop {request.data}")
        print(item)
        serializer = PurchaseReturnSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print("I'm Here")
            for i in item:
                purchase_return = get_object_or_404(PurchaseReturn,id= serializer.data['id'])
                i['purchase_return_id']=purchase_return.id
                ser = PurchaseReturnEntrySerializer(data= i)
                # print("I'm Here")
                item = get_object_or_404(PurchaseEntryForm, id=i['item_id'])
                if item.quantity <= int(i['quantity']):
                    msg={"msg":"You dont have that much quanity"}
                    return Response(msg)
                if ser.is_valid():
                    print(i)
                    ser.save()
                    item.quantity -= int(i['quantity'])
                    item.save()
                print(ser.errors)
            return Response(serializer.data)
        return Response(serializer.errors)
        # 		item_id = i['item_id']
        # 		if item_id is None:
        # 			msg ={"msg":"item_id is required"}
        # 		rack_id = i['rack_id']
        # 		if rack_id is None:
        # 			msg={"msg":"rack_id is required"}
        # 		quantity = int(i['quantity'])
        # 		price = int(i['price'])
        # 		purchase_return_item  = PurchaseReturnEntryForm.objects.create(
        # 			item = get_object_or_404(Item, id = item_id),
        # 			purchase_return = get_object_or_404(PurchaseReturn, id = serializer.data['id']),
        # 			quantity = quantity,
        # 			rack = get_object_or_404(Rack, id = rack_id),
        # 			price = price
        # 			)
        # 		item = get_object_or_404(Item, id = item_id)
        # 		stock = get_object_or_404(Stock, item = item)


        # 		if stock.quantity<= quantity:
        # 			msg = {"msg":"You dont have that much stock for purchase return "}
        # 			return Response(msg )
        # 		stock.quantity -= int(quantity)
        # 		stock.quantity_after_transfer -= int(quantity)
        # 		stock.save()
        # 		purchase_return_item.save()
        # 	return Response(serializer.data)
        # return Response(serializer.errors)

        '''
        serializer= PurchaseReturnSerializer(data= request.data)
        if serializer.is_valid():
            
            quantity = request.data.get('quantity')
            item_id = request.data.get('item_id')
            item = get_object_or_404(Item, id= item_id)
            stock = get_object_or_404(Stock, item = item)
            
Itequantity:
                msg = {"msg":"You dont have that much stock for purchase return "}
                return Response(msg )
            stock.quantity -= quantity
            stock.save()
            
            
                    
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
            '''




class PurchaseReturnDetailAPIView(APIView):

    def get(self,request, id):
        query_set = get_object_or_404(
            PurchaseReturn,
            id=id
            )
        serializer= PurchaseReturnSerializer(query_set)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )


    def put(self,request,id):
        query_set = get_object_or_404(
            PurchaseReturn,
            id=id
            )
        serializer= PurchaseReturnSerializer(
            query_set,
            data=request.data,
            partial=True
            )
        if serializer.is_valid():

            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def delete(self,request,id):
        query_set = get_object_or_404(PurchaseReturn, id= id)
        purchase_return_entry= query_set.purchasereturnentryform_set.all()
        for p in purchase_return_entry:
            item = p.item
            stock = get_object_or_404(Stock, item= item )
            stock.quantity += p.quantity
            stock.quantity_after_transfer += p.quantity
            stock.save()
        purchase_return_entry.delete()
        query_set.delete()
        return Response({"msg":"Purchase deleted sucessfully"})

class PurchaseReturnEntryFormAPIView(APIView):
    def get(self,request,id):
        item = get_object_or_404(PurchaseReturnEntryForm, id = id)
        serializer = PurchaseReturnEntrySerializer(item)
        return Response(serializer.data)
    
    def put(self, request,id):
        print(request.data)
        item = get_object_or_404(PurchaseReturnEntryForm, id = id)
        serializer = PurchaseReturnEntrySerializer(item, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(f"this is serializer data{serializer.data}")
        print(f"this is serializer errors {serializer.errors}")
        return Response(serializer.errors)
    
    def delete(self,request,id):
        item = get_object_or_404(PurchaseReturnEntryForm, id = id)
        item.delete()
        msg={"msg":"Item deleted successfully"}
        return Response(msg)




    
class PurchaseReturnEntryFormPostAPIView(APIView):
    def get(self,request):
        item = PurchaseReturnEntryForm.objects.all()
        serializer = PurchaseReturnEntrySerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseReturnEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        






class RackAPIView(APIView):

    def post(self,request):
        serializer = RackSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    def get(self,request):
        qs = Rack.objects.all().order_by('-id')
        serializer = RackSerializer(qs, many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)






class RackDetailAPIView(APIView):
    def get(self,request,id):
        query_set = get_object_or_404(Rack, id= id)
        serializer = RackSerializer(query_set)
        return Response(serializer.data,status= status.HTTP_200_OK)



    def put(self,request,id):
        query_set = get_object_or_404(Rack,id=id)
        serializer = RackSerializer(
            query_set,
            data=request.data,
            partial =True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    def delete(self, request, id):
        query_set = get_object_or_404(Rack, id= id)
        query_set.delete()
        msg = {"msg":"Rack deleted sucessfully"}
        return Response(msg, status= status.HTTP_200_OK)





class CustomerAPIView(APIView):

    def get(self,request):
        query_set = Customer.objects.all().order_by('-id')
        serializer = CustomerSerializer(query_set, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)



    def post(self,request):
        print(request.data)
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)







class CustomerDetailAPIView(APIView):

    def get(self,request, id):
        query_set = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(query_set)
        return Response(serializer.data, status = status.HTTP_200_OK)



    def put(self,request,id):
        print(request.data)
        query_set = get_object_or_404(Customer, id= id)
        serializer = CustomerSerializer(query_set, data = request.data ,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,id):
        query_set = get_object_or_404(Customer, id=id)
        query_set.delete()
        msg = {"msg":"Customer deleted sucessfully"}
        return Response(msg , status =status.HTTP_200_OK)







class LossDamageAPIView(APIView):

    def get(self,request):
        query_set = LossDamage.objects.all().order_by('-id')
        serializer = LossDamageSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self,request):
        print(request.data)
        for r in request.data:
            print(r)
            serializer = LossDamageSerializer(data= r)
            if serializer.is_valid():
                item_id  = r.get('item_id')
                item = get_object_or_404(Item , id = item_id)
                stock = get_object_or_404(Stock, item = item)
                quantity = int(r.get('quantity'))
                if stock.quantity <= quantity:
                    msg ={"msg": "You dont have that much quantity in stock"}
                    return Response(msg)
                stock.quantity -= r.get('quantity')
                stock.save()
                serializer.save()
   
            print(item)

        return Response({"msg":"loss and damage created successfully"})






class LossDamageDetailAPIView(APIView):

    def get(self,request,id):
        query_set = get_object_or_404(LossDamage, id=id)
        serializer = LossDamageSerializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self,request,id):
        query_set = get_object_or_404(LossDamage, id=id)
        serializer = LossDamageSerializer(query_set, data= request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    def delete(self,request,id):
        query_set = get_object_or_404(LossDamage, id= id)
        query_set.delete()
        return Response({"msg":"Lost damage deleted sucessfully"}, status= status.HTTP_200_OK)







class SalesAPIView(APIView):
    def get(self, request):
        query_set = Sales.objects.all().order_by('-id')
        serializer = SalesSerializer(query_set, many= True)
        return Response(serializer.data,status= status.HTTP_200_OK)




    def  post(self,request):
        item = request.data.pop('item')
        serializer = SalesSerializer(data = request.data)


        if serializer.is_valid():
            serializer.save()
            for i in item:
                sales = get_object_or_404(Sales, id = serializer.data['id'])
                i['sales_id']= sales.id
                ser = SalesEntryFormSerializer(data = i )
                item = get_object_or_404(PurchaseEntryForm, id= i['item_id'])

                if item.quantity <= i['quantity']:
                    msg = {"msg":"You don't have that much item in stock "}
                if ser.is_valid():
                    ser.save()

                    item.quantity -= int(i['quantity'])
                    item.save()
                print(ser.errors)

            return Response(serializer.data)
        return Response(serializer.errors)



        # 		item_id = i['item_id']
        # 		rack_id = i['rack_id']
        # 		if rack_id is None:
        # 			msg = {"msg":"rack_id is required"}
        # 			return Response(msg)
        # 		sales = get_object_or_404(Sales, id= serializer.data['id'])
        # 		quantity = int(i['quantity'])
        # 		price = int(i['price'])
        # 		related_item = get_object_or_404(Item, id = item_id)
        # 		stock = get_object_or_404(Stock, item = related_item)

        # 		if stock.quantity <= quantity:
        # 			msg = {"msg":"Yoy don't have that much stock "}
        # 			return Response(msg)
        # 		stock.quantity -= int(quantity)
        # 		stock.quantity_after_transfer -= int(quantity)
        # 		stock.save()


        # 		sales_item = SalesEntryForm.objects.create(
        # 			sales = sales,
        # 			item = related_item,
        # 			rack = get_object_or_404(Rack, id = rack_id),
        # 			quantity = quantity,
        # 			price = price
        # 			)
        # 		sales_item.save()
        # 	return Response(serializer.data)

        # return Response(serializer.errors)

        '''
        serializer = SalesSerializer(data= request.data)
        
        item_id = request.data.get('item_id')
        price = request.data.get('price')
        quantity = request.data.get('quantity')
        item = get_object_or_404(Item , id= item_id)
        stock = get_object_or_404(Stock, item = item)
        #voucher_type = get_object_or_404(VoucherType, voucher_type = "Sales")
        stock.quantity -= quantity
        if stock.quantity <= quantity:
            msg = {"msg":"Yoy don't have that much stock "}
            return Response(msg)
        stock.save()

        ledger = Ledger.objects.create(
            item = item,
            quantity = quantity,
            price =price,
            voucher_type = voucher_type)
        ledger.save()
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

'''



class SalesDetailAPIView(APIView):

    def get(self,request,id):
        query_set = get_object_or_404(Sales, id= id)
        serializer = SalesSerializer(query_set)
        return Response(serializer.data, status= status.HTTP_200_OK)



    def put(self,request,id):
        query_set = get_object_or_404(Sales, id=id)
        serializer = SalesSerializer(
            query_set,
            data=request.data,
            partial= True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



    def delete(self,request, id):
        query_set = get_object_or_404(Sales, id= id)
        sales_entry = query_set.salesentryform_set.all()
        for s in sales_entry:
            stock = get_object_or_404(Stock, item = s.item)
            stock.quantity += s.quantity
            stock.quantity_after_transfer += s.quantity
            stock.save()
        sales_entry.delete()
        query_set.delete()
        msg = {
        "msg":"Item Deleted Sucessfully",
        }
        return Response(msg, status= status.HTTP_200_OK)



class SalesReturnAPIView(APIView):

    def get(self, request):
        query_set = SalesReturn.objects.all().order_by('-id')
        serializer = SalesReturnSerializer(
            query_set,
            many = True
            )
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
            )


    def post(self, request):
        items = request.data.pop('item')
        serializer = SalesReturnSerializer(data= request.data)
        customer_id = request.data.get('customer_id')





        if serializer.is_valid():
            serializer.save()
            for i in items:
                item_id = i['item_id']
                rack_id = i['rack_id']
                quantity = int(i['quantity'])
                price = int(i['price'])

                item = get_object_or_404(Item, id = item_id)

                stock = get_object_or_404(Stock, item = item )
                stock.quantity += int(quantity)
                stock.quantity_after_transfer += int(quantity)
                stock.save()
                sales_return_item = SalesReturnEntryForm.objects.create(
                    sales_return = get_object_or_404(SalesReturn, id = serializer.data['id']),
                    item = item,
                    quantity = quantity,
                    rack = get_object_or_404(Rack, id = rack_id),
                    price = price
                    )
                sales_return_item.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        '''
        serializer = SalesReturnSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            item_id = request.data.get('item_id')

            item = get_object_or_404(Item , id =item_id)
            stock = get_object_or_404(Stock, item = item )
            print(stock.quantity)
            quantity = request.data.get('quantity')
            stock.quantity += quantity
            print(stock.quantity)
            stock.save()
            serializer.save()
            return Response(
                serializer.data, 
                status = status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
        '''



class SalesReturnDetailAPIView(APIView):

    def get(self,request,id):
        query_set = get_object_or_404(
            SalesReturn,
            id = id
            )
        serializer = SalesReturnSerializer(query_set)

        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request , id):
        query_set = get_object_or_404(
            SalesReturn,
            id = id
            )
        serializer = SalesReturnSerializer(
            query_set,
            data = request.data,
            partial = True
            )

        if serializer.is_valid():
            '''
            quantity = request.data.get('quantity')
            previous_quantity = query_set.quantity
            item = query_set.item
            stock = get_object_or_404(Stock, item = item)
            print(item)
            updated_quantity = stock.quantity - previous_quantity + quantity
            stock.quantity = updated_quantity
            stock.save()
   '''
            serializer.save()

            return Response(
                serializer.data,
                status = status.HTTP_200_OK
                )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )



    def delete(self, request, id):
        query_set = get_object_or_404(
            SalesReturn,
            id = id
            )
        sales_return_entry = query_set.salesreturnentryform_set.all()
        for s in sales_return_entry:
            stock = get_object_or_404(Stock, item = s.item )
            stock.quantity -= s.quantity
            stock.quantity_after_transfer  -= s.quantity
            stock.save()
        sales_return_entry.delete()
        query_set.delete()

        msg = {"msg":"sale return deleted sucessfully"}
        return Response(
            msg,
            status = status.HTTP_400_BAD_REQUEST
            )

'''
This api view view is to get detail about the stock and edit the detail
'''
class PurchaseEntryFormDetail(APIView):
    def get(self,request,id):
        stock = get_object_or_404(PurchaseEntryForm, id = id)
        serialier = PurchaseEntryFormSerializer(stock)
        return Response(serialier.data)
    
    def put(self, request, id):
        stock = get_object_or_404(PurchaseEntryForm, id=id)
        serializer = PurchaseEntryFormSerializer(stock, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        stock = get_object_or_404(PurchaseEntryForm , id = id)
        stock.delete()
        msg ={"msg":"Item Deletes successfully"}
        return Response(msg)
        



class PurchaseItemAPIView(APIView):
    def get(self,request,id):
        purchase = get_object_or_404(Purchase, id = id)
        qs= purchase.purchaseentryform_set.all()
        serializer = PurchaseEntryFormSerializer(qs, many = True)
        return Response(serializer.data)


class SalesItemAPIView(APIView):
    def get(self,request,id):
        sales = get_object_or_404(Sales, id = id)
        qs = sales.salesentryform_set.all()
        serializer = SalesEntryFormSerializer(qs, many = True)
        return Response(serializer.data)


class SalesReturnItemAPIView(APIView):
    def get(self,request,id):
        sales_return = get_object_or_404(SalesReturn ,id = id)
        qs = sales_return.salesreturnentryform_set.all()
        serializer = SalesReturnEntrySerializer(qs , many= True)
        return Response (serializer.data)


class PurchaseReturnItemAPIView(APIView):
    def get(self, request, id):
        purchase_return = get_object_or_404(PurchaseReturn, id = id)
        qs = purchase_return.purchasereturnentryform_set.all()
        serializer = PurchaseReturnEntrySerializer(qs , many = True)
        return Response(serializer.data)

class VendorPurchaseAPIView(APIView):


    def get(self,request,id):
        vendor = get_object_or_404(VendorDetail, id=id)
        query_set = vendor.purchase_set.all().order_by('-date')

        serializer = PurchaseSerializer(query_set, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)

class VendorPurchaseReturnAPIView(APIView):
    def get(self,request,id):
        vendor = get_object_or_404(VendorDetail, id = id)
        query_set = vendor.purchasereturn_set.all()
        serializer = PurchaseReturnSerializer(query_set, many= True)
        return Response(serializer.data)
    






class CustomerSalesAPIView(APIView):


    def get(self,request,id):
        customer = get_object_or_404(Customer, id=id)
        query_set = customer.sales_set.all()
        serializer = SalesSerializer(query_set, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)


class CustomerSalesReturnAPIView(APIView):
    def get(self, request, id):
        customer = get_object_or_404(Customer, id = id)
        query_set = customer.salesreturn_set.all()
        serializer = SalesReturnSerializer(query_set, many = True)
        return Response(serializer.data)
    




class StockInAPIView(APIView):


    def get(self,request):
        query_set = Purchase.objects.all().order_by('-date')
        serializer = PurchaseSerializer(query_set, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)





class StockOutOrder(APIView):


    def get(self, request):
        query_set = StockOut.objects.all().order_by('-date')
        serializer = StockOutSerializer(query_set, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )



class LedgerAPIView(APIView):

    def get(self,request):
        query_set = Ledger.objects.all().order_by('-id')
        serializer = LedgerSerializer(query_set, many = True)
        return Response(
            serializer.data ,
            status = status.HTTP_200_OK
            )
  
  
class StockAPIView(APIView):
    def get(self,request):
        qs = Stock.objects.all()
        serializer = StockSerializer(qs, many = True)
        return Response(serializer.data)  
    
    
class StockTransferAPIView(APIView):
    def post(self,request,id):
        stock = get_object_or_404(Stock, id = id)
        quantity = request.data.get('quantity')
        rack_id = request.data.get('rack_id')
        rack = get_object_or_404(Rack, id = rack_id)
        
        if quantity >= stock.quantity_after_transfer:
            msg = {"msg":"You don't have that much quantity in stock"}
            return Response(msg)
        stock_transfer = StockTransfer.objects.create(stock = stock,quantity = quantity,rack = get_object_or_404(Rack, id = rack_id))
        stock_transfer.save()
        stock.quantity_after_transfer = stock.quantity - quantity
        stock.save()
            
        msg = {
            "msg":f"Stock Transfered from {stock.rack} to {rack.rack_name}"
        }
        return Response(msg)
    
    
class StockTransferAllAPIView(APIView):
    def get(self,request):
        qs = StockTransfer.objects.all()
        serializer = StockTransferSerializer(qs , many = True)
        return Response(serializer.data)

        

class VendorNameReturn(APIView):
    def get(self, request , id):
        qs =get_object_or_404(VendorDetail , id = id )
        serializer = VendorSerializer(qs )
        return Response(serializer.data)


class StockRelatedToRackAPIView(APIView):
    def get(self,request, id ):
        rack = get_object_or_404(Rack, id= id)
        qs = StockTransfer.objects.filter(rack = rack )
        serializer = StockTransferSerializer(qs, many = True)
        return Response(serializer.data)
    
    
    
class TestDateAPIView(APIView):
    def post(self,request):
        serializer = DateTime(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request):
        qs = TestDate.objects.all()
        ser = DateTime(qs , many= True)
        return Response(ser.data)
    
    
    

class ItemCountAPIView(APIView):
    def get(self, request):
        
        stock = Stock.objects.all()
        stock_item_total =0
        total = 0
        for s in stock:
            total += s.quantity
            stock_item_total += s.quantity_after_transfer
            
        msg ={"total-item":total,"stock_total":stock_item_total}
        return Response(msg)
    
    
    

class ItemInRackAPIView(AddItemAPI):
    #send rack of rack to get all the item in rack 
    def get(self,request,id):
        rack = get_object_or_404(Rack,id =id)
        stock = rack.stocktransfer_set.all()
        serializer = StockTransferSerializer(stock, many=True)
        return Response(serializer.data)
        
    

        
    
        

 








