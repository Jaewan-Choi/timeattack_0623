from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer


class ItemView(APIView):
    
    def get(self, request):
        print(request)
        item_serialize = ItemSerializer()

        return Response(item_serialize.data, status=status.HTTP_200_OK)

        # if item_serialize.is_valid():
        #     return Response(item_serialize.data, status=status.HTTP_200_OK)
        # return Response(item_serialize.errors, status=status.HTTP_400_BAD_REQUEST)