import numpy as np
import pandas as pd
from icd.models import Codes
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.mail import EmailMessage
from icd.helper import BulkCreateManager

from .serializers import CodesSerializer, FileUploadSerializer



class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Routes View
@api_view(['GET'])
def getRoutes(request):
    routes = ['api/routes']
    return Response(routes)


# Get/Post Method for Showing and Creating Codes in Model
class CodesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    pagination_class = CustomPagination

# Get/Put Method for Obtaining/Editing Codes by Id in the Model
class CodesDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# Delete Method for Deleting Codes by Id in the Model
class CodesDeleteAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CodesUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    pagination_class = CustomPagination

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        
        df = pd.read_csv(file)
        df = df.replace({np.nan:None})
        df = df.values
        '''''''''
        for index,row in df.iterrows():
            new_file = Codes(
                                id = row['id'],
                                category_codes = row['Category Code'],
                                diagnosis_codes = row['Diagnosis Code'],
                                full_code = row['Full Code'],
                                abbrev_description = row['Abbreviated Description'],
                                full_description = row['Full Description'],
                                category_title = row['Category Title'],
                            )
            new_file.save()
        '''''''''
        bulk_mgr = BulkCreateManager()
        for row in df:
            bulk_mgr.add(Codes(
                                category_codes = row[0],
                                diagnosis_codes = row[1],
                                full_code = row[2],
                                abbrev_description = row[3],
                                full_description = row[4],
                                category_title = row[5],
                            ))
        bulk_mgr.done()

        email = EmailMessage(
                "Upload of Category Codes",
                "Upload Completed",
                'mpharmatakehome@gmail.com',
                ['andrewsboateng137@gmail.com']
            )
        email.send()

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
