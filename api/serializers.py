from rest_framework import serializers
from icd.models import Codes

class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__'


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ('file',)
        