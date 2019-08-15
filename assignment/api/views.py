from rest_framework import generics, viewsets
from . import serializers
from . import models
# Create your views here.


class DataSetView(viewsets.ModelViewSet):
    queryset = models.DataModel.objects.all()
    serializer_class = serializers.DataSetSerializer
