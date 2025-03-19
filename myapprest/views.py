from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from myapp.models import Report
from .serializers import ReportSerializer

class FileUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        
        if file:
            try:
                report = Report.objects.create(file=file)
                return Response({"Error": False, "data": ReportSerializer(report).data, "message": "File upload successfull"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"Error": True, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": True, "message": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            data = Report.objects.all()
            return Response(ReportSerializer(instance=data, many=True).data)
        except Exception as e:
            return Response({"error": True, "message": str(e)})