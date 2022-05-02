from .test_setup import TestSetUP #Importing TestSetUP Class for inheritance
from django.urls import reverse #Importing reverse function to use url names for endpoints
from icd.models import Codes #Importing Codes table from Models
from django.core.files.uploadedfile import SimpleUploadedFile #Class for handling file imports into POST methods.

# Class Object for Testing Views through their respective endpoints
class TestViews(TestSetUP):

    # Method to test the correct list view
    def test_correct_list_view(self):
        response = self.client.get(self.codeslisturl)
        self.assertEqual(response.status_code, 200)

    # Method to test the wrong list view
    def test_wrong_list_view(self):
        response = self.client.get('api/code')
        self.assertEqual(response.status_code, 404)

    # Method to test the create views
    def test_correct_create_view(self):
        prev_db_count = Codes.objects.all().count()
        response = self.createCode()
        db_count = Codes.objects.all().count()
        self.assertNotEqual(prev_db_count, db_count)
        self.assertEqual(db_count, 1)
        self.assertEqual(response.status_code, 201)
    
    # Method to test detailed view
    def test_correct_detail_view(self):
        response = self.createCode()
        res = self.client.get(reverse('getCode', kwargs={'id':response.data['id']}))
        db_data = Codes.objects.filter(id=res.data['id']).values()[0]
        self.assertEqual(db_data, res.data)
        self.assertEqual(res.status_code, 200)
    
    # Method to test update views
    def test_update_view(self):
        response = self.createCode()
        res = self.client.put(reverse('getCode', kwargs={'id':response.data['id']}),
                                    {"category_codes":"A011"})
        self.assertEqual(res.status_code, 200)
    
    # Method to test delete view
    def test_delete_view(self):
        response = self.createCode()
        res = self.client.delete(reverse('deleteCode', kwargs={'id':response.data['id']}))
        self.assertEqual(res.status_code, 204)
    
    # Method to test CSV Upload
    def test_file_upload(self):
        self.createFile()
        data =  open('test.csv','rb')
        data = SimpleUploadedFile(content=data.read(), name=data.name, content_type="multipart/form-data")
        content_type = 'multipart/form-data'
        headers = { 'HTTP_CONTENT_TYPE': content_type,
                    'HTTP_CONTENT_DISPOSITION': 'attachment; filename='+'test_csv'
                    }
        res = self.client.post(self.fileuploadurl, {"file":data}, **headers)
        self.assertEqual(res.status_code, 201)




