from rest_framework import serializers
from . import models
from api.tasks import fetch_and_trigger
from rest_framework.renderers import JSONRenderer


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UrlsModel
        fields = ('website_urls', )


class DataSetSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = super().create(validated_data)
        res = fetch_and_trigger.delay(data.id)
        return data

    class Meta:
        model = models.DataModel
        fields = ('id', 'email', 'website_urls')
