from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            'image',
            'thumbnail',
            'get_url',
            "get_image",
            'get_thumbnail',
        )
