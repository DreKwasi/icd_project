from rest_framework import serializers
from icd.models import Codes

# creating a class for serializing the Codes model to enable interaction with the Model
class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__' #assigning all ensures all fields are interacted with depending on the endpoint


# creating a class for serializing the csv file into a format readable by the view
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ('file',)
        