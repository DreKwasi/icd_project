import numpy as np #Numpy object to handle arrays
import pandas as pd #Pandas for handling importst
from icd.models import Codes #Codes table for exporting and importing data
from rest_framework import generics, mixins, status #generics/mixins for API Views and status for the Responses
from rest_framework.decorators import api_view #decorator to handle API views on functions
from rest_framework.pagination import PageNumberPagination #For customizing Pagination with affecting the whole app
from rest_framework.response import Response #For Handling responses of Views
from django.core.mail import EmailMessage #For sending emails via SMTP
from icd.helper import BulkCreateManager #Helper Class for handling bulk inserts of data

from .serializers import CodesSerializer, FileUploadSerializer #serializers for exporting and importing db data


# View the Returns all Endpoints for the Various Views
@api_view(['GET'])
def getRoutes(request):
    routes = [
        "api/codes/ : GET All Codes in DB and POST as well",
        "api/codes/<int:id>/ : GET Detailed View of ICD Code using ID and UPDATE where needed",
        "api/codes/<int:id>/delete : GET Detailed View of ICD Code using ID and DELETE where needed",
        "api/codes/fileupload : POST Codes through a CSV file upload",
    ]
    return Response(routes)


# A CustomPagination Class to paginate for only specified ListViews
class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


# View for Get/Post Methods to show/create ICD Codes into the Model
class CodesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Codes.objects.all() 
    serializer_class = CodesSerializer
    pagination_class = CustomPagination

# View for Get/Put Method to get detailed codes by ID and edit to and fro the Model
class CodesDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    lookup_field = 'id'

    # defining a method for partial updates to allow only parts of the non-required fields to be edited
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# View for Delete Method to delete Codes by Id in the Model
class CodesDeleteAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    lookup_field = 'id'

    # defining a method for destroying records since a  DestroyModelMixin was used with another view
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# View for Uploading Large Rows of ICD Codes in the Db
class CodesUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    pagination_class = CustomPagination

    # overiding the default post method to allow for file uploads
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        
        # using pandas to read file into dataframes and then vectorizing to numpy for speed
        df = pd.read_csv(file)
        df = df.replace({np.nan:None})
        df = df.values

        # creating a bulkcreatemanager object to handle uploads in chunks
        bulk_mgr = BulkCreateManager(chunk_size=500)
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

        # Sending an email using a dummy gmail account to a specified account
        email = EmailMessage(
                "Upload of ICD Codes",
                f"Thank You for Using the ICD REST Api \nUpload Completed for {df.shape[0]} ICD Codes \
                     Vist http://127.0.0.1:8000/api/codes/ to View or Add Additional Codes",
                'mpharmatakehome@gmail.com',
                ['andrewsboateng137@gmail.com', 'mpharmatakehome@gmail.com']
            )
        email.send()

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
