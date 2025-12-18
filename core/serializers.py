from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField(use_url=True)
    class Meta:
        model = Document
        fields = '__all__'
