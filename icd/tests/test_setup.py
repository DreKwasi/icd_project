from rest_framework.test import APITestCase
from django.urls import reverse
import pandas as pd

# Class object for defining instructions for view test cases
class TestSetUP(APITestCase):

    # defining a setUp method to define urls and sample data for Post Method
    def setUp(self):
        self.codeslisturl = reverse('codes')
        self.fileuploadurl = reverse('fileUpload')
        self.sample_data = {"category_codes": "A001",
                            "diagnosis_codes": "12",
                            "full_code": "A122",
                            "abbrev_description": "Malaria",
                            "full_description": "Cold",
                            "category_title": "Something",
                            "version": 10
                            }
    
    # method to have the Post Method Ingest Data into the Test DB
    def createCode(self):
        response = self.client.post(reverse('codes'), self.sample_data)
        return response

    # method to create sample data in file
    def createFile(self):
        df = pd.DataFrame({"category_codes": "A001",
                            "diagnosis_codes": "12",
                            "full_code": "A122",
                            "abbrev_description": "Malaria",
                            "full_description": "Cold",
                            "category_title": "Something",
                            "version": 10
                            }, index=['row1'])
        df.to_csv("test.csv", index=False)


    # method to tidy up the test after it succeeds/fails 
    def tearDown(self) -> None:
        return super().tearDown()
