from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

class DocumentListAPI(APIView):
    def get(self, request):
        exam = request.GET.get('exam')
        doc_type = request.GET.get('type')

        qs = Document.objects.filter(is_active=True)

        if exam:
            qs = qs.filter(exam__iexact=exam)

        if doc_type:
            qs = qs.filter(doc_type=doc_type)

        serializer = DocumentSerializer(
            qs,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
from django.shortcuts import render

# Create your views here.
