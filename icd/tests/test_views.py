from .test_setup import TestSetUP
from django.urls import reverse
from icd.models import Codes


class TestViews(TestSetUP):

    def test_correct_list_view(self):
        response = self.client.get(self.codeslisturl)
        self.assertEqual(response.status_code, 200)

    def test_wrong_list_view(self):
        response = self.client.get('api/code')
        self.assertEqual(response.status_code, 404)

    def test_correct_create_view(self):
        prev_db_count = Codes.objects.all().count()
        response = self.createCode()
        db_count = Codes.objects.all().count()
        self.assertNotEqual(prev_db_count, db_count)
        self.assertEqual(db_count, 1)
        self.assertEqual(response.status_code, 201)
    
    def test_correct_detail_view(self):
        response = self.createCode()
        res = self.client.get(reverse('getCode', kwargs={'id':response.data['id']}))
        db_data = Codes.objects.filter(id=res.data['id']).values()[0]
        self.assertEqual(db_data, res.data)
        self.assertEqual(res.status_code, 200)
    

    def test_update_view(self):
        response = self.createCode()
        res = self.client.put(reverse('getCode', kwargs={'id':response.data['id']}),
                                    {"category_codes":"A011"})
        self.assertEqual(res.status_code, 200)
    
    def test_delete_view(self):
        response = self.createCode()
        res = self.client.delete(reverse('deleteCode', kwargs={'id':response.data['id']}))
        self.assertEqual(res.status_code, 204)
    


