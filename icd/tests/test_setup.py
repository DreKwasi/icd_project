from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class TestSetUP(APITestCase):

    def setUp(self):
        self.codeslisturl = reverse('codes')
        self.sample_data = {"category_codes": "A001",
                    "diagnosis_codes": "12",
                    "full_code": "A122",
                    "abbrev_description": "Malaria",
                    "full_description": "Cold",
                    "category_title": "Something",
                    "version": 10
                        }
        pass
    
    def createCode(self):
        response = self.client.post(reverse('codes'), self.sample_data)
        return response


    def tearDown(self) -> None:
        return super().tearDown()
