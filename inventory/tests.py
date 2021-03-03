from django.test import TestCase
from rest_framework import APITestcase
from django.urls import reverse
import json 


# Create your tests here.

class VendorTestCase(APITestCase):
    
    def test_add_vendor(self):
        data = {
            "name":"Rojesh Prajapati",
            "address":"Madhyapur Thimi",
            "contact":"9849423800",
            "pan_number":"1234"
        }
        
        