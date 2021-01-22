from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import AirplaneCollector
from .serializers import AirplaneCollectorSerializer

class AirplaneCollectorController(viewsets.ModelViewSet):
    queryset = AirplaneCollector.objects.all()
    serializer_class = AirplaneCollectorSerializer

class TokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_token(self, request):
        payload = {'JSON WEB TOKEN': 'token'}
        return Response(payload)