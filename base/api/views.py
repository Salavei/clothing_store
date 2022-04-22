from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Items
from . import serializers


@api_view(['GET'])
def getDenim(request):
    items = Items.objects.all()
    serializer_items = serializers.ItemsSerializers(items, many=True)
    return Response(serializer_items.data)


@api_view(['GET'])
def getDenimDetail(request, pk):
    try:
        item = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializers_item = serializers.ItemsSerializers(item, many=False)
    return Response(serializers_item.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/v1/denim',
        'GET /api/v1/denim/:id',
    ]
    return Response(routes)
