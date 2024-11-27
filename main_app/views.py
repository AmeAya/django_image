from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *


class PaintingsApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        paintings = Paintings.objects.all()
        data = PaintingsSerializer(instance=paintings, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        painting = PaintingsSerializer(data=request.data)
        if painting.is_valid():
            painting.save()
            return Response(data={'detail': 'OK!'}, status=status.HTTP_200_OK)
        return Response(data=painting.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        painting_id = request.data.get('id')
        painting = Paintings.objects.get(id=painting_id)

        if request.data.get('image') is not None:
            import os
            from django.conf import settings
            os.remove(f'{settings.MEDIA_ROOT}/{painting.image}')

        painting = PaintingsSerializer(instance=painting, data=request.data, partial=True)
        if painting.is_valid():
            painting.save()
            return Response(data={'detail': 'OK!'}, status=status.HTTP_200_OK)
        return Response(data=painting.errors, status=status.HTTP_400_BAD_REQUEST)
