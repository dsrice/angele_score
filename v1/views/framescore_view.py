from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bowring.models.events import Event


class FrameScoreView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            result = {}
            return Response(result)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
