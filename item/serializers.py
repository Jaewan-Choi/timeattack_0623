from rest_framework import serializers
from .models import Item as ItemModel


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemModel
        fields = "__all__"

    def validate(self, data):
        return data